import cv2 as cv
import numpy as np
import gradio as gr 

def vintage(image):
    sepia_filter = np.array([[0.393, 0.769, 0.189],
                              [0.349, 0.686, 0.168],
                              [0.272, 0.534, 0.131]])
    image = cv.transform(image, sepia_filter)
    return cv.addWeighted(image, 0.8, np.zeros(image.shape, image.dtype), 0, 0)

def snowy(image):
    noise = np.random.normal(0, 25, image.shape).astype(np.uint8)
    return cv.add(image, noise)

def bohemian(image):
    image = cv.GaussianBlur(image, (15, 15), 0)
    return cv.addWeighted(image, 0.6, np.zeros(image.shape, image.dtype), 0, 50)

def black_and_white(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def pencil_sketch(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    inverted = cv.bitwise_not(gray)
    blurred = cv.GaussianBlur(inverted, (21, 21), 0)
    inverted_blurred = cv.bitwise_not(blurred)
    return cv.divide(gray, inverted_blurred, scale=256.0)

def invert_colors(image):
    return cv.bitwise_not(image)

def apply_filter(image, filter_name):
    image = np.array(image)

    if filter_name == "Vintage":
        return vintage(image)
    elif filter_name == "Snowy":
        return snowy(image)
    elif filter_name == "Bohemian":
        return bohemian(image)
    elif filter_name == "Black and White":
        return black_and_white(image)
    elif filter_name == "Pencil Sketch":
        return pencil_sketch(image)
    elif filter_name == "Invert Colors":
        return invert_colors(image)
    else:
        return image  # Default case (no filter)

# Gradio arayüzünü oluştur
with gr.Blocks() as demo:
    gr.Markdown("GÖRSELE FİLTRE UYGULAMA")
    gr.Markdown("Bir resim yükleyin ve bir filtre seçin")

    image_input = gr.Image(type='pil')
    filter_options = gr.Dropdown(choices=["Vintage", "Snowy", "Bohemian", 
                                           "Black and White", "Pencil Sketch", "Invert Colors"], 
                                  label="Filtre Seçin")
    image_output = gr.Image(type="numpy", label="Sonuç resmi")

    # Fonksiyonu Gradio bileşenlerine bağlayalım
    btn = gr.Button("Uygula")
    btn.click(fn=apply_filter, inputs=[image_input, filter_options], outputs=image_output)

# Gradio arayüzünü başlat
if __name__ == "__main__":
    demo.launch(share=True)
