#For Gray image
import cv2
import scipy.ndimage
import matplotlib.pyplot as plt
image = cv2.imread(r"image_path", cv2.IMREAD_GRAYSCALE)
mask_sizes = [3, 5, 9]
for mask_size in mask_sizes:
 output_image = scipy.ndimage.median_filter(image, size=mask_size)
 plt.figure()
 plt.imshow(image, cmap='gray')
 plt.title(f'Input Image - Mask Size: {mask_size}')
 plt.axis('off')
 
 plt.figure()
 plt.imshow(output_image, cmap='gray')
 plt.title(f'Median Filter Output - Mask Size: {mask_size}')
 plt.axis('off')
 plt.show()


#For Colour image
import cv2
import scipy.ndimage
import matplotlib.pyplot as plt
image = cv2.imread(r"C:\Users\DEVI\Downloads\sanju-img.jpeg")
b, g, r = cv2.split(image)
mask_sizes = [3, 5, 9]
for mask_size in mask_sizes:
 b_filtered = scipy.ndimage.median_filter(b, size=mask_size)
 g_filtered = scipy.ndimage.median_filter(g, size=mask_size)
 r_filtered = scipy.ndimage.median_filter(r, size=mask_size)
 output_image = cv2.merge((b_filtered, g_filtered, r_filtered))
 plt.figure()
 plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
 plt.title(f'Input Color Image - Mask Size: {mask_size}')
 plt.axis('off')
 plt.figure()
 plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
 plt.title(f'Median Filter Output - Mask Size: {mask_size}')
 plt.axis('off')
 plt.show()
