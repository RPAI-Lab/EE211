import cv2
import numpy as np

# Load the image
img = cv2.imread('./images/demo.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to segment the image
_, thresholded = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# Show the original and thresholded images
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()
