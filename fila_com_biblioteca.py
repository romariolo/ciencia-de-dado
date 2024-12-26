from collections import deque

#Criando uma fila
fila = deque()

#Operação com deque
fila.append(10)
fila.append(20)
fila.append(30)

print(f'Fila apóes inserções: {fila}')

#Operação com primeiro da fila
primeiro = fila.popleft()
print(f'Fila após remover o primeiro: {fila}')
print(f'Elemento retirado da fila: {primeiro}')

#Acessando o primeiro elemento da fila
print(f'Primeiro elemento da fila: {fila[0]}')

#Verificando se a fila está vazia
if not fila:
    print("A fila está vazia")
else:
    print(f'Fila não está vazia: {fila}')
    print(f'A fila tem {len(fila)} ítens')

