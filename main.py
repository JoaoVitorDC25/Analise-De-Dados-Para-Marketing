import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import config as cfg
import utils as ut
import data_generator as dg
import charts as ch

dados_ecommerce=dg.data_generator_ecommmerce()

ut.clear()

# ut.text(f"Shape da nossa massa de dados: {dados_ecommerce.shape}",
#         "Exemplo dos 5 primeiros usuarios: \n",
#         "\n Colunas: [Visitas, Tempo no site (min), Itens no Carrinho, Valor da compra(R$)] \n\n",
#         dados_ecommerce[:5])

print("\n Shape da nossa massa de dados:", dados_ecommerce.shape)
print("\n Exemplo dos 5 primeiros usuarios:")
print("\n Colunas: [Visitas, Tempo no site (min), Itens no Carrinho, Valor da compra(R$)]\n")
print(dados_ecommerce[:5])

#Separar colunas
visitas_col = dados_ecommerce[:,0]
tempo_col = dados_ecommerce[:,1]
itens_col = dados_ecommerce[:,2]
valor_col = dados_ecommerce[:,3]

print("\n --- ANÁLISE ESTATÍSTICA GERAL --- ")

#Media
media_visitas = np.mean(visitas_col)
media_tempo = np.mean(tempo_col)
media_itens = np.mean(itens_col)
media_valor = np.mean(valor_col)

print(f"\nMédia de Visitas: {media_visitas:.2f}")
print(f"Média de Tempo no Site: {media_tempo:.2f} min")
print(f"Média de Itens no Carrinho: {media_itens:.2f}")
print(f"Média de Valor de Compra (Ticket Médio): R$ {media_valor:.2f}")

#Mediana
mediana_valor = np.median(valor_col)
print(f"\nMediana do Valor de Compra: R$ {mediana_valor:.2f}")

#Desvio padrão
std_valor = np.std(valor_col)
print(f"\nDesvio padrao do Valor de Compra: R$ {std_valor:.2f}")

#Valores Máximos e Mínimos
max_valor = np.max(valor_col)
min_valor_positivo = np.min(valor_col[valor_col>0])
print(f"Maior Valor de Compra: R$ {max_valor:.2f}")
print(f"Menor Valor de Compra: R$ {min_valor_positivo:.2f}")

#Grafico
ch.hist_graphic(
        valor_col=valor_col,
        media_valor=media_valor,
        mediana_valor=mediana_valor,
        std_valor=std_valor,
        xLabel='Valor da Compra (R$)',
        yLabel='Frequência',
        titulo='Distribuição dos Valores de Compra')

#Filtro para visitantes que não compraram 
visitantes_sem_compra = dados_ecommerce[dados_ecommerce[:,3]==0]

print("\n --- ANÁLISE: VISITANTES QUE NÃO COMPRAM ---\n")
print(f"Número de visitantes que não compraram: {visitantes_sem_compra.shape[0]}")

#Estatísticas deste segmento
media_tempo_sem_compra = np.mean(visitantes_sem_compra[:,1])
media_visitas_sem_compra =np.mean(visitantes_sem_compra[:,0])

print(f"Média de visitas desses visitantes: {media_visitas_sem_compra:.2f}")
print(f"Apesar de não comprarem, eles passam em média: {media_tempo_sem_compra:.2f}")

#A função np.corrcoef calcula a matriz de correlação
#rowvar = False indica que as colunas são as variáveis
matriz_correlacao = np.corrcoef(dados_ecommerce, rowvar = False)

print("\n --- MATRIZ DE CORRELAÇÃO ---\n")
print("[Visitas, Tempo, Itens, Valor]\n")
print(np.round(matriz_correlacao,2))

nomes_variaveis = ["Visitas", "Tempo no Site", "Itens no Carrinho", "Valor da Compra"]

#Converter para Dataframe
df_correlacao = pd.DataFrame(matriz_correlacao,
                             index = nomes_variaveis,
                             columns = nomes_variaveis)

#Matriz de correlação (mapa de calor)
ch.heatmap_graphic(
    dados=df_correlacao,
    titulo="Matriz de Correlação")