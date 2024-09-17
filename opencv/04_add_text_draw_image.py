import cv2
import numpy as np

# Create a white image
white_image = 255 * np.ones((500, 500, 3), dtype=np.uint8)

image_text = white_image.copy()
# add text to image
text = "Hello World!"
font = cv2.FONT_HERSHEY_SIMPLEX
bottom_left_corner_of_text = (100, 100)
font_scale = 1
font_color = (255, 0, 0)
thickness = 2

cv2.putText(
    image_text,
    text,
    bottom_left_corner_of_text,
    font,
    font_scale,
    font_color,
    thickness,
)

# Make copy of the image
image_line = white_image.copy()
# Draw the image from point A to B
point_a = (200, 80)
point_b = (450, 80)
cv2.line(image_line, point_a, point_b, (255, 255, 0), thickness=3)


# Make copy of the image
image_circle = white_image.copy()
# Draw the image from point A to B
point_a = (200, 200)
radius = 100
cv2.circle(image_circle, point_a, radius, (255, 255, 0), thickness=-1)

# Make copy of the image
image_rectangle = white_image.copy()
# Draw a rectangle on the image
top_left = (150, 150)
bottom_right = (350, 350)
cv2.rectangle(image_rectangle, top_left, bottom_right, (0, 255, 0), thickness=2)

cv2.imshow("white_image", white_image)
cv2.imshow("image_text", image_text)
cv2.imshow("image line", image_line)
cv2.imshow("image circle", image_circle)
cv2.imshow("image rectangle", image_rectangle)

cv2.waitKey(0)
cv2.destroyAllWindows()
