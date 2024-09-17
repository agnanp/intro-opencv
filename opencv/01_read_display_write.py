import cv2

# Reading an image
img = cv2.imread("data/image.jpg", cv2.IMREAD_COLOR)

# Displaying the image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Writing the image
cv2.imwrite("data/output.jpg", img)
