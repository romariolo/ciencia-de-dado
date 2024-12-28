import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Criação de um DataFrame com dados simulados
data = pd.DataFrame({
    'idade': np.random.randint(18, 70, size=200),  # Valores de idade entre 18 e 69
    'satisfacao': np.random.randint(1, 6, size=200),  # Satisfação de 1 a 5
    'segmento': np.random.choice(['A', 'B', 'C'], size=200)  # Segmentos A, B e C
})

print(data)

# Listas para armazenar as métricas de satisfação por segmento
listamedias = []
listamedianas = []
listamodas = []

# Identificar os segmentos únicos e ordenar
segmentos = sorted(data['segmento'].unique())

# Calcular a média, mediana e moda para cada segmento
for segmento in segmentos:
    segmento_data = data[data['segmento'] == segmento]['satisfacao']

    media = segmento_data.mean()  # Cálculo da média
    mediana = segmento_data.median()  # Cálculo da mediana
    moda = segmento_data.mode().iloc[0]  # Usamos iloc para pegar o primeiro valor, caso haja múltiplas modas

    listamedias.append(media)
    listamedianas.append(mediana)
    listamodas.append(moda)

    print(f"Segmento {segmento}:")
    print(f" Média de Satisfação: {media}")
    print(f" Mediana de Satisfação: {mediana}")
    print(f" Moda de Satisfação: {moda}")
    print("\n")

# Dados dos segmentos
dados_segmentos = {
    "Segmento": segmentos,
    "Média de Satisfação": listamedias,
    "Mediana de Satisfação": listamedianas,
    "Moda de Satisfação": listamodas
}

# Criando o DataFrame
df_segmentos = pd.DataFrame(dados_segmentos)

# Exibindo o DataFrame
print(df_segmentos)

# Gerando o boxplot para visualizar a distribuição de satisfação por segmento
plt.figure(figsize=(10, 6))
data.boxplot(column="satisfacao", by="segmento", grid=False)

plt.title("Distribuição de Satisfação por Segmento")
plt.suptitle("")
plt.xlabel("Segmento")
plt.ylabel("Nível de Satisfação")

plt.show()

# Lista para armazenar as medidas de dispersão
medidas_dispersao = []

# Calcular medidas de dispersão para cada segmento
for segmento in sorted(data['segmento'].unique()):
    segmento_data = data[data['segmento'] == segmento]['satisfacao']

    amplitude = segmento_data.max() - segmento_data.min()  # Amplitude
    variancia = segmento_data.var()  # Variância
    desvio_padrao = segmento_data.std()  # Desvio padrão
    coeficiente_variacao = desvio_padrao / segmento_data.mean() if segmento_data.mean() != 0 else 0  # Coeficiente de variação

    medidas_dispersao.append({
        "Segmento": segmento,
        "Amplitude": amplitude,
        "Variância": variancia,
        "Desvio Padrão": desvio_padrao,
        "Coeficiente de Variação": coeficiente_variacao
    })

# Criando o DataFrame com as medidas de dispersão
df_dispersao = pd.DataFrame(medidas_dispersao)
print(df_dispersao)

# Contagem do número total de avaliações em cada segmento
total_A = len(data[data['segmento'] == 'A'])
total_B = len(data[data['segmento'] == 'B'])
total_C = len(data[data['segmento'] == 'C'])

# Definindo eventos e calculando probabilidades
# Evento A: cliente do Segmento A deu uma nota maior que 3
evento_A_favoraveis = len(data[(data['segmento'] == 'A') & (data['satisfacao'] > 3)])
prob_evento_A = evento_A_favoraveis / total_A

# Evento B: cliente do Segmento B deu uma nota menor ou igual a 2
evento_B_favoraveis = len(data[(data['segmento'] == 'B') & (data['satisfacao'] <= 2)])
prob_evento_B = evento_B_favoraveis / total_B

# Evento C: cliente do Segmento C deu uma nota igual a 5
evento_C_favoraveis = len(data[(data['segmento'] == 'C') & (data['satisfacao'] == 5)])
prob_evento_C = evento_C_favoraveis / total_C

# Exibindo as probabilidades
print(f"Probabilidade de um cliente do Segmento A dar uma nota maior que 3: {prob_evento_A:.2f}")
print(f"Probabilidade de um cliente do Segmento B dar uma nota menor ou igual a 2: {prob_evento_B:.2f}")
print(f"Probabilidade de um cliente do Segmento C dar uma nota igual a 5: {prob_evento_C:.2f}")

# Evento: cliente deu uma nota maior que 3 (Evento A)
total_nota_maior_3 = len(data[data['satisfacao'] > 3])

# Evento: cliente pertence ao segmento A e deu uma nota maior que 3 (Evento A ∩ B)
evento_A_e_B = len(data[(data['segmento'] == 'A') & (data['satisfacao'] > 3)])

# Probabilidade condicional: cliente pertence ao Segmento A dado que deu nota maior que 3
prob_A_dado_nota_maior_3 = evento_A_e_B / total_nota_maior_3

print(f"Probabilidade de um cliente ser do Segmento A dado que ele deu uma nota maior que 3: {prob_A_dado_nota_maior_3:.2f}")

# Função para calcular o intervalo de confiança para a média
def intervalo_de_confianca(media, desvio_padrao, n, nivel=0.95):
    """Calcula o intervalo de confiança para a média.

    Args:
        media: Média da amostra.
        desvio_padrao: Desvio padrão da amostra.
        n: Tamanho da amostra.
        nivel: Nível de confiança (padrão: 0.95).

    Returns:
        Tupla com os limites inferior e superior do intervalo.
    """
    z = stats.norm.ppf(1 - (1 - nivel) / 2)  # Valor crítico para 95% de confiança
    margem_erro = (desvio_padrao / np.sqrt(n)) * z
    return media - margem_erro, media + margem_erro

# Lista para armazenar os resultados dos intervalos de confiança
resultados_ic = []

# Calcular intervalos de confiança para cada segmento
for segmento in sorted(data['segmento'].unique()):
    segmento_data = data[data['segmento'] == segmento]['satisfacao']
    media = segmento_data.mean()
    desvio_padrao = segmento_data.std()
    n = len(segmento_data)
    ic_inferior, ic_superior = intervalo_de_confianca(media, desvio_padrao, n)

    resultados_ic.append({
        "Segmento": segmento,
        "Intervalo de confiança Inferior": ic_inferior,
        "Intervalo de confiança Superior": ic_superior
    })

# Criando o DataFrame com os intervalos de confiança
df_ic = pd.DataFrame(resultados_ic)
print(df_ic)
