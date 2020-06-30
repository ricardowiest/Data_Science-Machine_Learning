import pandas as pd

base = pd.read_csv('credit_dataA.csv') #variavel le o arquivo
base.describe()  
base.loc[base['age'] < 0] #seleciona a base idade para verificar erro < 0

# Preencher valores (idades) com erros pela média
base.mean() # visualisa a média
base['age'][base.age > 0].mean() #busca média da idade excluindo as idades < 0

base.loc[base.age < 0, 'age'] = 40.92 #altera idades negativas para média

pd.isnull(base['age'])
