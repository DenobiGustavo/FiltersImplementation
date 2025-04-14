# 📊 Equalização de Histograma

A **equalização de histograma** é uma técnica de processamento de imagens usada para melhorar o contraste de uma imagem, especialmente quando os níveis de intensidade estão concentrados em uma faixa estreita. A ideia central é redistribuir os valores dos pixels de modo que o histograma da imagem resultante seja aproximadamente uniforme.

---

## 🧠 Conceito

Imagens com pouco contraste têm seus valores de intensidade agrupados em torno de determinados valores. A equalização transforma esses valores, espalhando-os de forma mais uniforme, o que pode revelar detalhes ocultos.

---

## 🔢 Etapas do Algoritmo

1. **Calcular o histograma da imagem**  
   Conta quantos pixels existem para cada nível de intensidade (0 a 255 para imagens em tons de cinza).

2. **Calcular a função de distribuição acumulada (CDF)**  
   Soma cumulativa do histograma normalizado (probabilidades).  

   \[
   CDF(i) = \sum_{j=0}^{i} \frac{histograma(j)}{n_{pixels}}
   \]

3. **Normalizar a CDF**  
   Multiplica-se a CDF por 255 (valor máximo de intensidade). Isso gera uma **tabela de mapeamento** para os novos valores de intensidade.

4. **Aplicar o mapeamento**  
   Cada pixel da imagem original é substituído pelo novo valor obtido a partir da CDF.

---

## Implementação com Pillow

Este repositório contém uma implementação simples do algoritmo de erosão morfológica usando a biblioteca [Pillow](https://python-pillow.org/). A abordagem é baseada em operações básicas de manipulação de pixels, sem dependências adicionais como OpenCV ou NumPy.

---

## Uso

### Pré-requisitos

- Python 3.x
- Biblioteca Pillow (instale com `pip install pillow`)
