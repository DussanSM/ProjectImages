import matplotlib.pyplot as plt

def show_img(imagen, titulo):
    
    plt.figure(figsize=(6, 6))
    plt.imshow(imagen, cmap="gray" if len(imagen.shape) == 2 else None)
    plt.axis("off")
    plt.title(titulo)
    plt.show()