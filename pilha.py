#Criando uma pilha
#Não usaremos POO
pilha = []

pilha.append(1)
pilha.append(3)
pilha.append(10)
pilha.append(8)

#Imprimindo pilha após inserções
print(f'pilha após inserção de valores: {pilha}')

#Removendo o elemento do topo da pilha 
topo = pilha.pop()
print(pilha)
print(topo)

#Acessando o topo da pilha sem remover(top/peek)
print(f'Element no topo da pilha: {pilha[-1]}')

#Verificando se a lista está vazia
if not pilha:
    print("Pilha vazia")
else:
    print("Pilha não está vazia")
    print(f'A quantidade de elementos na pilha é: {len(pilha)}')

