import cv2
import numpy as np

# Load the image
img = cv2.imread('./images/demo.jpg')

# Resize the image
resized = cv2.resize(img, (600, 400), interpolation=cv2.INTER_AREA)

# Crop the image
cropped = resized[100:300, 200:400]

# Show the original, resized, and cropped images
cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', resized)
cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
