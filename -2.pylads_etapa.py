import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random
from seaborn import kdeplot


np.random.seed(42)  # Para garantir reprodutibilidade

# Criando uma instância do Faker
fake = Faker('pt_BR')  # Usando o local 'pt_BR' para gerar dados em português

# Criando dados de exemplo
datas = [fake.date_between(start_date='-1y', end_date='today') for _ in range(1000)]  # 1000 datas aleatórias no último ano
times = ['Flamengo', 'Palmeiras', 'Corinthians', 'São Paulo', 'Grêmio', 'Internacional', 'Atlético-MG', 'Cruzeiro', 'Santos']
posicoes = ['Goleiro', 'Zagueiro', 'Lateral', 'Volante', 'Meia', 'Atacante']
jogadores = [fake.name() for _ in range(100)]  # 100 nomes fictícios de jogadores

# Gerando 1000 registros aleatórios
n_registros = 1000
data_scores = []

for _ in range(n_registros):
    data = np.random.choice(datas)
    time = np.random.choice(times)
    jogador = np.random.choice(jogadores)
    posicao = np.random.choice(posicoes)
    gols = np.random.randint(0, 4)  # Gols entre 0 e 3
    assistencias = np.random.randint(0, 3)  # Assistências entre 0 e 2
    minutos_jogados = np.random.randint(0, 91)  # Minutos jogados entre 0 e 90
    nota = round(np.random.uniform(5, 10), 1)  # Nota entre 5.0 e 10.0
    
    data_scores.append({
        'data': data,
        'time': time,
        'jogador': jogador,
        'posicao': posicao,
        'gols': gols,
        'assistencias': assistencias,
        'minutos_jogados': minutos_jogados,
        'nota': nota
    })

# Criando o DataFrame
df_scores = pd.DataFrame(data_scores)
df_scores['data'] = df_scores['data'].astype('object')

# Salvando como CSV para uso futuro
df_scores.to_csv('dados_scores.csv', index=False)

# Visualizando as primeiras linhas
print("Primeiras linhas do DataFrame:")
print(df_scores.head())

# visualizando as últimas linhas
print("\nÚltimas linhas do DataFrame:")
print(df_scores.tail())

# Verificando o formato do DataFrame (linhas, colunas) com shape
print(f"Formato do DataFrame: {df_scores.shape}")
print(f"Número de linhas: {df_scores.shape[0]}")
print(f"Número de colunas: {df_scores.shape[1]}")

# Verificando os tipos de dados
print("Nomes das colunas:")
print(df_scores.columns.tolist())

# Verificando informações sobre o DataFrame com info()
print("Informações do DataFrame:")
print(df_scores.info())

# Estatísticas descritivas com describe()
print("Estatísticas descritivas:")
print(df_scores.describe())

# Contagem de valores únicos com nunique()
print("Número de valores únicos em cada coluna:")
print(df_scores.nunique())

# Verificando valores ausentes com isnull()
print("Valores nulos em cada coluna:")
print(df_scores.isnull().sum())

# Filtrando os dados do time do Santos
santos_scores = df_scores[df_scores['time'] == 'Santos']
print("\nDados do time Santos:")
print(santos_scores.head())

# Filtrando jogadores que marcaram mais de 2 gols
jogadores_gols = df_scores[df_scores['gols'] > 2]
print("\nJogadores que marcaram mais de 2 gols:")
print(jogadores_gols[['jogador', 'gols']].head())

# Selecionando múltiplas colunas (retorna um DataFrame)
print("\nSelecionando múltiplas colunas (jogador, gols, assistencias):")
print(df_scores[['jogador', 'gols', 'assistencias']].head())

# Agrupando os dados por time e somando os gols
gols_por_time = df_scores.groupby('time')['gols'].sum().reset_index()
print("\nGols por time:")
print(gols_por_time)

# Filtrando com múltiplas condições usando operadores lógicos & (AND) e | (OR)
jogadores_gols_assistencias = df_scores[(df_scores['gols'] > 2) & (df_scores['assistencias'] > 1)]
print("\nJogadores que marcaram mais de 2 gols e deram mais de 1 assistência:")
print(jogadores_gols_assistencias[['jogador', 'gols', 'assistencias']].head())

# Usando isin() para filtrar com uma lista de valores
times_interessados = ['Flamengo', 'Palmeiras']
jogadores_times_interessados = df_scores[df_scores['time'].isin(times_interessados)]
print("\nJogadores dos times Flamengo e Palmeiras:")
print(jogadores_times_interessados[['jogador', 'time']].head())

# Usando between() para filtrar valores em um intervalo
jogadores_minutos = df_scores[df_scores['minutos_jogados'].between(30, 60)]
print("\nJogadores que jogaram entre 30 e 60 minutos:")
print(jogadores_minutos[['jogador', 'minutos_jogados']].head())

# Ordenando por uma coluna em ordem crescente (padrão)
df_ordenado = df_scores.sort_values(by='gols')
print("\nDataFrame ordenado por gols (crescente):")
print(df_ordenado[['jogador', 'gols']].head())

# Ordenando por múltiplas colunas
df_ordenado_multiplas = df_scores.sort_values(by=['time', 'gols'], ascending=[True, False])
print("\nDataFrame ordenado por time e gols (crescente e decrescente):")
print(df_ordenado_multiplas[['time', 'jogador', 'gols']].head(10))

# Definindo uma coluna como índice
df_scores.set_index('data', inplace=True)
print("\nDataFrame com a coluna 'data' como índice:")
print(df_scores.head())

print(df_scores.index.unique())

# Acessando dados através do índice
data_aleatoria = np.random.choice(df_scores.index.unique())  # Escolhe uma data aleatória do índice
print(f"Dados do dia {data_aleatoria}:")
print(df_scores.loc[data_aleatoria].head())

# Resetando o índice para voltar ao formato original
df_scores.reset_index(inplace=True)
print("\nDataFrame com o índice resetado:")
print(df_scores.head())

# Calculando a média (mean) de uma coluna
media_gols = df_scores['gols'].mean()
print(f"\nMédia de gols: {media_gols:.2f}")

# Calculando a soma (sum) de uma coluna
soma_gols = df_scores['gols'].sum()
print(f"Soma total de gols: {soma_gols}")

# Calculando o mínimo (min) e máximo (max)
min_gols = df_scores['gols'].min()
max_gols = df_scores['gols'].max()
print(f"Mínimo de gols: {min_gols}")
print(f"Máximo de gols: {max_gols}")

# Calculando a mediana (median / 50º percentil)
mediana_gols = df_scores['gols'].median()
print(f"Mediana de gols: {mediana_gols}")

# Calculando outros percentis
percentis = df_scores['gols'].quantile([0.25, 0.5, 0.75])
print(f"Percentis de gols (25%, 50%, 75%):\n{percentis}")

# Calculando o desvio padrão (std) e variância (var)
desvio_padrao_gols = df_scores['gols'].std()
variancia_gols = df_scores['gols'].var()
print(f"Desvio padrão de gols: {desvio_padrao_gols:.2f}")

# Calculando a média de gols por time
media_gols_por_time = df_scores.groupby('time')['gols'].mean().reset_index()
print("\nMédia de gols por time:")
print(media_gols_por_time)

# Calculando estatísticas descritivas de gols por time
stats_por_time = df_scores.groupby('time')['gols'].agg(['count', 'mean', 'min', 'max'])
print("\nEstatísticas descritivas de gols por time:")
print(stats_por_time)

# Renomeando as colunas para melhor legibilidade
stats_por_time.rename(columns={'count': 'total_jogos', 'mean': 'media_gols', 'min': 'min_gols', 'max': 'max_gols'}, inplace=True)
print("\nEstatísticas descritivas de gols por time (com colunas renomeadas):")
print(stats_por_time)

# Exemplo básico: agrupando por posição e calculando a média de gols
gols_por_categoria = df_scores.groupby('posicao')['gols'].mean().reset_index()
print("\nMédia de gols por posição:")
print(gols_por_categoria)

# Contagem de jogadores por posição
contagem_posicoes = df_scores['posicao'].value_counts().reset_index()
contagem_posicoes.columns = ['posicao', 'contagem']
print("\nContagem de jogadores por posição:")
print(contagem_posicoes)

# Soma do valor de gols por posição
soma_gols_posicoes = df_scores.groupby('posicao')['gols'].sum().reset_index()
print("\nSoma de gols por posição:")
print(soma_gols_posicoes)

# Agrupando por posição e calculando a média de gols e assistências
gols_assistencias_posicoes = df_scores.groupby('posicao').agg({'gols': 'mean', 'assistencias': 'mean'}).reset_index()
print("\nMédia de gols e assistências por posição:")
print(gols_assistencias_posicoes)

# Aplicando diferentes funções a diferentes colunas
gols_assistencias_stats = df_scores.groupby('posicao').agg({'gols': ['mean', 'sum'], 'assistencias': ['mean', 'sum']}).reset_index()
print("\nEstatísticas de gols e assistências por posição:")
print(gols_assistencias_stats)

# Convertendo a coluna 'data' para datetime
df_scores['data'] = pd.to_datetime(df_scores['data'])
# Extraindo o mês e o ano da data
df_scores['mes'] = df_scores['data'].dt.month
df_scores['ano'] = df_scores['data'].dt.year
df_scores['dia'] = df_scores['data'].dt.day

# Visualizando as novas colunas
print("\nDataFrame com colunas de mês, ano e dia:")
print(df_scores[['data', 'mes', 'ano', 'dia']].head())

# Criando novas colunas com operações matemáticas
df_scores['gols_por_minuto'] = df_scores['gols'] / df_scores['minutos_jogados']
df_scores['assistencias_por_minuto'] = df_scores['assistencias'] / df_scores['minutos_jogados']
print("\nDataFrame com colunas de gols e assistências por minuto:")
print(df_scores[['gols_por_minuto', 'assistencias_por_minuto']].head())

# Criando coluns personalizadas com apply() e funções personalizadas
def classificar_nota(nota):
    if nota >= 9:
        return 'Excelente'
    elif nota >= 7:
        return 'Bom'
    elif nota >= 5:
        return 'Regular'
    else:
        return 'Ruim'
    
df_scores['classificacao_nota'] = df_scores['nota'].apply(classificar_nota)
print("\nDataFrame com classificação de notas:")
print(df_scores[['jogador', 'nota', 'classificacao_nota']].head())

# Definindo uma função para categorizar a quantidade
def categorizar_gols(gols):
    if gols == 0:
        return 'Nenhum'
    elif gols == 1:
        return 'Um'
    elif gols == 2:
        return 'Dois'
    else:
        return 'Mais de dois'
df_scores['categoria_gols'] = df_scores['gols'].apply(categorizar_gols)
print("\nDataFrame com categoria de gols:")
print(df_scores[['jogador', 'gols', 'categoria_gols']].head())

# Visualizando as novas colunas categóricas
print("\nContagem de categorias de gols:")
print(df_scores['categoria_gols'].value_counts())

# Agrupando por categoria de gols e contando
gols_por_categoria = df_scores.groupby('categoria_gols')['gols'].count().reset_index()
print("\nContagem de gols por categoria:")
print(gols_por_categoria)
# Criando um gráfico de barras para visualizar a contagem de gols por categoria
plt.figure(figsize=(10, 6))
plt.bar(gols_por_categoria['categoria_gols'], gols_por_categoria['gols'], color='skyblue')
plt.title('Contagem de Gols por Categoria')
plt.xlabel('Categoria de Gols')
plt.ylabel('Contagem')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Criando um simples gráfico de linha
# Agrupando por data e somando os gols
gols_por_data = df_scores.groupby('data')['gols'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(gols_por_data['data'], gols_por_data['gols'], marker='o', linestyle='-', color='b')
plt.title('Gols ao longo do tempo')
plt.xlabel('Data')
plt.ylabel('Gols')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()

# Agrupando por mês e somando os gols
gols_por_mes = df_scores.groupby('mes')['gols'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(gols_por_mes['mes'], gols_por_mes['gols'], color='orange')
plt.title('Gols por Mês')
plt.xlabel('Mês')
plt.ylabel('Gols')
plt.xticks(gols_por_mes['mes'], ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Criando gráfico de linha por mês e ano
gols_por_mes_ano = df_scores.groupby(['ano', 'mes'])['gols'].sum().reset_index()

# Criando uma coluna para exibir "Mês/Ano" no eixo X
gols_por_mes_ano['mes_ano'] = gols_por_mes_ano['mes'].map({
    1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
    7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
}) + '/' + gols_por_mes_ano['ano'].astype(str)

plt.figure(figsize=(12, 6))
plt.plot(gols_por_mes_ano['mes_ano'], gols_por_mes_ano['gols'], marker='o', linestyle='-', color='g')
plt.title('Gols por Mês e Ano')
plt.xlabel('Mês/Ano')
plt.ylabel('Gols')
plt.xticks(rotation=45)  # Rotacionando os rótulos para melhor visualização
plt.grid()
plt.tight_layout()
plt.show()

# Histograma de gols
plt.figure(figsize=(10, 6))
plt.hist(df_scores['gols'], bins=10, color='purple', alpha=0.7)
plt.title('Distribuição de Gols')
plt.xlabel('Número de Gols')
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Histograma de minutos jogados
plt.figure(figsize=(10, 6))
plt.hist(df_scores['minutos_jogados'], bins=10, color='red', alpha=0.7)
plt.title('Distribuição de Minutos Jogados')
plt.xlabel('Minutos Jogados')
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Agrupando os dados por time e mês, somando os gols
gols_por_time_mes = df_scores.groupby(['time', 'mes'])['gols'].sum().reset_index()

# Criando um FacetGrid para gráficos de dispersão por time
g = sns.FacetGrid(gols_por_time_mes, col="time", col_wrap=3, height=4, sharey=True, sharex=True)
g.map(sns.scatterplot, "mes", "gols", color="blue", s=50)

# Configurando os rótulos e o layout
g.set_titles("{col_name}")
g.set_axis_labels("Mês", "Número de Gols")
g.set(xticks=range(1, 13), xticklabels=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("Dispersão de Gols por Time e Mês", fontsize=16)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Criando o gráfico de dispersão
plt.figure(figsize=(12, 6))
sns.scatterplot(data=gols_por_time_mes, x='mes', y='gols', hue='time', palette='tab10', s=100)

# Configurando o gráfico
plt.title('Dispersão de Gols por Time e Mês', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Número de Gols', fontsize=12)
plt.xticks(ticks=range(1, 13), labels=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'], rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Time', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Boxplot de gols por time
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_scores, x='time', y='gols', palette='Set3')
plt.title('Boxplot de Gols por Time', fontsize=16)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Número de Gols', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Boxplot de notas por posição
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_scores, x='posicao', y='nota', palette='Set2')
plt.title('Boxplot de Notas por Posição', fontsize=16)
plt.xlabel('Posição', fontsize=12)
plt.ylabel('Nota', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Criando um violinplot agrupado com violinos divididos
plt.figure(figsize=(12, 6))
sns.violinplot(data=df_scores, x='posicao', y='nota', hue='time', split=True, palette='Set2')

# Configurando o gráfico
plt.title('Distribuição de Notas por Posição e Time', fontsize=16)
plt.xlabel('Posição', fontsize=12)
plt.ylabel('Nota', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Time', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Selecionando apenas as colunas numéricas
colunas_numericas = df_scores.select_dtypes(include=['float64', 'int64'])

# Calculando a matriz de correlação
plt.figure(figsize=(10, 6))
correlation_matrix = colunas_numericas.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Matriz de Correlação', fontsize=16)
plt.tight_layout()
plt.show()

# Lista de times únicos
times_unicos = df_scores['time'].unique()

# Embaralhando os times para garantir aleatoriedade
random.shuffle(times_unicos)

# Contador para limitar a duas comparações
comparacoes_realizadas = 0

# Loop para comparar dois times por vez
for i in range(len(times_unicos)):
    for j in range(i + 1, len(times_unicos)):
        # Selecionando os dois times para comparação
        times_comparados = [times_unicos[i], times_unicos[j]]
        df_comparacao = df_scores[df_scores['time'].isin(times_comparados)]
        
        # Criando o violin plot para os dois times
        plt.figure(figsize=(12, 6))
        sns.violinplot(data=df_comparacao, x='posicao', y='nota', hue='time', split=True, palette='Set2')
        
        # Configurando o gráfico
        plt.title(f'Distribuição de Notas por Posição - {times_comparados[0]} vs {times_comparados[1]}', fontsize=16)
        plt.xlabel('Posição', fontsize=12)
        plt.ylabel('Nota', fontsize=12)
        plt.xticks(rotation=45)
        plt.legend(title='Time', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()
        
        # Incrementando o contador de comparações
        comparacoes_realizadas += 1
        
        # Interrompendo o loop após duas comparações
        if comparacoes_realizadas == 2:
            break
    if comparacoes_realizadas == 2:
        break

# Configurando o tamanho do gráfico
plt.figure(figsize=(12, 8))

# Iterando sobre as posições para criar densidades sobrepostas
posicoes_unicas = df_scores['posicao'].unique()
for i, posicao in enumerate(posicoes_unicas):
    subset = df_scores[df_scores['posicao'] == posicao]
    kdeplot(
        data=subset,
        x='nota',
        fill=True,
        alpha=0.6,
        label=posicao
    )

# Configurando o gráfico
plt.title('Distribuição de Notas por Posição (Ridge Plot)', fontsize=16)
plt.xlabel('Nota', fontsize=12)
plt.ylabel('Densidade', fontsize=12)
plt.legend(title='Posição', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Criando um FacetGrid para o ridge plot
g = sns.FacetGrid(df_scores, row="posicao", height=2, aspect=4, sharex=True, sharey=False)

# Adicionando o gráfico de densidade a cada facet
g.map(sns.kdeplot, "nota", fill=True, alpha=0.6, color="blue")

# Configurando o layout e os rótulos
g.set_titles("{row_name}")
g.set_axis_labels("Nota", "Densidade")
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("Distribuição de Notas por Posição (Ridge Plot)", fontsize=16)
plt.show()