#Numpy para cálculos de alto desempenho
import numpy as np 
#Pandas para análise de dados(especialmente quano há tabelas)
import pandas as pd

np.__version__#Versão da biblioteca

#ineragir com arrays

np.array([1,4,2,5,3])

print(np.array([3.14, 5,7,8]))#Upcast para tudo float

#np.array([1,2,3,4],  type ='float32')#Casting explícito

# Criando arrays unidimensionais e multidimensionais
array_1d = np.array([1, 2, 3, 4])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

print("Array 1D:", array_1d)
print("Array 2D:", array_2d)
print("Array 3D:", array_3d)


#listas aninhadas resultam em arrays multidimensionais

print(np.array([range(i, i + 3) for i in [2, 4, 6]]))