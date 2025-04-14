from PIL import Image

#PARA IMAGENS EM TONS DE CINZA
#MELHORA O BRILHO E O CONTRASTE

def equalizar_histograma(imagem):
    # Passo 1: Converter para tons de cinza
    imagem_gray = imagem.convert('L')
    pixels = list(imagem_gray.getdata())
    total_pixels = len(pixels)

    # Passo 2: Calcular o histograma
    histograma = [0] * 256
    for pixel in pixels:
        histograma[pixel] += 1

    # Passo 3: Calcular a CDF
    cdf = []
    soma = 0
    for valor in histograma:
        soma += valor
        cdf.append(soma)

    # Passo 4: Normalizar a CDF
    cdf_min = next(c for c in cdf if c > 0)
    cdf_normalizado = [
        round((c - cdf_min) / (total_pixels - cdf_min) * 255) for c in cdf
    ]

    # Passo 5: Mapear os valores
    pixels_equalizados = [cdf_normalizado[p] for p in pixels]

    # Criar nova imagem com os pixels equalizados
    imagem_equalizada = Image.new('L', imagem_gray.size)
    imagem_equalizada.putdata(pixels_equalizados)
    return imagem_equalizada

# 🖼️ Abrir imagem e aplicar equalização
imagem = Image.open("./01/miranha.jpg")
imagem_eq = equalizar_histograma(imagem)
imagem_eq.show()

