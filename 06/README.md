# Algoritmo de Erosão Morfológica com Pillow

## O que é Erosão Morfológica?

A erosão morfológica é uma operação em processamento de imagens utilizada para reduzir ruídos, destacar formas ou diminuir o tamanho de objetos em uma imagem. Essa técnica é amplamente usada em análises de imagens binárias, mas também pode ser aplicada a imagens em escala de cinza.

### Como Funciona?

A erosão funciona analisando uma região ao redor de cada pixel, definida por um elemento estruturante (ou kernel). Para cada pixel da imagem:
1. Verifica-se todos os pixels vizinhos dentro da área definida pelo kernel.
2. O valor do pixel central é substituído pelo menor valor encontrado nessa região.

Essa operação resulta em um "encolhimento" dos objetos presentes na imagem, suavizando bordas e removendo pequenos detalhes ou ruídos.

---

## Implementação com Pillow

Este repositório contém uma implementação simples do algoritmo de erosão morfológica usando a biblioteca [Pillow](https://python-pillow.org/). A abordagem é baseada em operações básicas de manipulação de pixels, sem dependências adicionais como OpenCV ou NumPy.

---

## Uso

### Pré-requisitos

- Python 3.x
- Biblioteca Pillow (instale com `pip install pillow`)



