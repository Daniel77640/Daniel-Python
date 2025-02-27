
import csv

dados = [
    ['Carro', 'Portas', 'L/100km'],
    ['Fiat', 6, 6.1],
    ['Citroen', 12, 8.9],
    ['Seat', 4, 5.3],
    ['Audi', 3, 8.8]
]

file_path = 'carros.csv'

with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(dados)

print(f'Ficheiro CSV criado em: {file_path}')

import csv

file_path = 'carros.csv'

with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    
    for linha in csv_reader:
        print(linha)
