import cv2 as cv
#resmi oku
img=cv.imread(r'data/yesil_elma.jpg')

#goruntunun boyutlarını al(yukseklık ve genıslık)
height,width=img.shape[:2]
channels=img.shape[2]
print(height,width)

#goruntnun veri tipini al
data_type=img.dtype

# Bilgileri yazdır
print(f"Görüntü Yüksekliği: {height} piksel")
print(f"Görüntü Genişliği: {width} piksel")
print(f"Kanal Sayısı: {channels}")
print(f"Veri Tipi: {data_type}")

# Görüntüyü göster (isteğe bağlı)
cv.imshow("Goruntu", img)
cv.waitKey(0)
cv.destroyAllWindows()