import pandas as pd

#Criando um objeto no pandas
data = pd.Series([0.25,0.50,0.75,1])
print(data)

#Saber os valores do array
print(data.values)

#Saber dos índices
print(data.index)

#Acessando pelos índices
print(data[1])
print(data[1:3])#até 3 -1 (no caso até 2)

#Criando uma nova forma de indexação
data2=pd.Series([0.25,0.50,0.75,1],
                index=['a', 'b', 'c', 'd'])
                
print(data2)
print("-----------")
print(data2['b'])


#Outra

data3=pd.Series([0.25,0.50,0.75,1],
                index=[2,5,3,7])

print(data3)
print("-----------")
print(data3[3])


#Dicionário
populaca_dicionario = { 'São Paulo': 248222.8,  
    'Minas Gerais': 586528.3, 
    'Rio de Janeiro': 43677.6,  
    'Bahia': 564733.2,  
    'Paraná': 199314.9  
}

populacao = pd.Series(populaca_dicionario)
print(populacao)
print("-------")
print(populacao['São Paulo'])
print(populacao['Rio de Janeiro': 'Paraná'])


#outras formas de definir 
print(pd.Series([2,4,6]))#Indice gerado normalmente
print(pd.Series(5, index=[100,200,300]))#Valor 5 para cada indice
print(pd.Series({2: 'a', 3:'b', 5:'c'}))#Dicinario
print(pd.Series({2: 'a', 3:'b', 5:'c'},  index=[2,3]))#Dicinario com apenas indices 2,3


#-----------------------------------------------------------------------------------------

#Dataframe

arae_dict = estados = {
    'São Paulo': 248222.8,  
    'Minas Gerais': 586528.3, 
    'Rio de Janeiro': 43677.6,  
    'Bahia': 564733.2,  
    'Paraná': 199314.9  
}

area4 = pd.Series(arae_dict)
print(area4)

#Construindo um Dataframe
estados = pd.DataFrame({'população': populacao,
                        'area': area4})


print(estados)

print(estados.index)
print(estados.columns)
print(estados['area'])#Pegando somente area
print(estados['população'])#Somente população


print(pd.DataFrame(populacao,columns=['população']))

#montando um dataframe
data5 = [{'a': i, 'b': 2 * i}
            for i in range(3)]

pd.DataFrame(data5)

print(data5)

#Index como conjunto ordenado
indA = pd.Index([1,3,5,7,9])
indB = pd.Index([2,3,5,7,11])

print(indA.intersection(indB))#Interseção
print(indA.union(indB))#União
print(indA.symmetric_difference(indB))#Diferença simétrica A.B ou B.A

area6 = pd.Series({ 'São Paulo': 248222.8,  
    'Minas Gerais': 586528.3, 
    'Rio de Janeiro': 43677.6,  
    'Bahia': 564733.2,  
    'Paraná': 199314.9  })

pop = pd.Series({'São Paulo': 12345678,
 'Minas Gerais': 21234567,
  'Rio de Janeiro': 6748392,
   'Bahia': 14873064,
 'Paraná': 11516840})

data = pd.DataFrame({'area': area6, 'população': pop})
print(data)

print(data['area'])

#Inserir nova colun
data['densidade'] = data['população'] / data['area']
print(data )

print(data.values)
print(data.T)#Transposta

#-------------------------------------------

#Filtragmem de dados

#Exemplo de Dataframe
data7 = {'nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
        'idade': [17, 21, 25, 36]}

df = pd.DataFrame(data7)
print(df)

df_maior_18 = df[df['idade'] > 18]

print(df_maior_18)

#Condições multiplas

df_filtrado = df[(df['idade'] > 18) & (df['nome'].str.startswith('B'))]
print(df_filtrado)

#Onde  nome é Ana ou Diana
df_filtrado_nomes = df[df['nome'].isin(['Ana', 'Diana'])]
print(df_filtrado_nomes)


#Adicionando valors nulos para exemplo
df.loc[1, 'idade'] = None

#filtrar linhas onde valores são nulos em 'idade'
df_filtro_com_nulos = df[df['idade'].isnull()]
print(df_filtro_com_nulos)

#Faixa de idade
df_faixa_idade = df[df['idade'].between(18, 25)]
print(df_faixa_idade)

#Filtrar com expressões complexas
df_expressao = df[(df['nome'].str.len() > 4) & (df['idade'] > 20)]
print(df_expressao)

import pandas as pd
import numpy as np

data8 = pd.Series([1, np.nan, 'hello', None])
print(data8.isnull())  # Verificar nulos
print("-----------------")
print(data8[data8.notnull()])  # Filtrar o que não é nulo

#Para remover valores nulos
print(data8.dropna())

#Considere o seguinte Dataframe
df1 = pd.DataFrame([[1, np.nan, 2],
                   [2,3,5],
                   [np.nan, 4, 6]])

print(df)

#df.dropna()

#Controlando o drpnan
df1.dropna(axis='columns')#Retorna as colunas que não tem nenhum nan
print(df1)

#Leitura de um arquivo

df_csv = pd.read_csv('datasets/sample_data.csv')
print(df_csv)

print("--------------")

#Leitura de arquivo excel
df_excel = pd.read_excel('datasets/sampe_data.xlsx')
print(df_excel)


#Escrita em arquivo
df = pd.read_csv('datasets/sample_data.csv')  # Para CSV
# df = pd.read_excel('caminho_do_arquivo.xlsx')  # Para Excel

# Apresentar dataframe do arquivo
print("DataFrame do arquivo:")
print(df)

# Selecionar os dados onde a idade é maior que 25
filtered_df = df[df['Age'] > 25]
print("\nDataFrame Filtrado (idade > 25):")
print(filtered_df)

# Modificar o DataFrame, por exemplo, adicionar 1 para a coluna age (idade)
df['Age'] = df['Age'] + 1
print("\nDataFrame com Idades Modificadas:")
print(df)

# Salvar o DataFrame modificado em um novo arquivo
df.to_csv('datasets/nova_data_modificado.csv', index=False)
# df.to_excel('nova_arquivo_modificado.xlsx', index=False)