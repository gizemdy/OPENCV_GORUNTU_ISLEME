import cv2 as cv
import numpy as np
import gradio as gr 

def nostalji(image):
    image = np.array(image)
    # BAYER formatı yerine doğrudan BGR formatına çeviriyoruz
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return gray_image

# Gradio arayüzünü oluştur
with gr.Blocks() as demo:
    gr.Markdown("Görseli siyah beyaza çevir")
    gr.Markdown("Bir resim yükleyin")

    image_input = gr.Image(type='pil')
    image_output = gr.Image(type="numpy", label="Sonuç resmi")

    # Fonksiyonu Gradio bileşenlerine bağlayalım
    btn = gr.Button("Çevir")
    btn.click(fn=nostalji, inputs=image_input, outputs=image_output)

# Gradio arayüzünü başlat
if __name__ == "__main__":  
    demo.launch(share=True)
