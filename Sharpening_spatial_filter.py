import cv2
import numpy as np
image = cv2.imread(r"image_path")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
sharpened_image = cv2.addWeighted(gray_image, 1.5, laplacian, -0.5, 0)
output_image = cv2.merge((sharpened_image, sharpened_image, sharpened_image))

# Save and display the output sharpened color image
cv2.imwrite('output_sharpened_color_image.jpg', output_image)
cv2.imshow('Output Sharpened Color Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
