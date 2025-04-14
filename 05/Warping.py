from PIL import Image
import math

def warping_onda_vertical(imagem, amplitude=30, frequencia=0.05):
    largura, altura = imagem.size
    nova_imagem = Image.new('RGB', (largura, altura))
    pixels_original = imagem.load()
    pixels_novos = nova_imagem.load()

    for y in range(altura):
        for x in range(largura):
            # Aplica deslocamento em X com base no Y
            deslocamento = int(amplitude * math.sin(2 * math.pi * frequencia * y))
            novo_x = x + deslocamento

            # Se estiver dentro dos limites, copia o pixel
            if 0 <= novo_x < largura:
                pixels_novos[x, y] = pixels_original[novo_x, y]
            else:
                pixels_novos[x, y] = (0, 0, 0)  # preto fora dos limites

    return nova_imagem

# 🖼️ Abrir imagem e aplicar warping
imagem = Image.open("./05/miranha.jpg").convert('RGB')
imagem_warp = warping_onda_vertical(imagem)
imagem_warp.show()

