#kırmızı rengi yeşile cevirme
import cv2 as cv
img_bgr=cv.imread(r'data/elma.jpg')


#orijinali göster
cv.imshow('Kirmizi elma', img_bgr)
b,g,r=cv.split(img_bgr)

#kırmızı ve yesil kanalları birleştir

img_yesil=cv.merge((b,r,g))
img_mavi=cv.merge((r,g,b))

#yesil ve mavi renkli elmayı göster
cv.imshow('Yesil elma',img_yesil)
cv.imshow('Mavi elma',img_mavi)


cv.waitKey(0)
cv.destroyAllWindows()