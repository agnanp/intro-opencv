import cv2

# Reading video
video = cv2.VideoCapture(0)

# Get the FPS of the video
fps = video.get(cv2.CAP_PROP_FPS)
print(f"FPS: {fps}")

while True:
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
