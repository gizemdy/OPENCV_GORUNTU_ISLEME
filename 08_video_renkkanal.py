import cv2 as cv
import numpy as numpy

#giriş ve çıkkış video

input_video=r'data/araba_video.mp4'
output_video=r'data/araba_output.mp4'

#video yakalama

cap=cv.VideoCapture(input_video)

#video özelliklerine bak
fourcc=cv.VideoWriter_fource(*'mp4v')   #kodek
fps=int(cap.get(cv.CAP_PROP_FPS)) #saniyedeki frame sayısı
width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH)) #genislik
height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)) #yukseklik

#kodek=cap.get(cv.CAP_PROP_FOURCC)

out=cv.VideoWriter(output_video,fourcc,fps,(width,height)) #videomuzu belirtilen özelliklerde oluştur

while cap.isOpened():
    ret,frame=cap.read()

    if not ret: #okuma başarılı ise
        break
    
    b,g,r=cv.split(frame)

    rgb_frame=cv.merge((r,g,b))

    cv.imshow('mavi video',rgb_frame)

    out.write(rgb_frame) #videoya yaz
    if cv.waitKey(1) & 0xFF == ord('q'):    #q tuşuna basıldığında
        break
cap.release()
out.release()
cv.destroyAllWindows()
