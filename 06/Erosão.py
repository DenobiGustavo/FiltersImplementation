from PIL import Image

def erode(image, kernel_size=3):
    """
    Aplica a erosão a uma imagem usando o Pillow.
    
    :param image: Objeto Image da PIL, em escala de cinza.
    :param kernel_size: Tamanho do elemento estruturante (deve ser ímpar).
    :return: Nova imagem erodida.
    """
    # Converter imagem para escala de cinza
    image = image.convert("L")
    width, height = image.size
    pixels = image.load()
    
    # Criação da nova imagem
    new_image = Image.new("L", (width, height))
    new_pixels = new_image.load()
    
    # Definir o deslocamento baseado no kernel
    offset = kernel_size // 2
    
    for y in range(offset, height - offset):
        for x in range(offset, width - offset):
            # Inicializar o menor valor como o máximo possível (255 para grayscale)
            min_value = 255
            
            # Iterar pelo kernel
            for ky in range(-offset, offset + 1):
                for kx in range(-offset, offset + 1):
                    pixel_value = pixels[x + kx, y + ky]
                    min_value = min(min_value, pixel_value)
            
            # Atribuir o menor valor ao pixel central
            new_pixels[x, y] = min_value
    
    return new_image

# Exemplo de uso
if __name__ == "__main__":
    # Abrir a imagem
    input_image = Image.open("imagem_binaria.png")
    
    # Aplicar a erosão
    eroded_image = erode(input_image, kernel_size=3)
    
    # Salvar o resultado
    eroded_image.show()
