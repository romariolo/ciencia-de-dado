#importando as bibliotecas necessárias
import pandas as pd

from sklearn.datasets import load_iris

#carregar o dataset iris
iris = load_iris()

#criar um dataframe com as características (features)
dados = pd.DataFrame(iris.data, columns=iris.feature_names)


#adicionar a coluna alvo(target), que contém a classe das flores
dados['especies'] = iris.target

#Exibir as primeiras linhas do Dataframe
dados.head()


#-----------------------------------------------------------------------------

#Limpeza e Preparação dos Dados


#Verificar se há dados ausentes
print(dados.isnull().sum())

#Verificar a distribuição das classes (espécies de flores)
print(dados['especies'].value_counts())


#------------------------------------------------------------------------------

#Análise Exploratória dos Dados

import seaborn as sns
import matplotlib.pyplot as plt


#contagem das flores por espécie
sns.countplot(x='especies', data=dados, palette=["#1f77b4", "#ff7f0e", "#2ca02c"])
plt.title("Distribuição das espécies de flores")
plt.xlabel("Espécied flor (0 = Setosa, 1 = Versicolar, 2 = Virginica)")
plt.ylabel("Quantidade")
plt.show()

#-----------------------------------------------------------------------------------

#Boxplt para comparar o tamanho das pétalas entre as espécies
sns.boxplot(x='especies', y='petal length (cm)', data=dados, palette="Set2")
plt.title("Comprimento da pétala por espécies")
plt.xlabel('Espécie de flor (0 = setosa, 1 = versicolor, 2 = virginica)')
plt.show()

print(dados.describe())