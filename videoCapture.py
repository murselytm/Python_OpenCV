import cv2

cap = cv2.VideoCapture(cv2.CAP_DSHOW)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 2560
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 1440

# WINDOWS -- *'DIVX'
# MACOS OR LINUX *'XVID'

writer = cv2.VideoWriter('C:/Users/0/Desktop/pyVideSave/myvideo2.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 15, (width, height))

while True:

    ret, frame = cap.read()

    # OPERATİONS (DRAWING)
    writer.write(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
