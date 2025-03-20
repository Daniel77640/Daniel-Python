"""1. Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mês e ano para
três variáveis inteiras."""
"""data = input("Digite uma data no seguinte formato DD-MM-AAAA ")
dia, mês, ano = map(int, data.split('-'))
print(f"Dia: {dia}")
print(f"Mês: {mês}")
print(f"Ano: {ano}")"""


"""2. Escreve uma função em Python que dada uma palavra retorne o número de vogais nessa
palavra."""
"""def conta_vogais(serie):
    vogais = "a, e, i, o, u, A, E, I, O, U"
    contador = sum(1 for letra in serie if letra in vogais)
    return contador
serie = input("Digite uma palavra: ")
print(f"O número de vogais é: {conta_vogais(serie)}")"""


"""3. Escreve uma função em Python que dada uma lista de números imprime a soma dos
valores dessa lista, o número de elementos da lista e a media desses valores. Implementa
tratamento de exceções no teu código (try…except…else..finally)."""
"""def analisar_lista():
    try:
        entrada = input("Digite uma lista de números separados por espaço entre eles: ")
        numeros = list(map(float, entrada.split()))
        if not numeros:
            raise ValueError("Lista sem valores. Não sendo possível calcular a média.")
        soma = sum(numeros)
        quantidade = len(numeros)
        media = soma / quantidade
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    else:
        print(f"Soma de valores: {soma}")
        print(f"Número de elementos: {quantidade}")
        print(f"Média de valores: {media:.2f}")
    finally:
        print("Fim dos cálculos.")
analisar_lista()"""


"""4.a. Cria um array de números 1 com shape (8, 2)"""
"""import numpy as np
array = np.ones((8, 2))
print(array)"""


"""4.b. Cria um array de zeros com shape (5, 7)"""
"""array = np.zeros((5, 7))
print(array)"""


"""4.c. Subtraia o novo array de outro com dados aleatórios e armazene-o numa variável
chamada subarray"""
"""array_zeros = np.zeros((5, 7))
array_random = np.random.rand(5, 7)
subarray = array_random - array_zeros
print("Array aleatório:")
print(array_random)
print("\n Array de zeros:")
print(array_zeros)
print("\n Resultado da subtração (subarray):")
print(subarray)"""


"""4.d. Calcula a média dos valores do array subarray"""
"""array_random = np.random.rand(5, 7)
array_zeros = np.zeros((5, 7))
subarray = array_random - array_zeros
media_subarray = np.mean(subarray)
print("Subarray:")
print(subarray)
print("\n Média dos valores do subarray:", media_subarray)"""

"""5. Usando as bibliotecas Pandas e MatPlotLib e um dataset (podes selecionar das aulas, fazer
download na plataforma kaggle ou escolher um dataset pessoal), elabora um notebook
jupyter no qual efetues:
    a. Limpeza e tratamento de dados;"""
"""import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('vendas.csv')
df.head()
df.info()
df.isnull().sum()
df.describe()
df['Vendas'].fillna(df['Vendas'].mean(), inplace=True)
df['Preço Unitário'].fillna(df['Preço Unitário'].mean(), inplace=True)
df.drop_duplicates(inplace=True)
df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
df['Valor Total'] = df['Vendas'] * df['Preço Unitário']
df_filtered = df[df['Vendas'] > 200]
df['Ano'] = df['Data'].dt.year
df['Mês'] = df['Data'].dt.month
df_category_sales = df.groupby('Categoria')['Valor Total'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(df_category_sales['Categoria'], df_category_sales['Valor Total'], color='skyblue')
plt.title('Valor Total de Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor Total de Vendas (R$)')
plt.xticks(rotation=45)
plt.show()
df_monthly_sales = df.groupby(['Ano', 'Mês'])['Valor Total'].sum().reset_index()
plt.figure(figsize=(12, 6))
for year in df_monthly_sales['Ano'].unique():
    df_year = df_monthly_sales[df_monthly_sales['Ano'] == year]
    plt.plot(df_year['Mês'], df_year['Valor Total'], label=f'Ano {year}', marker='o')
plt.title('Vendas Mensais por Ano')
plt.xlabel('Mês')
plt.ylabel('Valor Total de Vendas (R$)')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.grid(True)
plt.show()
df.to_csv('vendas_tratadas.csv', index=False)"""



"""5.b.Processamento de dados: groupby, filter, criação de novas colunas,…"""
"""import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('vendas_produtos.csv')
df.info()
df.describe()
df.head()
print(df.isnull().sum())
df['Desconto (%)'].fillna(df['Desconto (%)'].mean(), inplace=True)
df.drop_duplicates(inplace=True)
df['Data_Venda'] = pd.to_datetime(df['Data_Venda'])
df_produto = df.groupby('Produto')['Total_Venda'].sum().reset_index().sort_values('Total_Venda', ascending=False)
df_filial = df.groupby('Filial')['Total_Venda'].sum().reset_index().sort_values('Total_Venda', ascending=False)
df['Ano_Mês'] = df['Data_Venda'].dt.to_period('M')
df_mes = df.groupby('Ano_Mês')['Total_Venda'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(df_produto['Produto'], df_produto['Total_Venda'], color='skyblue')
plt.title('Vendas Totais por Produto')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas (€)')
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(10, 6))
plt.bar(df_filial['Filial'], df_filial['Total_Venda'], color='salmon')
plt.title('Vendas Totais por Concessionario')
plt.xlabel('Filial')
plt.ylabel('Total de Vendas (€)')
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(10, 6))
plt.plot(df_mes['Ano_Mês'].astype(str), df_mes['Total_Venda'], marker='o', color='purple')
plt.title('Vendas Totais por Mês')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas (€)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))
plt.scatter(df['Desconto (%)'], df['Total_Venda'], color='orange')
plt.title('Relação entre Desconto e Total de Vendas')
plt.xlabel('Desconto (%)')
plt.ylabel('Total de Vendas (€)')
plt.show()
df.to_csv('vendas_tratadas.csv', index=False)"""
