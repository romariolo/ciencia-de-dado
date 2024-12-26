#Criando uma lista
minha_lista_vazia = []

minha_lista = [1, 2, 'python', 3.5]

#Acessando elementos
print(minha_lista[-1])

#Adicionando um novo elemento
minha_lista.append(6)
print(minha_lista)

#Removendo um elemento
minha_lista.remove('python')
print(minha_lista)

#Ordenando uma lista de números
numeros = [10, 5, 6,1, 100]
numeros.sort()
print(numeros)

#Revertendo a ordem da lista
numeros.reverse()
print(numeros)

#Inserindo número 10 no índice 0, na primeira posição
numeros.insert(0,10)
print(numeros)

elem = numeros.pop()
print(numeros)
#Imprimindo o último elemento que foi excluindo
print(elem)

