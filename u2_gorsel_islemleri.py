import cv2 as cv
img=cv.imread('data/satranc3x3.jpg')

print(img)


cv.imshow('Stranc 3x3 @techist',img)

cv.waitKey(0)

cv.destroyAllWindows()