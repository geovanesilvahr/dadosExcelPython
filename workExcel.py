import pandas as pd
import time

x = pd.read_excel(r"C:\estudo_dev\dados_python\dados.xlsx",
                  engine='openpyxl', na_filter=False)
nomes = x['AUTORES']
n = []

for i in range(len(nomes)):
    if nomes[i] == '':
        pass
    else:
        n.append(nomes[i])

print(n)
