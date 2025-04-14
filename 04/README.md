# 🧠 Filtro de Gabor em Python com PIL

O **Filtro de Gabor** é uma ferramenta poderosa para **análise de texturas**, **detecção de bordas em múltiplas orientações** e **extração de características** em imagens. É bastante usado em aplicações como reconhecimento facial, análise de impressões digitais e visão computacional em geral.

---

## 🔍 Como funciona

O filtro de Gabor é uma **função senoidal modulada por uma Gaussiana**. Ele age como uma lupa orientada e sensível à frequência, sendo ótimo para detectar **padrões específicos em certas direções e escalas**.

O kernel de Gabor possui parâmetros que controlam sua orientação, frequência e forma:

- `λ` (lambda): comprimento de onda da senóide.
- `θ` (theta): orientação da borda (em radianos).
- `σ` (sigma): largura do envelope gaussiano.
- `γ` (gamma): razão de aspecto (controle de elongação).
- `φ` (phi): fase da senóide.
- `tamanho`: tamanho do kernel.
---

## Implementação com Pillow

Este repositório contém uma implementação simples do algoritmo de erosão morfológica usando a biblioteca [Pillow](https://python-pillow.org/). A abordagem é baseada em operações básicas de manipulação de pixels, sem dependências adicionais como OpenCV ou NumPy.

---

## Uso

### Pré-requisitos

- Python 3.x
- Biblioteca Pillow (instale com `pip install pillow`)