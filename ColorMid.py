import cv2
import numpy as np

image_width = 800
image_height = 600

black_image = np.zeros((image_height, image_width, 3), dtype=np.uint8)
white_region_width = 100
white_region_height =  100
x_center = image_width // 2
y_center = image_height // 2
print("x center : {} \n y center :{}".format(x_center,y_center))
x_start = x_center - white_region_width // 2
y_start = y_center - white_region_height // 2
print("x center : {} \n y center :{}".format(x_start,y_start))

x_end = x_start + white_region_width
y_end = y_start + white_region_height
print("x center : {} \n y center :{}".format(x_end,y_end))
black_image[y_start:y_end, x_start:x_end] = (255, 255, 255)
cv2.imshow("Black Image with White Region", black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
