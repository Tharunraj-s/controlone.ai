import cv2
import numpy as np
# Create blank images for each shape
line_image = np.zeros((400, 400, 3), dtype=np.uint8)
rectangle_image = np.zeros((400, 400, 3), dtype=np.uint8)
ellipse_image = np.zeros((400, 400, 3), dtype=np.uint8)
circle_image = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw a line
cv2.line(line_image, (50, 50), (350, 50), (0, 0, 255), 2)
# Draw a rectangle
cv2.rectangle(rectangle_image, (100, 100), (300, 300), (0, 255, 0), 2)
# Draw an ellipse
cv2.ellipse(ellipse_image, (200, 200), (100, 50), 0, 0, 360, (255, 0, 0), 2)
# Draw a circle
cv2.circle(circle_image, (200, 200), 50, (255, 255, 255), -1)  # -1 for filled circle

# Display the image
cv2.imshow("Line", line_image)
cv2.waitKey(1000)  # Display for 1 second (1000 milliseconds)
cv2.imshow("Rectangle", rectangle_image)
cv2.waitKey(1000)
cv2.imshow("Ellipse", ellipse_image)
cv2.waitKey(1000)
cv2.imshow("Circle", circle_image)
# Wait for a key press and close all windows when any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
