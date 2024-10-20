import cv2

# Load the input image
input_image = cv2.imread('./images/demo.jpg')

# Convert the input image to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Create a SIFT object for feature detection and extraction
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors for the input image
keypoints, descriptors = sift.detectAndCompute(gray_image, None)

# Draw the detected keypoints on the input image
output_image = cv2.drawKeypoints(input_image, keypoints, None)

# Show the output image
cv2.imshow('Output Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
