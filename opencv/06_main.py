import cv2


def main():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        width, height = frame.shape[:2]

        print(f"width: {width}, height: {height}")

        frame_crop = frame[100:400, 100:600]
        frame_resize = cv2.resize(frame, (height // 2, width // 2))

        cv2.imshow("frame", frame)
        cv2.imshow("frame crop", frame_crop)
        cv2.imshow("frame resize", frame_resize)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
