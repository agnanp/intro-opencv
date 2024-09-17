import cv2

img = cv2.imread("data/image.jpg")

# resize image using dsize
resized_0 = cv2.resize(img, (480, 640))
cv2.imshow("resized_0", resized_0)

# resize image using fx and fy
resized_1 = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
cv2.imshow("resized_1", resized_1)

# resize image with interpolation
resized_2 = cv2.resize(img, (0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_NEAREST)
cv2.imshow("resized_2", resized_2)

# resize image with interpolation
resized_3 = cv2.resize(img, (0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
cv2.imshow("resized_3", resized_3)

# resize image with interpolation
resized_4 = cv2.resize(img, (0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
cv2.imshow("resized_4", resized_4)

# resize image with interpolation
resized_5 = cv2.resize(img, (0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC)
cv2.imshow("resized_5", resized_5)

cv2.waitKey(0)
cv2.destroyAllWindows()
