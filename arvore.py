#Estrutura básica de uma árvore
#[Valor, filho a esquerda, filho a direita]

arvore = [50,
          [30,[20, None, None], [40, None, None]],
          [70,[60, None, None], [80, None, None]]]

def inserir(valor, arvore):
    if arvore is None:
        return [valor, None, None]
    if valor < arvore[0]:
        arvore[1] = inserir(valor, arvore[1]) #Inserir à esquerda

    else:
        arvore[2] = inserir(valor, arvore[2]) #Inserir à direita
    return arvore


def em_ordem(arvore):
    if arvore is not None:
        em_ordem(arvore[1]) #Percorre a sub arvore da esquerda
        print(arvore[0]) #Visita a raíz
        em_ordem(arvore[2]) #Percorre a sub arvore a direita
    

#Criando uma arvore vazia
arvore = None

#Inserindo valores na árvore
arvore = inserir(50, arvore)
arvore = inserir(30, arvore)
arvore = inserir(70, arvore)
arvore = inserir(20, arvore)
arvore = inserir(40, arvore)
arvore = inserir(60, arvore)
arvore = inserir(80, arvore)

#Percorrendo a árvore em ordem
print("Percorrendo em ordem.")
em_ordem(arvore)

# 4.3 Função para Calcular a Altura da Árvore
def altura(arvore):
    if arvore is None:
        return -1
    else:
        altura_esquerda = altura(arvore[1])
        altura_direita = altura(arvore[2])
        return 1 + max(altura_esquerda, altura_direita)

print("Altura da árvore:", altura(arvore))

# 4.4 Função para Buscar elemento na Árvore
def buscar(arvore, valor):
    # Caso base: árvore vazia ou encontramos o valor
    if arvore is None:
        return "Valor não encontrado."
    if arvore[0] == valor:
        return "Valor {} encontrado!".format(valor)

    # Se o valor é menor que o valor da raiz, buscar na subárvore esquerda
    if valor < arvore[0]:
        return buscar(arvore[1], valor)
    else:
        # Se o valor é maior, buscar na subárvore direita
        return buscar(arvore[2], valor)


#Exercício

# Lista de comentários
comentarios = ["Eu adorei este produto", "Péssima experiência", "Muito bom, mas pode melhorar"]

# Lista de stopwords
stopwords = ["eu", "este", "mas", "pode"]

# Função simples para remover stopwords
def remover_stopwords(comentario, stopwords):
    palavras = comentario.split()  # separa as palavras em uma lista (espaço é o delimitador)
    palavras_filtradas = []
    for palavra in palavras:
        if palavra.lower() not in stopwords:
            palavras_filtradas.append(palavra)
    return " ".join(palavras_filtradas)

# Processar todos os comentários
for i in range(len(comentarios)):
    comentarios[i] = remover_stopwords(comentarios[i], stopwords)

print("Comentários filtrados:", comentarios)


#Processamento dos comentários em ordem

# Fila de comentários (FIFO)
fila_comentarios = comentarios

# Processar os comentários em ordem
while len(fila_comentarios) > 0:
    comentario = fila_comentarios.pop(0).lower()  # Remove o primeiro item da fila
    print("Processando comentário:", comentario)


# Função para Calcular a Altura da Árvore
def altura(arvore):
    if arvore is None:
        return -1
    else:
        altura_esquerda = altura(arvore[1])
        altura_direita = altura(arvore[2])
        return 1 + max(altura_esquerda, altura_direita)

print("Altura da árvore:", altura(arvore))

# Função para Buscar elemento na Árvore
def buscar(arvore, valor):
    # Caso base: árvore vazia ou encontramos o valor
    if arvore is None:
        return "Valor não encontrado."
    if arvore[0] == valor:
        return "Valor {} encontrado!".format(valor)
    
    # Se o valor é menor que o valor atual, buscar na subárvore esquerda
    if valor < arvore[0]:
        return buscar(arvore[1], valor)
    # Se o valor é maior, buscar na subárvore direita
    else:
        return buscar(arvore[2], valor)



# Pilha de comentários negativos
pilha_negativos = []
comentarios = ["Produto excelente", "Péssimo atendimento", "Bom custo-benefício", "Entrega horrível"]

# Adicionar comentários negativos à pilha
for comentario in comentarios:
    if "Péssimo" in comentario or "horrível" in comentario:
        pilha_negativos.append(comentario)  # Adiciona os negativos à pilha

# Processar os comentários negativos (último a entrar é o primeiro a sair)
ordem = 1
while len(pilha_negativos) > 0:
    comentario = pilha_negativos.pop()
    print(f"[{ordem}] Processando comentário negativo:", comentario)
    ordem += 1
