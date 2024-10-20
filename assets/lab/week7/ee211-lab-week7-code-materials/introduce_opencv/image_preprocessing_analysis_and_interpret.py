import cv2
import numpy as np

# Set up the canvas
canvas = np.zeros((480, 640, 3), dtype=np.uint8)
drawing = False
ix, iy = -1, -1
shape = ''

# Define the mouse callback function
def draw_shape(event, x, y, flags, param):
    global canvas, drawing, ix, iy, shape

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(canvas, (ix, iy), (x, y), (0, 0, 255), 2)
            ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(canvas, (ix, iy), (x, y), (0, 0, 255), 2)

        # Convert the canvas to grayscale and threshold it
        gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

        # Find contours in the thresholded image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Identify the shape of the outline
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 500:
                # Ignore small contours
                continue
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
            if len(approx) == 3:
                shape = 'Triangle'
            elif len(approx) == 4:
                shape = 'Rectangle'
            else:
                shape = 'Circle'

# Set up the window and mouse callback
cv2.namedWindow('Canvas')
cv2.setMouseCallback('Canvas', draw_shape)

# Main loop
while True:
    cv2.imshow('Canvas', canvas)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas = np.zeros((480, 640, 3), dtype=np.uint8)
        shape = ''

# Print the final shape
print('Final Shape: {}'.format(shape))

cv2.destroyAllWindows()
