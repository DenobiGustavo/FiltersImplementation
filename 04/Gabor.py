from PIL import Image
import math

def gerar_kernel_gabor(tamanho, lambda_, theta, sigma, gamma, phi):
    """Gera um kernel de Gabor com os parâmetros especificados"""
    meio = tamanho // 2
    kernel = []

    for y in range(-meio, meio + 1):
        linha = []
        for x in range(-meio, meio + 1):
            x_theta = x * math.cos(theta) + y * math.sin(theta)
            y_theta = -x * math.sin(theta) + y * math.cos(theta)

            exp = math.exp(-(x_theta**2 + (gamma**2) * y_theta**2) / (2 * sigma**2))
            cos = math.cos(2 * math.pi * x_theta / lambda_ + phi)

            valor = exp * cos
            linha.append(valor)
        kernel.append(linha)
    return kernel

def aplicar_kernel(imagem, kernel):
    largura, altura = imagem.size
    pixels = imagem.load()
    nova = Image.new('L', (largura, altura))
    novos = nova.load()

    meio = len(kernel) // 2

    for y in range(meio, altura - meio):
        for x in range(meio, largura - meio):
            soma = 0
            for j in range(len(kernel)):
                for i in range(len(kernel[0])):
                    xi = x + i - meio
                    yj = y + j - meio
                    soma += pixels[xi, yj] * kernel[j][i]
            valor = int(min(max(soma, 0), 255))  # clamp
            novos[x, y] = valor

    return nova

# Parâmetros do filtro Gabor
tamanho_kernel = 11
lambda_ = 8.0
theta = math.pi / 4  # 45 graus
sigma = 4.0
gamma = 0.5
phi = 0

# 📸 Abrir imagem em tons de cinza
imagem = Image.open("./04/miranha.jpg").convert('L')

# 🔧 Gerar kernel e aplicar
kernel_gabor = gerar_kernel_gabor(tamanho_kernel, lambda_, theta, sigma, gamma, phi)
imagem_gabor = aplicar_kernel(imagem, kernel_gabor)

# 🖼️ Exibir e salvar
imagem_gabor.show()

