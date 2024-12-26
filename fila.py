#Criando uma fila
#Não usaremos POO
fila = []

fila.append(1)
fila.append(3)
fila.append(10)
fila.append(8)

#Imprimindo fila após inserções
print(f'pilha após inserção de valores: {fila}')

#Operação Dequeue(remove o primeiro elemento da fila)
primeiro = fila.pop(0)
print(fila)
print(primeiro)

#Acessando o primeiro elemento da fila(front)
print(f'O primeiro elemento da fila: {fila}')

#Verificando se a fila está vazia 
if not fila:
    print("A fila está vazia")
else:
    print(f'A fila não está vazia: {fila}')
    print(f'O tamanho da fila é de: {len(fila)}')

    