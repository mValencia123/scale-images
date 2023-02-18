import cv2 as cv
import numpy as np

img = cv.imread('test-2.jpg')

cv.imshow('img',img)

# imgB = img.copy()
# imgB[:,:,1] = 0
# imgB[:,:,2] = 0
# cv.imshow('imgB',imgB)

# imgR = img.copy()
# imgR[:,:,1] = 0
# imgR[:,:,0] = 0
# cv.imshow('imgR',imgR)

# imgG = img.copy()
# imgG[:,:,0] = 0
# imgG[:,:,2] = 0
# cv.imshow('imgG',imgG)

# imgB_gray = img[:,:,0]
# cv.imshow('imgB_gray',imgB_gray)

# imgG_gray = img[:,:,1]
# cv.imshow('imgG_gray',imgG_gray)


# imgR_gray = img[:,:,2]
# cv.imshow('imgR_gray',imgR_gray)




img_Prom = np.uint8((np.double(img[:,:,0]) + np.double(img[:,:,1]) + np.double(img[:,:,2]))/ 3)
img_uma = np.uint8(((np.double(img[:,:,0]) * 0.11) + (np.double(img[:,:,1]) * 0.59) + (np.double(img[:,:,2]) * 0.3))/ 3)

cv.imshow('img_Prom',img_Prom)
cv.imshow('img_uma',img_uma)
cv.waitKey(0) 