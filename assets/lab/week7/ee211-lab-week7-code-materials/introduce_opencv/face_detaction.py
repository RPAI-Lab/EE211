import cv2
import time

# Load the pre-trained classifier
face_cascade = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')

# Initialize the video capture device
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# Initialize variables for calculating average time
total_time = 0
frame_count = 0

while True:
    # Capture frame-by-frame and record start time
    ret, frame = cap.read()
    start_time = time.time()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw a rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Calculate time spent on this frame and update variables
    end_time = time.time()
    time_spent = end_time - start_time
    total_time += time_spent
    frame_count += 1

    # Check for key press and exit if necessary
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture device and close all windows
cap.release()
cv2.destroyAllWindows()

# Calculate and print average time spent per frame
avg_time_per_frame = total_time / frame_count
print("Average time spent per frame: {:.2f} seconds".format(avg_time_per_frame))
