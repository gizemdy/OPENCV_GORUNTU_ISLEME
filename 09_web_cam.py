import cv2 as cv

#kameradan video akışını başlat

cap=cv.VideoCapture(0) # 0=varsayılan kamera

while True:
    ret,frame=cap.read()
    cv.imshow('kamera',frame)

    if cv.waitKey(1) & 0xFF==ord('q'):
        break

'''

    cv.waitKey(0)

cap.release()
cv.destroyAllWindows()
'''