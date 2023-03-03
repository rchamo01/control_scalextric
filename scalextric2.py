import pandas as pd
import os

name = 'Scalextric.xlsx'
count = 0
archivos = os.listdir()
for i in archivos:
  if i == name:
    count = 1
if count == 0:
  df = pd.DataFrame(columns=['Jugador', 'Coche', 'NVueltas', 'Tiempo', 'Media'])
  df.to_excel(name)
df = pd.read_excel(name)
df.drop(columns= ['Unnamed: 0'], inplace = True)

jugadores = {}
x, y = '', ''
while (1):
    print('Introduce un jugador y su coche. f para finalizar')
    x = input()
    if x == 'f':
        break
    y = input()
    jugadores[x] = y
    

aux = pd.DataFrame(columns = df.columns)
aux['Jugador'] = jugadores.keys()
aux['Coche'] = jugadores.values()
df = pd.concat([df,aux], sort = True)

pista1, pista2 = {}, {}
for i in range(len(df['Jugador'])):
    j1, j2 = '', ''
    t1, t2 = '', ''
    n1, n2 = '', ''
    print('Pista 1')
    j1 = input()
    print('Tiempo')
    t1 = input()
    print('NVueltas')
    n1 = input()
    print('Pista 2')
    j2 = input()
    print('Tiempo2')
    t2 = input()
    print('NVueltas2')
    n2 = input()
    pista1[j1] = [j2, t1, n1]
    pista1[j2] = [j1, t2, n2]
    
print(pista1, pista2)