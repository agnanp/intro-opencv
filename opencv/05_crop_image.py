import cv2

img = cv2.imread("data/image.jpg")

"""
Image slicing for cropping:
img[y_start:y_end, x_start:x_end]

This selects a rectangular region from the image
y_start:y_end specifies the vertical range (rows)
x_start:x_end specifies the horizontal range (columns)

"""

cropped = img[400:600, 400:600]


cv2.imshow("cropped_0", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
