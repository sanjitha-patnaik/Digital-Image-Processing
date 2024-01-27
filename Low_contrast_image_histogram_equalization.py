# Histogram equalization of a low contrast image and pixel spreading graph for gray image
import cv2
import matplotlib.pyplot as plt
import numpy as np
# Path to the image file
image_path = r"image_path"
# Read the image as grayscale
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# Apply histogram equalization
equ = cv2.equalizeHist(img)
hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_equalized = cv2.calcHist([equ], [0], None, [256], [0, 256])
# Calculate pixel spreading graph
cdf_original = hist_original.cumsum()
cdf_equalized = hist_equalized.cumsum()
plt.figure(figsize=(12, 8))

# Original Image and Histogram
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.subplot(2, 3, 4)
plt.plot(hist_original, color='b')
plt.title('Original Histogram')
plt.subplot(2, 3, 2)
plt.imshow(equ, cmap='gray')
plt.title('Equalized Image')
plt.subplot(2, 3, 5)
plt.plot(hist_equalized, color='b')
plt.title('Equalized Histogram')
plt.subplot(2, 3, 3)
plt.plot(cdf_original, color='b', label='Original')
plt.plot(cdf_equalized, color='r', label='Equalized')
plt.title('Pixel Spreading Graph')
plt.legend()
plt.tight_layout()
plt.show()


#For Colour Image
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the low contrast color image
low_contrast_color_image = cv2.imread(r"image_path")

# Convert the image to YUV color space for better luminance equalization
yuv_image = cv2.cvtColor(low_contrast_color_image, cv2.COLOR_BGR2YUV)

# Equalize the histogram of the Y channel (luminance)
yuv_image[:,:,0] = cv2.equalizeHist(yuv_image[:,:,0])

# Convert the image back to BGR color space
equalized_color_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)
hist_original_channels = [cv2.calcHist([low_contrast_color_image], [i], None, [256], [0, 
256]) for i in range(3)]
hist_equalized_channels = [cv2.calcHist([equalized_color_image], [i], None, [256], [0, 
256]) for i in range(3)]
hist_original = np.concatenate([hist.flatten() for hist in hist_original_channels])
hist_equalized = np.concatenate([hist.flatten() for hist in hist_equalized_channels])
plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1)
plt.plot(hist_original, color='black')
plt.title('Histogram of Low Contrast Color Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.subplot(1, 3, 2)
plt.plot(hist_equalized, color='gray')
plt.title('Histogram of Equalized Color Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(low_contrast_color_image, 
cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 6))
plt.plot(np.arange(256), np.arange(256), color='black', 
label='Original')
plt.plot(np.arange(256), hist_equalized, color='gray', 
label='Equalized')
plt.title('Pixel Spreading Graph')
plt.xlabel('Original Pixel Value')
plt.ylabel('Equalized Pixel Value')
plt.legend()
plt.grid(True)
plt.show()

