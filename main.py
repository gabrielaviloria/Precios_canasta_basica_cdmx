import tabula
import pandas as pd
from decouple import config

ruta_pdf = config('RUTA_PDF')
tables = tabula.read_pdf(
    ruta_pdf,
    pages = '2-3',
    multiple_tables = True,
    lattice= True,
    stream = True,
    guess = False,
    pandas_options= {"header": None}
)
 
df = tables[1].dropna(axis = 0, how = 'all')
df = df.drop(range(0,2))
n = 1
columns = [0]
for i in range(8):
    if n < 7:
        df[[f'{n}.2',f'{n}.3']] =df[n].str.split(r'[ \r]', n = 1, expand = True)
    else:
        df[f'{n}.2'] = df[n] 
        df[f'{n}.3'] = 'CEDA'
    if n % 2 == 1 :
        tipo_costo = 'Bajo'
    else:
        tipo_costo = 'alto'
    df[f'{n}.1'] = tipo_costo
    columns.extend([f'{n}.1',f'{n}.2',f'{n}.3'])
    n += 1
df = df.drop(df.columns[1:n], axis = 1)
#columns.extend([9])
df = df[columns]

print(df.columns)