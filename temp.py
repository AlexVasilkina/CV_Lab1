import cv2 as cv
import numpy as np

img = cv.imread("raincat.jpg", cv.IMREAD_GRAYSCALE)
norm = np.zeros((800,800))
#print(img.shape)
final = cv.normalize(img,  None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
cv.imshow('Normalized bw Image', final)
cv.imwrite('image_normalized.jpg', final)
cv.waitKey(0)
cv.destroyAllWindows()




