import cv2
import numpy as np

# Input
orig = cv2.imread("test.png")
cv2.imshow("Original", orig)
# Convert BGR to HSV
hsv = cv2.cvtColor(orig, cv2.COLOR_BGR2HSV)

# Define ranges of color in HSV color space
lower_red = np.array([0, 50, 70])
upper_red = np.array([5, 255, 255])

lower_orange = np.array([6, 50, 70])
upper_orange = np.array([15, 255, 255])

lower_yellow = np.array([16, 50, 70])
upper_yellow = np.array([35, 255, 255])

lower_green = np.array([36, 50, 70])
upper_green = np.array([89, 255, 255])

lower_blue = np.array([90, 50, 70])
upper_blue = np.array([125, 255, 255])

lower_magenta = np.array([126, 50, 70])
upper_magenta = np.array([160, 255, 255])

# Threshold the HSV image
red_mask = cv2.inRange(hsv, lower_red, upper_red)
red_res = cv2.bitwise_and(orig,orig, mask= red_mask)

orange_mask = cv2.inRange(hsv, lower_orange, upper_orange)
orange_res = cv2.bitwise_and(orig,orig, mask= orange_mask)

yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
yellow_res = cv2.bitwise_and(orig,orig, mask= yellow_mask)

green_mask = cv2.inRange(hsv, lower_green, upper_green)
green_res = cv2.bitwise_and(orig,orig, mask= green_mask)

blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
blue_res = cv2.bitwise_and(orig,orig, mask= blue_mask)

magenta_mask = cv2.inRange(hsv, lower_magenta, upper_magenta)
magenta_res = cv2.bitwise_and(orig,orig, mask= magenta_mask)

# Show output
cv2.imshow("Red", red_res)
cv2.imshow("Orange", orange_res)
cv2.imshow("Yellow", yellow_res)
cv2.imshow("Green", green_res)
cv2.imshow("Blue", blue_res)
cv2.imshow("Magenta", magenta_res)

cv2.waitKey()