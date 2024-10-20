import cv2
import numpy as np

# Load the image
img = cv2.imread('./images/demo.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a histogram equalization to enhance the image contrast
enhanced = cv2.equalizeHist(gray)

# Show the original and enhanced images
cv2.imshow('Original Image', img)
cv2.imshow('Enhanced Image', enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
