import cv2

# Load the image
img = cv2.imread("./images/demo.jpg")

# Apply Gaussian filter
filtered = cv2.GaussianBlur(img, (15, 15), 0)

# Display the original and filtered images side by side
cv2.imshow("Original", img)
cv2.imshow("Filtered", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
