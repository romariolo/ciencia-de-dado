import array as arr

#Criando array de inteiros
meu_array = arr.array('i',[1,2,3,4])

#Acessando elemento
print(meu_array[0])

#Adicionando elementos
meu_array.append(6)
print(meu_array)

#Removendo último elemento
meu_array.pop()
print(meu_array)

#Alterando um valor
meu_array[0]  = 10

meu_array[2] = 2025

#Inserindo elemento na posição 3
meu_array.insert(2,7)
print(meu_array)

#RTemovendo o primeiro 7 encontrado no array
meu_array.remove(7)
print(meu_array) # type: ignore