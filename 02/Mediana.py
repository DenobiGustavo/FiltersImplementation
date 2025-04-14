from PIL import Image

def aplicar_filtro_mediana(imagem):
    imagem_gray = imagem.convert('L')
    largura, altura = imagem_gray.size
    pixels = imagem_gray.load()

    nova_imagem = Image.new('L', (largura, altura))
    novos_pixels = nova_imagem.load()

    for y in range(1, altura - 1):
        for x in range(1, largura - 1):
            vizinhanca = []

            # Captura a vizinhança 3x3
            for j in range(-1, 2):
                for i in range(-1, 2):
                    vizinhanca.append(pixels[x + i, y + j])

            # Ordena e pega a mediana
            vizinhanca.sort()
            mediana = vizinhanca[len(vizinhanca) // 2]

            # Define o novo pixel
            novos_pixels[x, y] = mediana

    return nova_imagem

# 🖼️ Abrir imagem e aplicar filtro
imagem = Image.open("./02/miranhapintado.jpg")
imagem_filtrada = aplicar_filtro_mediana(imagem)
imagem_filtrada.show()

