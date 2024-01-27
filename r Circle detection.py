import cv2
import numpy as np
def detect_and_display_circles(image_path, min_radius=20, max_radius=100, param1=50, param2=30):
 image = cv2.imread(image_path)
 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 blurred = cv2.GaussianBlur(gray, (5, 5), 0)
 circles = cv2.HoughCircles(
 blurred, 
 cv2.HOUGH_GRADIENT, dp=1, minDist=20,
 param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius
 )
 if circles is not None:
 circles = np.uint16(np.around(circles))
 for i in circles[0, :]:
 cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
 cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)
 cv2.imshow('Original Image', cv2.imread(image_path))
 cv2.imshow('Detected Circles', image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
  #Add an original image path
input_image_path = r"image_path"
detect_and_display_circles(input_image_path)

