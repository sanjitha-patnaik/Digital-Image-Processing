import cv2
import numpy as np
def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
 noisy_image = np.copy(image)
 total_pixels = image.size
 num_salt = int(total_pixels * salt_prob)
 num_pepper = int(total_pixels * pepper_prob)
 
 salt_coords = tuple(np.random.randint(0, i - 1, num_salt) for i in image.shape)
 pepper_coords = tuple(np.random.randint(0, i - 1, num_pepper) for i in image.shape)
 
 noisy_image[salt_coords] = 255
 noisy_image[pepper_coords] = 0
 return noisy_image
  
# Function to remove salt and pepper noise using median filter
def remove_salt_and_pepper_noise_median(image, filter_size=3):
 denoised_image = cv2.medianBlur(image, filter_size)
 return denoised_image
  
# Read the input image
image_path = r"image_path"
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Add salt and pepper noise to the original image
salt_and_pepper_noisy_image = add_salt_and_pepper_noise(original_image, salt_prob=0.02, 
pepper_prob=0.02)

# Remove salt and pepper noise using median filter
denoised_salt_and_pepper_image = remove_salt_and_pepper_noise_median(salt_and_pepper_noisy_image)

# Display the images
cv2.imshow("Original Image", original_image)
cv2.imshow("Salt and Pepper Noisy Image", salt_and_pepper_noisy_image)
cv2.imshow("Denoised Salt and Pepper Image", denoised_salt_and_pepper_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

