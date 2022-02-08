import pandas as pd

pessoas = pd.read_excel(r"C:\estudo_dev\dados_python\pessoas.xlsx", engine='openpyxl', na_filter=False)
nome_cpf = pd.read_excel(r"C:\estudo_dev\dados_python\nome_cpf.xlsx", engine='openpyxl', na_filter=False)
                  
nomePessoas = pessoas['NOME']
nomesCPF = nome_cpf['NOME']

#Looping - Verifica individualmente se o NOME de PESSOAS.xlsx está contida no NOME_CPF.xlsx
for i in range(len(nomePessoas)):
    for a in range(len(nomesCPF)):
        if nomePessoas.values[i] == nomesCPF.values[a]:
            print(nome_cpf.values[a])
            break
        else:
            pass
            
      
