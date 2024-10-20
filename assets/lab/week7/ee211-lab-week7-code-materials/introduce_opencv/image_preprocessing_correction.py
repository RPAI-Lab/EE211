import cv2

# Load the image
img = cv2.imread('./images/demo.jpg')

# Apply histogram equalization to each color channel
equalized = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
equalized[:, :, 0] = cv2.equalizeHist(equalized[:, :, 0])
equalized = cv2.cvtColor(equalized, cv2.COLOR_YUV2BGR)

# Display the original and equalized images side by side
cv2.imshow('Original', img)
cv2.imshow('Equalized', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
