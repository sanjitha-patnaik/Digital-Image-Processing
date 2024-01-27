# Histogram equalization of a high contrast image the pixel spreading graphFpr Gray Image
#FOR GREY IMAGE
import cv2
import matplotlib.pyplot as plt
import numpy as np
image_path = r"image_path"
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
min_val = 50  # Adjust these values to control the contrast
max_val = 200
high_contrast_img = cv2.convertScaleAbs(gray_img, alpha=(255.0 / (max_val - min_val)), beta=(-min_val * 255.0 / 
(max_val - min_val)))
hist_original = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
hist_high_contrast = cv2.calcHist([high_contrast_img], [0], None, [256], [0, 256])
cdf_original = hist_original.cumsum()
cdf_high_contrast = hist_high_contrast.cumsum()
plt.figure(figsize=(12, 8))
plt.subplot(2, 3, 1)
plt.imshow(gray_img, cmap='gray')
plt.title('Original Image')
plt.subplot(2, 3, 4)
plt.plot(hist_original, color='b')
plt.title('Original Histogram')
plt.subplot(2, 3, 2)
plt.imshow(high_contrast_img, cmap='gray')
plt.title('High-Contrast Image')
plt.subplot(2, 3, 5)
plt.plot(hist_high_contrast, color='b')
plt.title('High-Contrast Histogram')
plt.subplot(2, 3, 3)
plt.plot(cdf_original, color='b', label='Original')
plt.plot(cdf_high_contrast, color='r', label='High-Contrast')
plt.title('Pixel Spreading Graph')
plt.legend()
plt.tight_layout()
plt.show()

#For colour image
import cv2
import matplotlib.pyplot as plt
image_path = r"image_path"
color_img = cv2.imread(image_path)
min_val = 50 # Adjust these values to control the contrast
max_val = 200
for i in range(3): # Loop through each color channel (BGR)
 color_img[:,:,i] = cv2.convertScaleAbs(color_img[:,:,i], alpha=(255.0 / (max_val - min_val)), beta=(-min_val * 
255.0 / (max_val - min_val)))
hist_original = [cv2.calcHist([color_img], [i], None, [256], [0, 256]) for i in range(3)]
cdf_original = [hist.cumsum() for hist in hist_original]
plt.figure(figsize=(12, 8))
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB))
plt.title('Original Color Image')
for i, color in enumerate(['b', 'g', 'r']):
 plt.subplot(2, 3, i + 2)
 plt.plot(hist_original[i], color=color)
 plt.title(f'Original {color.upper()} Histogram')
  
# Pixel Spreading Graph for Original Image
plt.subplot(2, 3, 5)
for i, color in enumerate(['b', 'g', 'r']):
 plt.plot(cdf_original[i], color=color, label=f'{color.upper()} Channel')
plt.title('Pixel Spreading Graph (Original Image)')
plt.legend()
plt.tight_layout()
plt.show()

