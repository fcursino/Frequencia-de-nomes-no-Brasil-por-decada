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



xm = (pd.DataFrame.from_dict(enzo['res'],))
ym = (pd.DataFrame.from_dict(joao['res'],))

xf = (pd.DataFrame.from_dict(leticia['res'],))
yf = (pd.DataFrame.from_dict(maria['res'],))


print(xm)
print(ym)
print(xf)
print(yf)
















































