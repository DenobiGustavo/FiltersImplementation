# 🌊 Efeito Warping com Onda Vertical (Pillow - Python)

Este efeito de **warping com onda vertical** distorce a imagem aplicando uma transformação no deslocamento horizontal de seus pixels, baseado em uma função seno. Ele simula uma ondulação horizontal onde os pixels se movem para a esquerda ou para a direita dependendo da posição na altura da imagem.

---

## 🧠 Como funciona

1. Abre a imagem e converte para o modo `'RGB'` (cores).
2. Cria uma nova imagem em branco com o mesmo tamanho.
3. Percorre cada pixel da imagem original (linha por linha).
4. Para cada linha (`y`), calcula um **deslocamento horizontal (`x`)** com base em uma função **senoidal**, usando os parâmetros `amplitude` e `frequencia`.
5. Aplica esse deslocamento ao pixel na horizontal, se ele estiver dentro da imagem.
6. Copia o pixel deslocado para a nova imagem; se sair dos limites, preenche com preto `(0, 0, 0)`.
7. Exibe a nova imagem com o efeito de **ondulação vertical**.


---

## Implementação com Pillow

Este repositório contém uma implementação simples do algoritmo de erosão morfológica usando a biblioteca [Pillow](https://python-pillow.org/). A abordagem é baseada em operações básicas de manipulação de pixels, sem dependências adicionais como OpenCV ou NumPy.

---

## Uso

### Pré-requisitos

- Python 3.x
- Biblioteca Pillow (instale com `pip install pillow`)