from PIL import Image

def aplicar_filtro_sobel(imagem):
    imagem_gray = imagem.convert('L')
    largura, altura = imagem_gray.size
    pixels = imagem_gray.load()

    nova_imagem = Image.new('L', (largura, altura))
    novos_pixels = nova_imagem.load()

    # Máscaras de Sobel
    sobel_x = [[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]]

    sobel_y = [[-1, -2, -1],
               [ 0,  0,  0],
               [ 1,  2,  1]]

    for y in range(1, altura - 1):
        for x in range(1, largura - 1):
            gx = 0
            gy = 0

            # Aplica as máscaras
            for j in range(-1, 2):
                for i in range(-1, 2):
                    pixel = pixels[x + i, y + j]
                    gx += pixel * sobel_x[j + 1][i + 1]
                    gy += pixel * sobel_y[j + 1][i + 1]

            # Magnitude da borda (valor entre 0 e 255)
            g = min(abs(gx) + abs(gy), 255)
            novos_pixels[x, y] = g

    return nova_imagem

# 🖼️ Abrir imagem e aplicar Sobel
imagem = Image.open("./03/miranha.jpg")
imagem_sobel = aplicar_filtro_sobel(imagem)
imagem_sobel.show()

