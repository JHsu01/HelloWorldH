import cv2 as cv

img = cv.imread("image.jpg", cv.IMREAD_GRAYSCALE)

#cv.imwrite("test.jpg", img)

cv.namedWindow('image',cv.WINDOW_AUTOSIZE)
cv.imshow('image',img)
cv.waitKey()






