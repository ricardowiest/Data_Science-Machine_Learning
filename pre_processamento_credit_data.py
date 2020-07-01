import pandas as pd

base = pd.read_csv('credit_dataA.csv') #variavel le o arquivo
base.describe()  
base.loc[base['age'] < 0] #seleciona a base idade para verificar erro < 0

# Preencher valores (idades) com erros pela média
base.mean() # visualisa a média
base['age'][base.age > 0].mean() #busca média da idade excluindo as idades < 0

base.loc[base.age < 0, 'age'] = 40.92 #altera idades negativas para média

pd.isnull(base['age']) #identifica se no campo idade está vazio
base.loc[pd.isnull(base['age'])] #somente os campos vazios

#criação das variáveis para tratamento dos dados
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values= 'NaN', strategy= 'mean', axis =0)
imp = SimpleImputer.fit(previsores[:, 0:3])
previsores[:, 0:3] = imp.transform(previsores[:, 0:3])
