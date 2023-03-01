import cv2
import numpy as np

# Create a function based on a CV2 Event (Left button click)


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global center, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x, y)
        clicked = False

    # get mouse click on down and track center
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

    # Use boolean variable to track if the mouse has been released


# Haven't drawn anything yet!
center = (0, 0)
clicked = False

# Capture Video
cap = cv2.VideoCapture(0)

# Create a named window for connections
cv2.namedWindow('frame')

# Bind draw_rectangle function to mouse cliks

cv2.setMouseCallback('frame', draw_circle)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Use if statement to see if clicked is true
    if clicked == True:
        cv2.circle(frame, center, radius=50, color=(255, 0, 0), thickness=5)
    # Draw circle on frame

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Simply pressing X on the window won't work!


# When everything is done, release the capture
cv2.release()
cv2.destroyAllWindows()