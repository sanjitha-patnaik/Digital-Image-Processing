#EROSION
#Erosion is a morphological operation that shrinks or erodes the boundaries of objects in a binary image by removing pixels based on the defined structuring element.
import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread(r"image_path", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8) # You can adjust the size of the kernel
erosion_result = cv2.erode(image, kernel, iterations=1)
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(122), plt.imshow(erosion_result, cmap='gray'), plt.title('Eroded')
plt.show()


#DILATION
#Dilation is a morphological operation that expands or dilates the boundaries of objects in a binary image by adding pixels based on the defined structuring element.

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


#OPENING
#Opening is a morphological operation that combines an erosion operation followed by a dilation operation, useful for removing noise and small objects while preserving the structural integrity of larger objects in a binary image.

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


# CLOSING
#Closing is a morphological operation that combines a dilation operation followed by an erosion operation, effective in closing small gaps and filling holes in objects within a binary image.
import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load an example image 
image = cv2.imread(r"image_path", cv2.IMREAD_GRAYSCALE)
# Define a kernel for closing
kernel = np.ones((5, 5), np.uint8) # You can adjust the size of the kernel
# Perform closing
closing_result = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
# Display the original and closed images
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(122), plt.imshow(closing_result, cmap='gray'), plt.title('Closed')
plt.show()


#BOUNDARY EXTRACTION
#Boundary extraction is a process that involves highlighting the edges or boundaries of objects in an image by subtracting a morphologically eroded version of the image from the original, emphasizing the object contours.

import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load an example image 
image = cv2.imread(r"image_path", cv2.IMREAD_GRAYSCALE)
# Define a kernel for erosion
kernel = np.ones((5, 5), np.uint8) # You can adjust the size of the kernel
# Perform erosion
erosion_result = cv2.erode(image, kernel, iterations=1)
# Extract the boundary by subtracting the eroded image from the original image
boundary_result = cv2.absdiff(image, erosion_result)
# Display the original, eroded, and boundary images
plt.subplot(131), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(132), plt.imshow(erosion_result, cmap='gray'), plt.title('Eroded')
plt.subplot(133), plt.imshow(boundary_result, cmap='gray'), plt.title('Boundary')
plt.show()


#HIT AND MISS TRANSFORM
#Hit-and-Miss transform is a morphological operation used for precise pattern matching in binary images by applying both foreground and background structuring elements to identify specific configurations or features.

import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread(r"image_path", cv2.IMREAD_GRAYSCALE)
hit_kernel = np.array([[0, 1, 0],
 [0, 1, 1],
 [0, 1, 0]], dtype=np.uint8)
miss_kernel = np.array([[1, 0, 1],
 [1, 0, 0],
 [1, 0, 1]], dtype=np.uint8)
hit_miss_result = cv2.morphologyEx(image, cv2.MORPH_HITMISS, hit_kernel, borderType=cv2.BORDER_CONSTANT, 
borderValue=255)
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(122), plt.imshow(hit_miss_result, cmap='gray'), plt.title('Hit-or-Miss Result')
plt.show()


#HOLE FILLING
#Hole filling is a morphological operation that involves using dilation to fill small gaps or holes in objects within a binary image, resulting in a more connected and complete representation

import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load an example binary image 
image = cv2.imread(r"image_path", cv2.IMREAD_GRAYSCALE)
# Threshold the image to create a binary image if it's not binary already
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
# Define a kernel for dilation
kernel = np.ones((5, 5), np.uint8) # You can adjust the size of the kernel
# Perform dilation to fill holes
filled_image = cv2.dilate(binary_image, kernel, iterations=1)
# Display the original and filled images
plt.subplot(121), plt.imshow(binary_image, cmap='gray'), plt.title('Original Binary Image')
plt.subplot(122), plt.imshow(filled_image, cmap='gray'), plt.title('Filled Image')
plt.show()


