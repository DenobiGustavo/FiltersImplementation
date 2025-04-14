# 🧼 Filtro da Mediana em Python com PIL

O **filtro da mediana** é uma técnica bastante eficaz para remover ruídos em imagens, especialmente o famoso **ruído sal e pimenta**. Diferente de filtros que usam médias, ele substitui cada pixel pela **mediana** dos valores da vizinhança, preservando melhor as bordas da imagem.

Este exemplo utiliza a biblioteca **PIL (Pillow)** para aplicar o filtro em tons de cinza.

---

## 🧠 Como funciona

1. Converte a imagem para escala de cinza (modo `'L'`).
2. Percorre cada pixel da imagem, ignorando as bordas.
3. Coleta os valores de uma **janela 3x3** em torno do pixel atual.
4. Ordena esses valores e seleciona o valor da **mediana**.
5. Substitui o pixel original pela mediana calculada.
6. Exibe a nova imagem com o ruído suavizado.

---

## Implementação com Pillow

Este repositório contém uma implementação simples do algoritmo de erosão morfológica usando a biblioteca [Pillow](https://python-pillow.org/). A abordagem é baseada em operações básicas de manipulação de pixels, sem dependências adicionais como OpenCV ou NumPy.

---

## Uso

### Pré-requisitos

- Python 3.x
- Biblioteca Pillow (instale com `pip install pillow`)