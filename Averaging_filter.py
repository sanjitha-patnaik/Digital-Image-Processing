#For Gray image
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread(r"image_path", cv2.IMREAD_GRAYSCALE)
mask_sizes = [3, 5, 9]
for mask_size in mask_sizes:
 kernel = np.ones((mask_size, mask_size), np.float32) / (mask_size * mask_size)
 output_image = cv2.filter2D(image, -1, kernel)
 plt.figure()
 plt.imshow(image, cmap='gray')
 plt.title(f'Input Image - Mask Size: {mask_size}')
 plt.axis('off')
 
 plt.figure()
 plt.imshow(output_image, cmap='gray')
 plt.title(f'Averaging Filter Output - Mask Size: {mask_size}')
 plt.axis('off')
 plt.show()



#For Colour image
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread(r"image_path")
b, g, r = cv2.split(image)
mask_sizes = [3, 5, 9]
for mask_size in mask_sizes:
 kernel = np.ones((mask_size, mask_size), np.float32) / (mask_size * mask_size)
 b_filtered = cv2.filter2D(b, -1, kernel)
 g_filtered = cv2.filter2D(g, -1, kernel)
 r_filtered = cv2.filter2D(r, -1, kernel)
 output_image = cv2.merge((b_filtered, g_filtered, r_filtered))
 plt.figure()
 plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
 plt.title(f'Input Color Image - Mask Size: {mask_size}')
 plt.axis('off')
 plt.figure()
 plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
 plt.title(f'Averaging Filter Output - Mask Size: {mask_size}')
 plt.axis('off')
 plt.show()

