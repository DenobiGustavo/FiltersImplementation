# 🧭 Filtro de Sobel em Python com PIL

O **Filtro de Sobel** é uma técnica de detecção de bordas muito usada em processamento de imagens. Ele calcula a **mudança de intensidade dos pixels** para destacar bordas horizontais e verticais. Esse filtro é útil em sistemas de visão computacional e reconhecimento de padrões.

---

## 🔍 Como funciona

O filtro utiliza duas **máscaras convolucionais** (kernels), uma para detectar mudanças no eixo **x** (horizontal) e outra no eixo **y** (vertical):


1. A imagem é convertida para tons de cinza.
2. Cada pixel (exceto os da borda) é avaliado dentro de uma janela 3x3.
3. As máscaras são aplicadas separadamente nos eixos X e Y.
4. A **magnitude do gradiente** é calculada com `|gx| + |gy|`.
5. O resultado é limitado a 255 (intervalo do pixel em tons de cinza).
6. A nova imagem é exibida com as bordas destacadas.

---

## Implementação com Pillow

Este repositório contém uma implementação simples do algoritmo de erosão morfológica usando a biblioteca [Pillow](https://python-pillow.org/). A abordagem é baseada em operações básicas de manipulação de pixels, sem dependências adicionais como OpenCV ou NumPy.

---

## Uso

### Pré-requisitos

- Python 3.x
- Biblioteca Pillow (instale com `pip install pillow`)