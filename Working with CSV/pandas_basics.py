# O Pandas é uma biblioteca open-source de Python para análise e manipulação de dados. O Pandas é popularmente utilizado
# em ciência de dados e análise de dados, mas também pode ser usado para uma variedade de outras tarefas, como:
# Limpeza e tratamento de dados: O Pandas fornece ferramentas para lidar com dados ausentes, duplicados e inconsistentes
# Exploratory data analysis(EDA): O Pandas permite que você explore e visualize os seus dados para identificar padrões e
#                                 tendências.
# Suporte em atividades de Machine Learning: O Pandas pode ser usado para pré-processar e preparar os seus dados para
#                                            modelos de Machine Learning.
# Consultas e queries em bancos de dados relacionais: O Pandas pode se conectar a bancos de dados relacionais e executar
#                                                     consultas SQL.
# Visualização de dados: O Pandas fornece ferramentas para criar gráficos e visualizações de dados de alta qualidade.
# Webscraping: O Pandas pode ser usado para extrair dados de sites da web.

# O Pandas possui dois objetos primários importantes:
# Series: Uma série é um array unidimensional rotulado. As rótulas são chamadas de "índices".
# DataFrames: Um DataFrame é uma estrutura de dados bidimensional rotulada semelhante a uma planilha. As colunas são
# rotuladas com nomes e as linhas são rotuladas com índices.
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html  sobre o read_csv().to_dict
import pandas
import csv
# import webbrowser

# webbrowser.open('https://pandas.pydata.org/docs/')
# webbrowser.open('https://pandas.pydata.org/docs/reference/index.html')

# P1: Sem usar funções do método csv:
# with open('weather_data.csv', encoding='utf-8') as file:
#     data: list = [row.strip().split(',') for row in file]


# P2: Usar funções que pertencem ao método csv:
# with open('weather_data.csv', encoding='utf-8') as file:
#     data = csv.reader(file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
# todo Mas não é funcional quando tiver um data muito maior complexa. Portanto, é muito melhor usar o Pandas!!!!!

# P3: Usar o módulo Pandas:
data = pandas.read_csv('weather_data.csv')
print(data, '\n', '-' * 175)  # Print num formato de tabela

# Get data in Columns:
print(data.columns)  # Index(['day', 'temp', 'condition'], dtype='object')
print(data.columns[0])  # day
print(list(data.columns))  # ['day', 'temp', 'condition']
print(data['temp'], '\n', '-' * 175)
print(data.temp, '\n', '-' * 175)

print(data.day == 'Monday', '\n', '-' * 175)

# Get data in Row:
print(data[data.day == 'Monday'], '\n', '-' * 175)

print(data.head(3), '\n', '-' * 175)  # Print as 3 primeiras linhas num formato de tabela
print(data.tail(3), '\n', '-' * 175)  # Print as 3 últimas linhas num formato de tabela
print(data['temp'].notna(), '\n', '-' * 175)  # Verifica se existe NA in the column
print(data.loc[data['temp'] > 21, 'day'], '\n', '-' * 175)  # Verifica onde a temperatura > 21 e return coluna day
print(data.iloc[3:5, 1:3], '\n', '*' * 175)  # Print as linhas 3 e 4 e as colunas 1 e 2!!

data_dict = data.to_dict()  # Transforma os dados em dicionário
print(data_dict, '\n', '-' * 175)
data_list = data['temp'].to_list()  # Transforma os dados numa lista
print(data_list, '\n', '*' * 175)

# P1: Calcular a média:
print(sum(data_list) / len(data_list), '-' * 175)  # Calculei a média: 17.428571428571427
#  P2: Calcular a médio pelo series.mean():
print(data['temp'].mean(), '\n', '*' * 175)  # 17.428571428571427

print(data['temp'].max(), '\n', '*' * 175)
print(data[data.temp == data.temp.max()], '\n', '*' * 175)
print(data[data.condition == 'Rain'], '\n', '*' * 175)
print(data.loc[data.day == 'Monday', 'temp'], '\n', '-' * 175)




