import cv2
import numpy as np

# Function to convert image to HSV and apply threshold
def threshold_red(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    return cv2.bitwise_or(mask1, mask2)

# Function to check if a region can be approximated by a circle
def is_approx_circle(contour, accuracy=0.04):
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, accuracy * perimeter, True)
    return len(approx) == 3 and cv2.isContourConvex(contour)

# Load the image
image = cv2.imread('./images/red.png')


# Threshold the image to get only red color
red_mask = threshold_red(image)

cv2.imshow('Original', image)
cv2.imshow('Red_Filtered', red_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
