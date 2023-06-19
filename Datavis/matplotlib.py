# -*- coding: utf-8 -*-
"""Matplotlib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ZA0ZMvFZ8v-CXwBMJeOAttBAkypKRtz
"""

# Biblioteca para modelagem de dados
import pandas as pd

# Biblioteca para recursos matemáticos
import numpy as np

# Biblioteca para recursos Graficos
import matplotlib.pyplot as plt

# Gerando numeros com o numpy
Dados_x = np.linspace(0, 10, 200)
Dados_y = Dados_x * Dados_x

# ---- Gráfico Linha com 2 eixos e ajustando os parâmetros

# Ajustando a figura
plt.figure(
    figsize=(10, 5),  # Ajustando o tamanho do gráfico
    facecolor='gray'  # Ajustando cor de fundo
)

# Adicionando eixos
Ax = plt.axes()
Ax.set_facecolor('white')  # Definindo cor de fundo no gráfico

# Criando o gráfico e passando parâmetros para ajustes
plt.plot(
    Dados_x, Dados_y,  # Dados do gráficos
    color='magenta',  # Cor da linha
    linewidth=2,  # Espessura da linha
    markersize=5,  # Tamanho do marcador
    marker='o',  # Tipo do marcados
    linestyle='dashed',  # Tipo da linha
    markeredgecolor='black',  # Cor linha do marcador
)

# Definindo label do eixo x
plt.xlabel(
    'Eixo x',  # nome do label
    fontweight='bold',  # estilo
    fontsize='large',  # Tamanho da fonte
    fontfamily='fantasy',  # Tipo da fonte
    color='blue',  # Cor da Fonte
)

# Definindo label do eixo y
# Mesmo parâmetros pode ser aplicado do 'xlabel'
plt.ylabel('Eixo y')

# Definindo um titulo
plt.title(
    'Gráfico Simples',  # Título do Gráfico
    fontweight='bold',  # Estilo da fonte
    fontsize='xx-large',  # Tamanho da fonte
    fontfamily='fantasy',  # Tipo da fonte
    color='blue',  # Cor da Fonte
)

# Definindo as legendas
plt.legend(
    'Números Aleatórios',  # Nome da legenda
    loc='upper center',  # Posição da legenda
    bbox_to_anchor=(1, 0., 0.0, 0.2),  # Posição legenda na Figura
    fontsize='large',  # Tamanho do texto
    shadow=True,  # Sombra na legenda
    borderpad=1,  # Bordar da legenda
);

# Plotando varios graficos em uma grade

# Definindo a dimensão da Grade
Linhas = 2
Colunas = 2

# Grafico na 1º posição da Grade
plt.subplot(Linhas, Colunas, 1)
plt.plot(Dados_x, 'r--')
plt.title('Grafico 1')

# Grafico 2º posição da Grade
plt.subplot(Linhas, Colunas, 2)
plt.plot(Dados_y, 'g-')
plt.title('Grafico 2')

# Grafico 3º posição da Grade
plt.subplot(Linhas, Colunas, 3)
plt.plot(Dados_y, 'y-')
plt.title('Grafico 3')

# Grafico 4º posição da Grade - Incluindo 2 eixos
plt.subplot(Linhas, Colunas, 4)
plt.plot(Dados_x, 'b--')
plt.plot(Dados_y, 'p--')
plt.title('Grafico 4');

# Grafico com mini grafico acoplado

# Criando uma nova firua
Figura = plt.figure()

# Definindo o tamanho do grafico
Eixo_1 = Figura.add_axes([0.1, 0.1, 0.8, 0.8])

# Definindo o tamanho do grafico
Eixo_2 = Figura.add_axes([0.2, 0.5, 0.3, 0.3])

# Plotando os graficos
Eixo_1.plot(Dados_x, Dados_y, 'r--')
Eixo_2.plot(Dados_y, Dados_x, 'y');

# Grafico de Barras

# Criando a figura
Figura = plt.figure()

# Definindo o Tamanho
Grafico = Figura.add_axes([0, 0, 0.7, 0.7])

# Definindo os rotulos
Rotulos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Gerando o gráfico
Grafico.bar(Rotulos, Dados_x);

# Grafico de Barras com mais eixos

# Criando a figura
Figura = plt.figure()

# Definindo o Tamanho
Grafico = Figura.add_axes([0, 0, 0.7, 0.7])

# Definindo os rotulos
Rotulos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Gerando o gráfico
Grafico.bar(Rotulos, Dados_x, color='r')
Grafico.bar(Rotulos, Dados_y * 0.1, color='b');

# Grafico Boxplot
plt.boxplot(Dados_y);


