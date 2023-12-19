#!/usr/bin/python

import cv2
from collections import deque

# RTSP stream URL
rtsp_url = 'rtsp://192.168.1.116:8554/stream'


# Create a VideoCapture object to read the RTSP stream
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error: Could not open RTSP stream.")
    exit()

# Enable hardware acceleration if available
cap.set(cv2.CAP_PROP_HW_ACCELERATION, 1)

# Get the initial frame width and height for window sizing
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a resizable window
cv2.namedWindow('Cam Zero 5', cv2.WINDOW_NORMAL)

# Define the size of the frame buffer
buffer_size = 5  # You can adjust this as needed

# Create a deque (double-ended queue) to store frames
frame_buffer = deque(maxlen=buffer_size)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Store the frame in the buffer
    frame_buffer.append(frame)

    # Display the frames from the buffer in the resizable window
    for buffered_frame in frame_buffer:
        cv2.imshow('Cam Zero 5', buffered_frame)

    # Check for the 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close the window
cap.release()
cv2.destroyAllWindows()
