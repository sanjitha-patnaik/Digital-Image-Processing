#EROSION
import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread(r"image_path", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8) # You can adjust the size of the kernel
erosion_result = cv2.erode(image, kernel, iterations=1)
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(122), plt.imshow(erosion_result, cmap='gray'), plt.title('Eroded')
plt.show()


#Dilation
import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load an example image 
image = cv2.imread(r"image_path", cv2.IMREAD_GRAYSCALE)
# Define a kernel for dilation
kernel = np.ones((5, 5), np.uint8) # You can adjust the size of the kernel
# Perform dilation
dilation_result = cv2.dilate(image, kernel, iterations=1)
# Display the original and dilated images
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(122), plt.imshow(dilation_result, cmap='gray'), plt.title('Dilated')
plt.show()


#Opening
import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load an example image (replace with your own image)
image = cv2.imread(r"image_path", cv2.IMREAD_GRAYSCALE)
# Define a kernel for opening
kernel = np.ones((5, 5), np.uint8) # You can adjust the size of the kernel
# Perform opening
opening_result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
# Display the original and opened images
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(122), plt.imshow(opening_result, cmap='gray'), plt.title('Opened')
plt.show()