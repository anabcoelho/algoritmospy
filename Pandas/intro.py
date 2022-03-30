# Biblioteca para recursos matemáticos
import numpy as np

# Biblioteca para plotagem de dados
import matplotlib.pyplot as plt

# Biblioteca para modelagem de dados
import pandas as pd

# Lista com os rotulos
Labels = ['1º', '2º', '3º']

# Lista com os valores
Valores = [10, 20, 30]

# Criando a base de dados com as listas
Serie = pd.Series( data=Valores, index=Labels )
Serie

Serie['1º']

Serie * 2

Serie_Nova = pd.Series( data=[50,100,150], index=Labels )

Serie + Serie_Nova

# Criando um dicionário
Dicionario = {
    'A' : [1, 2, 3],
    'B' : [-3, -2, -1],
    'C' : [0, 10, 20] }

# Criando uma lista com os labels
Label = ['1º Linha', '2º Linha', '3º Linha']

DataFrame_01 = pd.DataFrame( Dicionario, index=Label )
DataFrame_01

DataFrame_01['A']

DataFrame_01[['A', 'B']]

DataFrame_01['Nova_Coluna'] = DataFrame_01['A'] * DataFrame_01['B']
DataFrame_01

DataFrame_01.drop('Nova_Coluna', axis=1, inplace=True)
DataFrame_01

DataFrame_01.loc['1º Linha']

DataFrame_01.loc[['1º Linha','3º Linha' ], ['A', 'C']]

DataFrame_01.iloc[0:3, 1:]

DataFrame_01 > 0

DataFrame_01[ DataFrame_01['A'] > 0 ]['C']

Filtro = DataFrame_01['C'] > 0
DataFrame_02 = DataFrame_01[Filtro]
DataFrame_02['A']

DataFrame_01[
  ( DataFrame_01['A'] > 1 ) & ( DataFrame_01['C'] > 0 )
]

DataFrame_01.reset_index()

DataFrame_01

# Criando varios dicionarios
Dicionario_01 = {'A' : [1, 2, 3],
                 'B' : [-32, -21, -15],
                 'C' : [60, 10, 20],
                 'Chave' : ['AA', 'BB', 'CC'] }

Dicionario_02 = {'A' : [6, 7, 8],
                 'B' : [-39, -28, -17],
                 'C' : [1000, 10, 60],
                 'Chave' : ['AA', 'BB', 'CC'] }

Dicionario_03 = {'A' : [11, 12, 13],
                 'B' : [-39, -22, -11],
                 'C' : [30, 10, 20],
                 'Chave' : ['AA', 'BB', 'CC'] }

# Criando varias listas para serem os labels
Label_01 = ['1º Linha', '2º Linha', '3º Linha']
Label_02 = ['4º Linha', '5º Linha', '6º Linha']
Label_03 = ['7º Linha', '8º Linha', '9º Linha']

# Estruturando as bases de dados
DataFrame_01 = pd.DataFrame( Dicionario_01, index=Label_01 )
DataFrame_02 = pd.DataFrame( Dicionario_02, index=Label_02 )
DataFrame_03 = pd.DataFrame( Dicionario_03, index=Label_03 )

pd.concat(
  [ DataFrame_01, DataFrame_02, DataFrame_03 ]
)

pd.merge(
  DataFrame_01, DataFrame_02, how='inner', on='Chave'
)

# Criando varios dicionarios
Dicionario_01 = {'A' : [1, 2, 3],
                 'B' : [-32, -21, -15],
                 'C' : [60, 10, 20] }

Dicionario_02 = {'D' : [6, 7, 8],
                 'E' : [-39, -28, -17],
                 'F' : [1000, 10, 60] }

# Criando varias listas para serem os labels
Label_01 = ['1º Linha', '2º Linha', '3º Linha']


# Estruturando as bases de dados
DataFrame_01 = pd.DataFrame( Dicionario_01, index=Label_01 )
DataFrame_02 = pd.DataFrame( Dicionario_02, index=Label_01 )

# Aplicando a função join
DataFrame_01.join(DataFrame_02)





Dados = pd.Series( [1,3,5,np.nan,6,8] )
 Dados



Lista_Datas = pd.date_range('20210101', periods=5)
Lista_Datas

DataFrame_01 = pd.DataFrame( np.random.randn(5,4),
                  index=Lista_Datas,
                  columns=list( ['A','B','C','D']) )
DataFrame_01

Dicionario = {
    'A' : 1,
    'B' : pd.Timestamp('20210102'),
    'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
    'D' : np.array([3] * 4, dtype='int32'),
    'E' : pd.Categorical( ["Email", "Telefone", "Celular", "País"] ),
    'F' : pd.Categorical( ["email@.email.com", "(11)4455-4455", "(11)922332233", "Brasil"] ),
}

DataFrame_02 = pd.DataFrame( Dicionario )
DataFrame_02

DataFrame_02.dtypes

DataFrame_02.head()

DataFrame_02.tail(2)

DataFrame_02.index

DataFrame_02.columns

DataFrame_02.values

DataFrame_02.describe()

DataFrame_01.sort_index(axis=1, ascending=False)

DataFrame_02.sort_values(by='E')

DataFrame_01['A']

DataFrame_01[0:3]

DataFrame_01['20210101':'20210102']

DataFrame_01.loc['20210101']

DataFrame_01.loc[:,['A','B']]

DataFrame_01.iloc[3]

DataFrame_01.iloc[3:5,0:2]

DataFrame_01[ DataFrame_01.A > 0 ]

DataFrame_01[ DataFrame_01 > 0 ]

DataFrame_03 = DataFrame_01.copy()
DataFrame_03

DataFrame_03['Nova_Coluna'] = ['abc', 'def', 'ghi', 'jkl', 'mno']
DataFrame_03

DataFrame_03[ DataFrame_03['Nova_Coluna'].isin(['abc', 'mno']) ]

DataFrame_04 = pd.Series( [1,2,3,4,5,6],
                          index=pd.date_range('20210101', periods=6) )
 DataFrame_04

DataFrame_04.at[ dates[0], 'A'] = 0

Lista = [ c for c in range(1,50000000) ]

# Commented out IPython magic to ensure Python compatibility.
# %time for i in Lista: pass

# Commented out IPython magic to ensure Python compatibility.
# %time
for c in range(1, 50000000):
  pass
# %time

