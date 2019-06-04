import json
import ast
import pandas as pd
import urllib
import requests
rm = urllib.request.urlopen('https://servicodados.ibge.gov.br/api/v2/censos/nomes/joao%7Cenzo')
datam = json.loads(rm.read())
rf = urllib.request.urlopen('https://servicodados.ibge.gov.br/api/v2/censos/nomes/leticia%7Cmaria') 
dataf = json.loads(rf.read())
enzo = datam[0]
joao = datam[1]
leticia = dataf[0]
maria = dataf[1]
##amod = {'tags': a}
##bmod = {'tags': b}


##a = ' '.join([''.join(dictionare)])
##b = a.count('periodo')
##print(a[4])


xm = (pd.DataFrame.from_dict(enzo['res'],))
ym = (pd.DataFrame.from_dict(joao['res'],))

xf = (pd.DataFrame.from_dict(leticia['res'],))
yf = (pd.DataFrame.from_dict(maria['res'],))
##x = 'enzo' + str(x)
##y = 'joao' + str(y)
##m = x.replace('[','')
##n = y.replace('[','')

print(xm)
print(ym)
print(xf)
print(yf)


##import numpy as np
##def excel_file(self, df_final, filename, sheet_name):
##	df = df_final[['data','valor']].iloc[1:6,]
##	df.to_excel(filename, sheet_name=sheet_name, index=False)
##df = x
##excel_reader = pd.ExcelFile('C:/Pasta1.xlsx')
##to_update = {"Plan1": df}
### Criar objeto para escrita
##excel_writer = pd.ExcelWriter('C:/Pasta1.xlsx')
## 
### Loop para o caso de querer trabalhar com mais de uma planilha
##for sheet in excel_reader.sheet_names:
##	sheet_df = excel_reader.parse(sheet)
##	append_df = to_update.get(sheet)
##	# Concatenar com o que já existia
##	if append_df is not None:
##		sheet_df = pd.concat([sheet_df, df]).drop_duplicates()
##	# Gravar no arquivo
##	sheet_df.to_excel(excel_writer, sheet, index=False)
### Salvar e fechar arquivo
##excel_writer.save()
##print(m)
##print(n)














































##import json
##import ast
##import pandas as pd
##import urllib
##import requests
##r = urllib.request.content('https://servicodados.ibge.gov.br/api/v2/censos/nomes/joao%7Cenzo')
##
##a = (json.loads(r))
##print(a)
##
##
####for p in data: a = str(p)
####for p in a['res']: b = str(p)
####print(b)
######dictionare = {'tags': data}
######a = (pd.DataFrame(dictionare['nome'].popitem()))
######a = str(a)
######a = a.replace('['and']'and,'')
######print (a)
