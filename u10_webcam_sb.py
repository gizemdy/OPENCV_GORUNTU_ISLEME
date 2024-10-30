import cv2 as cv

#kamerayı başlat

cap=cv.VideoCapture()

while True:
    ret,frame=cap.read()
    if not ret:
        break
    #gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    hsv_img=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    cv.imshow('kamera',hsv_img)

    if cv.waitKey(1) & 0xFF==ord('q'):
        break

#kamerayı kapat
cap.release()
cv.destroyAllWindows()