import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from faker import Faker

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
print(df_scores.head())