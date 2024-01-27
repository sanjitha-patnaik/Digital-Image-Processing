#Gaussian Noise
import cv2
import numpy as np

# Function to add Gaussian noise to an image
def add_gaussian_noise(image, mean=0, std=25):
 noisy_image = np.copy(image)
 gaussian_noise = np.random.normal(mean, std, image.shape).astype(np.uint8)
 noisy_image = cv2.add(image, gaussian_noise)
 return noisy_image
  
# Function to remove Gaussian noise using Wiener filter
def remove_gaussian_noise_wiener(image, noise_var):
 psf = np.ones((5, 5)) / 25 # Point Spread Function (PSF) for Wiener filter
 restored_image = cv2.filter2D(image, -1, psf) + noise_var / 255
 wiener_filter = 1 / (1 + noise_var / 255)
 restored_image *= wiener_filter
 return restored_image.astype(np.uint8)

# Read the input image
image_path = r"image_path"
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Add Gaussian noise to the original image
gaussian_noisy_image = add_gaussian_noise(original_image)

# Remove Gaussian noise using Wiener filter
denoised_gaussian_image = remove_gaussian_noise_wiener(gaussian_noisy_image, noise_var=25)

# Display the images
cv2.imshow("Original Image", original_image)
cv2.imshow("Gaussian Noisy Image", gaussian_noisy_image)
cv2.imshow("Denoised Gaussian Image", denoised_gaussian_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

