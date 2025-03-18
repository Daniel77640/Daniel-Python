from turtle import pd
import matplotlib.pyplot as plt  # Import necessário
import numpy as np
plt.plot()
plt.plot([1, 2, 3, 4, 5])
x= [1, 2, 3, 4, 5]
y= [10, 20, 30, 40, 50]
plt.plot(x, y)
"""plt.show()"""
fig, ax = plt.subplots()
ax.plot(x, y)
x= np.linspace(0, 10, 100)
x[:10]

x = np.array([1, 2, 3, 4, 5])  # Convertendo para um array NumPy
y = np.array([10, 20, 30, 40, 50])

# Criando o primeiro gráfico (parábola)
fig, ax = plt.subplots()
ax.plot(x, x**2)  # Agora `x**2` funciona corretamente

# Criando o segundo gráfico (seno)
fig, ax = plt.subplots()
ax.scatter(x, np.sin(x))

"""plt.show()  # Para exibir os gráficos"""


produtos= {"Pão": 10, "Leite": 8, "Sorvete": 12}

fig, ax = plt.subplots()
ax.bar(produtos.keys(), produtos.values())
ax.set(title="Lista de produtos", ylabel="Preço")
fig, ax = plt.subplots()
ax.barh(list(produtos.keys()), list(produtos.values()))
""""plt.show()  # Para exibir os gráficos"""

x = np.random.randn(1000)

fig, ax=plt.subplots()
ax.hist(x)
"""plt.show()  # Para exibir os gráficos"""


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))
ax1.plot(x, x/2); #line
ax2.scatter(np.random.random(10), np.random.random(10)) #scatter
ax3.bar(produtos.keys(), produtos.values()) #bar
ax4.hist(np.random.random(1000)) #hist
"""plt.show()"""

import matplotlib.pyplot as plt  # Importar matplotlib se ainda não foi feito
import pandas as pd
df = pd.read_csv("heart-disease.csv") 
# Certifica-te de que 'mais_de_50' existe
mais_de_50 = df[df["age"] > 50]  # Filtrar pacientes com mais de 50 anos

fig, ax = plt.subplots(figsize=(10, 6))

# Criar scatter plot
scatter = ax.scatter(mais_de_50["age"], mais_de_50["chol"], c=mais_de_50["target"])

# Adicionar títulos e rótulos
ax.set(title="Doença cardíaca e níveis de colesterol",
       xlabel="Idade",
       ylabel="Colesterol")

# Adicionar legenda com cores baseadas na variável "target"
ax.legend(*scatter.legend_elements(), title="Alvo")

# Exibir o gráfico
plt.show()



import pandas as pd
df = pd.read_csv("heart-disease.csv") 
print(df.head())

fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(mais_de_50["age"],
                     mais_de_50["chol"],
                     c=mais_de_50["target"])
ax.set(title="Doença cardiaca e niveis de colestrol",
       xlabel="Idade",
       ylabel="colestrol")
ax.legend(*scatter.legend_elements(), title="Alvo");
plt.show()


