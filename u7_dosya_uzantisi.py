import cv2 as cv

img=cv.imread(r'data\satranc3x3.jpg')
b, g, r=cv.split(img)

mavi_img=cv.merge((r,g,b))


cv.imshow('mavi dama',mavi_img)
cv.imwrite('data/mavi_dama.jpg',mavi_img)


#kanalları göster

cv.imshow('satranc 3x3',img)
cv.imshow('blue kanali',b)
cv.imshow('green kanali',g)
cv.imshow('red kanali',r)


cv.waitKey(0)
cv.destroyAllWindows()