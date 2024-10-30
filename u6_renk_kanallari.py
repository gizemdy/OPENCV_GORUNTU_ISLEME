import cv2 as cv

#dosya oku
#img=cv.imread('data/kizil_sac.jpg')
img_ferrari=cv.imread('data/kirmizi_ferrari.jpg')

#b,g,r=cv.split(img)
bf,gf,rf=cv.split(img_ferrari)


#mavi saç
#img_mavi=cv.merge((r,g,b))
#mavi ferrari
mv_fer=cv.merge((rf,gf,bf))

#sari sac
#img_sari=cv.merge((b,r,r))

#laci ferrari
#laci_fer=cv.merge((rf,gf,gf))

#turkuaz
tur_fer=cv.merge((rf,rf,bf))
#pembe ferrari
pembe_fer=cv.merge((rf,gf,rf))

#fotoyu göster
#cv.imshow('orijinal sac', img)
#cv.imshow('mavi sac', img_mavi)
cv.imshow('orijinal ferrari',img_ferrari)
cv.imshow('mavi ferrari',mv_fer)
#cv.imshow('lacivert ferrari',laci_fer)
cv.imshow('turkuaz ferrari',tur_fer)
cv.imshow('pembe ferrari',pembe_fer)


cv.waitKey(0)
cv.destroyAllWindows()