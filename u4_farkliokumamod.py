import cv2 as cv
resim_dosyasi='data\satranc3x3.jpg'
resim_dosyasi2='data\elma.jpg'

#renkli yap
img_color=cv.imread(resim_dosyasi,1)
#img_color=cv.imread(resim_dosyasi,1)


#siyah beyaz yap
img_grey=cv.imread(resim_dosyasi,0)
elma_grey=cv.imread(resim_dosyasi2,0)


cv.imshow('Renkli',img_color)
cv.imshow('Siyah-beyaz',img_grey)
cv.imshow('gri elma',elma_grey)
cv.waitKey(0)
cv.destroyAllWindows()