import tkinter as tk
from tkinter import filedialog

import cv2

import showImg
from Operaciones import gray, bw, resize, rotate, aritOP, logOP, interpol
from Filtros import blur, gaussBlur, sharpen, canny, emboss, dilate
from Morfologicas import Open, close, gradient
from Segmentacion import umbral, segCanny, contour, k_means, watershed

# Variables globales para almacenar las imagenes originales
img = None

def upload_img():

    global img
    ruta = filedialog.askopenfilename(filetypes=[("Imagenes", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])

    if ruta:

        # Cargar una imagen en color
        img = cv2.imread(ruta)

        # Convertir la imagen de BGR a RGB (OpenCV usa BGR por defecto)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        showImg.show_img(img, "Imagen Original")

        # # Mostrar los botones de procesamiento
        # btn_gray.pack(pady=5)
        # btn_bw.pack(pady=5)
        # btn_resize.pack(pady=5)
        # btn_rotate.pack(pady=5)
        # btn_aritOP.pack(pady=5)
        # btn_logOP.pack(pady=5)
        # btn_interpol.pack(pady=5)
        # btn_blur.pack(pady=5)
        # btn_gaussBlur.pack(pady=5)
        # btn_sharpen.pack(pady=5)
        # btn_canny.pack(pady=5)
        # btn_emboss.pack(pady=5)
        # btn_dilate.pack(pady=5)

        # Mostrar solo los botones de categorías (Operaciones y Filtros)
        btn_operations.pack(pady=5)
        btn_filters.pack(pady=5)
        btn_morph.pack(pady=5)
        btn_segment.pack(pady=5)



# Convierte la imagen a escala de grises
def appGrayscale():
    if img is not None:
        grayImg = gray.grayscale(img)
        showImg.show_img(grayImg, "Esacala de grises")


# Convierte la imagen a blanco y negro (binarización)
def appBlacknWhite():
    if img is not None:
        bwImg = bw.blackNwhite(img)
        showImg.show_img(bwImg, "Blanco y Negro")

# Permite cambiar el tamaño de la imagen
def appResize():
    if img is not None:
        resizedImg = resize.resizeImg(img)
        showImg.show_img(resizedImg, "redimensionar")

# Permite rotar la imagen
def appRotate():
    if img is not None:
        rotatedImg = rotate.rotateImg(img)
        showImg.show_img(rotatedImg, "Rotar")

# Obtiene imagenes realizadas con operaciones aritmeticas entre dos imagenes
def appArit():
    if img is not None:
        aritOP.aritmeticOP(img)

# Permite realizar Operaciones Logicas entre Imagenes
def appLogic():
    if img is not None:
        logOP.logicOP(img)

# Aplica diferentes métodos de interpolación a la imagen.
def appInterpolation():
    if img is not None:
        interpol.interpolation(img)

# Aplicar el filtro de desenfoque
def appBlur():
    if img is not None:
        blurred = blur.blurImg(img)
        showImg.show_img(blurred,"Difuminar")
        
def appGaussBlur():
    if img is not None:
        gaussBlurred = gaussBlur.gaussianBlur(img)
        showImg.show_img(gaussBlurred, "Desenfoque Gaussiano")

def appSharpen():
    if img is not None:
        sharped = sharpen.sharp(img)
        showImg.show_img(sharped, "Nitidez")

# Aplicar el filtro de detección de bordes (Canny)
def appCanny():
    if img is not None:
        edges = canny.cannyImg(img)
        showImg.show_img(edges, "Detección de Bordes (Canny)")

# Aplicar el filtro de relieve
def appEmboss():
    if img is not None:
        embossed = emboss.embossImg(img)
        showImg.show_img(embossed, "Relieve")

def appDilate():
    if img is not None:
        dilated = dilate.dilateImg(img)
        showImg.show_img(dilated, "Dilatación")

def appOpening():
    if img is not None:
        openImg = Open.opening(img)
        showImg.show_img(openImg, "Apertura")

def appClosing():
    if img is not None:
        closeImg = close.closing(img)
        showImg.show_img(closeImg,"Cierre")

def appGradient():
    if img is not None:
        boardedImg = gradient.boardDetection(img)
        showImg.show_img(boardedImg,"Deteccion de Bordes")

def appThreshold():
    if img is not None:
        umbral.thresholding(img)

def appSegCanny():
    if img is not None:
        segCanny.segmentCanny(img)

def appContour():
    if img is not None:
        conturImg = contour.segContour(img)
        showImg.show_img(conturImg,"Segmentaciòn por Contornos")

def appKmeans():
    if img is not None:
        kmeansImg = k_means.kmeans(img)
        showImg.show_img(kmeansImg,"Segmentaciòn k-means")

def appWatershed():
    if img is not None:
        watershedImg = watershed.segWatershed(img)
        showImg.show_img(watershedImg,"Segmentaciòn Watershed")

# # Crear la interfaz gráfica
# root = tk.Tk()
# root.title("Procesador de Imágenes")

# btn_upload = tk.Button(root, text="Cargar Imagen", command=upload_img)
# btn_upload.pack(pady=70)

# # Botones de procesamiento (inicialmente ocultos)
# btn_gray = tk.Button(root, text="Escala de Grises", command=appGrayscale)
# btn_bw = tk.Button(root, text="Blanco y Negro", command=appBlacknWhite)
# btn_resize = tk.Button(root, text="Redimensiòn", command=appResize)
# btn_rotate = tk.Button(root, text="Rotar Imagen", command=appRotate)
# btn_aritOP = tk.Button(root, text="Operaciones Aritmeticas", command=appArit)
# btn_logOP = tk.Button(root, text="Operaciones Lógicas", command=appLogic)
# btn_interpol = tk.Button(root, text="Interpolación", command=appInterpolation)
# btn_blur = tk.Button(root, text="Difuminar", command=appBlur)
# btn_gaussBlur = tk.Button(root, text="Desenfoque Gaussiano", command=appGaussBlur)
# btn_sharpen = tk.Button(root, text="Nitidez", command=appSharpen)
# btn_canny = tk.Button(root, text="Canny", command=appCanny)
# btn_emboss = tk.Button(root, text="Relieve", command=appEmboss)
# btn_dilate = tk.Button(root, text="Dilatación", command=appDilate)

# root.mainloop()

def show_operations():
    """Muestra u oculta los botones de operaciones."""
    if frame_operations.winfo_ismapped():
        frame_operations.pack_forget()  # Ocultar si ya está visible
    else:
        frame_operations.pack(pady=10)  # Mostrar

def show_filters():
    """Muestra u oculta los botones de filtros."""
    if frame_filters.winfo_ismapped():
        frame_filters.pack_forget()  # Ocultar si ya está visible
    else:
        frame_filters.pack(pady=10)  # Mostrar

def show_morph():
    """Muestra u oculta los botones de los filtros morfologicos."""
    if frame_morph.winfo_ismapped():
        frame_morph.pack_forget()  # Ocultar si ya está visible
    else:
        frame_morph.pack(pady=10)  # Mostrar

def show_segment():
    """Muestra u oculta los botones de segmentacion."""
    if frame_segment.winfo_ismapped():
        frame_segment.pack_forget()  # Ocultar si ya está visible
    else:
        frame_segment.pack(pady=10)  # Mostrar


# Crear la ventana principal
root = tk.Tk()
root.title("Procesador de Imágenes")

# Botón para cargar imagen
btn_upload = tk.Button(root, text="Cargar Imagen", command=upload_img)
btn_upload.pack(pady=20)

# Botones de categoría
btn_operations = tk.Button(root, text="Mostrar Operaciones", command=show_operations)
btn_filters = tk.Button(root, text="Mostrar Filtros", command=show_filters)
btn_morph = tk.Button(root, text="Mostrar Morfologicas", command=show_morph)
btn_segment = tk.Button(root, text="Mostrar Segmentacion", command=show_segment)

# --- Marcos para cada grupo de botones ---
frame_operations = tk.Frame(root)
frame_filters = tk.Frame(root)
frame_morph = tk.Frame(root)
frame_segment = tk.Frame(root)

# Botones de operaciones
btn_gray = tk.Button(frame_operations, text="Escala de Grises", command=appGrayscale)
btn_bw = tk.Button(frame_operations, text="Blanco y Negro", command=appBlacknWhite)
btn_resize = tk.Button(frame_operations, text="Redimensionar", command=appResize)
btn_rotate = tk.Button(frame_operations, text="Rotar Imagen", command=appRotate)
btn_aritOP = tk.Button(frame_operations, text="Operaciones Aritméticas", command=appArit)
btn_logOP = tk.Button(frame_operations, text="Operaciones Lógicas", command=appLogic)
btn_interpol = tk.Button(frame_operations, text="Interpolación", command=appInterpolation)

# Agregar botones de operaciones al `frame_operations`
for btn in [btn_gray, btn_bw, btn_resize, btn_rotate, btn_aritOP, btn_logOP, btn_interpol]:
    btn.pack(pady=5)

# Botones de filtros
btn_blur = tk.Button(frame_filters, text="Difuminar", command=appBlur)
btn_gaussBlur = tk.Button(frame_filters, text="Desenfoque Gaussiano", command=appGaussBlur)
btn_sharpen = tk.Button(frame_filters, text="Nitidez", command=appSharpen)
btn_canny = tk.Button(frame_filters, text="Canny", command=appCanny)
btn_emboss = tk.Button(frame_filters, text="Relieve", command=appEmboss)
btn_dilate = tk.Button(frame_filters, text="Dilatación", command=appDilate)

# Agregar botones de filtros al `frame_filters`
for btn in [btn_blur, btn_gaussBlur, btn_sharpen, btn_canny, btn_emboss, btn_dilate]:
    btn.pack(pady=5)

# Botones Morfologicos
btn_open = tk.Button(frame_morph, text="Apertura", command=appOpening)
btn_close = tk.Button(frame_morph, text="Cierre", command=appClosing)
btn_gradient = tk.Button(frame_morph, text="Deteccion de bordes", command=appGradient)

# Agregar botones de filtros al `frame_filters`
for btn in [btn_open,btn_close,btn_gradient]:
    btn.pack(pady=5)

# Botones Segmentacion
btn_threshold = tk.Button(frame_segment, text="umbralizacion", command=appThreshold)
btn_segCanny = tk.Button(frame_segment, text="Segmentacion Canny", command=appSegCanny)
btn_contour = tk.Button(frame_segment, text="Contornos", command=appContour)
btn_kmeans = tk.Button(frame_segment, text="k-means", command=appKmeans)
btn_watershed = tk.Button(frame_segment, text="watershed", command=appWatershed)

# Agregar botones de filtros al `frame_filters`
for btn in [btn_threshold,btn_segCanny,btn_contour,btn_kmeans,btn_watershed]:
    btn.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()