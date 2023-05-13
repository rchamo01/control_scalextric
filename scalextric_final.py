# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
#import threading
import PySimpleGUI as sg
from datetime import datetime

name = 'Scalextric.xlsx'
#df.drop(columns= ['Unnamed: 0'], inplace = True)

df = pd.DataFrame(columns=['Fecha', 'Jugador', 'Coche', 'NVueltas', 'Tiempo', 'Media', 'VRapida'])

sg.theme('Dark Grey 13')

layout = [[sg.Text('Nuevo Piloto', size =(14, 1)), sg.Text('',key='pantalla', size =(15, 1)), sg.Text('', key='pant', size =(15, 1))],
          [sg.Input(size =(15, 1)), sg.Text('', key = 'pantalla2', size =(15, 1)), sg.Text('', key='pant2', size =(15, 1))],
          [sg.Text('Coche', size =(14, 1)), sg.Text('', key='pantalla3', size =(15, 1)), sg.Text('', key='pant3', size =(15, 1))],
          [sg.Input(size =(15, 1)), sg.Text('', key='pantalla4', size =(15, 1)), sg.Text('', key='pant4', size =(15, 1))],
          [sg.OK(), sg.Cancel()]]

window = sg.Window('Scalextric', layout)

jugadores = {}
j=1
while (1):
    event, v = window.read()
    #print(event)
    if event in (sg.WIN_CLOSED, 'Cancel'):
        window.close()
        break
    if event == 'OK':
        jugadores[v[0]] = v[1]
        if j == 1:
            window['pantalla'].update(list(jugadores.keys())[-1])
            window['pant'].update(list(jugadores.values())[-1])
            j +=1
        elif j == 2:
            window['pantalla'].update(list(jugadores.keys())[-1])
            window['pant'].update(list(jugadores.values())[-1])
            window['pantalla2'].update(list(jugadores.keys())[-2])
            window['pant2'].update(list(jugadores.values())[-2])
            j +=1
        elif j == 3:
            window['pantalla'].update(list(jugadores.keys())[-1])
            window['pant'].update(list(jugadores.values())[-1])
            window['pantalla2'].update(list(jugadores.keys())[-2])
            window['pant2'].update(list(jugadores.values())[-2])
            window['pantalla3'].update(list(jugadores.keys())[-3])
            window['pant3'].update(list(jugadores.values())[-3])
            j +=1
        elif j == 4:
            window['pantalla'].update(list(jugadores.keys())[-1])
            window['pant'].update(list(jugadores.values())[-1])
            window['pantalla2'].update(list(jugadores.keys())[-2])
            window['pant2'].update(list(jugadores.values())[-2])
            window['pantalla3'].update(list(jugadores.keys())[-3])
            window['pant3'].update(list(jugadores.values())[-3])
            window['pantalla4'].update(list(jugadores.keys())[-4])
            window['pant4'].update(list(jugadores.values())[-4])
            j = 1

aux = pd.DataFrame(columns=df.columns)
now = datetime.now()
aux['Jugador'] = jugadores.keys()
aux['Coche'] = jugadores.values()
aux['Fecha'] = str(now.day) + '/' + str(now.month) + '/' + str(now.year)
df = pd.concat([df,aux], sort = True)

def comb (n):
    return n*n-n

asignacion = {}
j = 0
for i in df['Jugador']:
    asignacion[i] = [j, len(df['Jugador']) + j]
    j += 1
    
numeroVueltas = np.zeros([len(df['Jugador']), 2*len(df['Jugador'])])
vueltaRapida = np.zeros([len(df['Jugador']), 2*len(df['Jugador'])])
tiempoV = np.zeros([len(df['Jugador']), 2*len(df['Jugador'])])

enfrentamientos = []

layout2 = [[sg.Text('Piloto1', size =(45, 1)), sg.Text('Piloto2', size =(15, 1))],
          [sg.InputText(size =(45, 1), key='val1'), sg.InputText(size =(15, 1), key='val2')],
           [sg.Text('Tiempo p1', size =(15, 1)), sg.Text('nVueltas p1', size =(15, 1)), sg.Text('vRapida p1', size =(15, 1)), 
            sg.Text('Tiempo p2', size =(15, 1)), sg.Text('nVueltas p2', size =(15, 1)), sg.Text('vRapida p2', size =(15, 1))],
           [sg.InputText(size =(16, 1), key='t1'), sg.InputText(size =(16, 1), key='n1'), sg.InputText(size =(16, 1), key='v1'), 
            sg.InputText(size =(16, 1), key='t2'), sg.InputText(size =(16, 1), key='n2'), sg.InputText(size =(16, 1), key='v2')],
          [sg.Text('Introduce los pilotos, numero de vueltas, tiempo y vuelta rapida', key='pantalla')],
          [sg.OK(), sg.Button('Datos'), sg.Cancel()]]

window2 = sg.Window('Competicion', layout2, margins=(10, 10))

def mostrar_datos():
    fig, ax = plt.subplots()
    plt.title('tiempo por vuelta')
    ax.imshow(tiempoV)
    fig2, ax2 = plt.subplots()
    plt.title('numero de vueltas')
    ax2.imshow(numeroVueltas)
    fig3, ax3 = plt.subplots()
    plt.title('vuelta mas rapida')
    ax3.imshow(numeroVueltas)
    xlabs = list(asignacion.keys()) + list(asignacion.keys())
    ylabs = list(asignacion.keys())
    # Agregar las etiquetas
    ax.set_xticks(np.arange(len(xlabs)), labels = xlabs)
    ax.set_yticks(np.arange(len(ylabs)), labels = ylabs)
    ax2.set_xticks(np.arange(len(xlabs)), labels = xlabs)
    ax2.set_yticks(np.arange(len(ylabs)), labels = ylabs)
    ax3.set_xticks(np.arange(len(xlabs)), labels = xlabs)
    ax3.set_yticks(np.arange(len(ylabs)), labels = ylabs)
    # Agregar los valores a cada celda
    for i in range(len(xlabs)):
        for j in range(len(ylabs)):
            text = ax.text(i, j, tiempoV[j,i],
                        ha = "center", va = "center", color = "w")
    for i in range(len(xlabs)):
        for j in range(len(ylabs)):
            text = ax2.text(i, j, numeroVueltas[j,i],
                        ha = "center", va = "center", color = "w")
    for i in range(len(xlabs)):
        for j in range(len(ylabs)):
            text = ax3.text(i, j, vueltaRapida[j,i],
                        ha = "center", va = "center", color = "w")
    plt.show()
    
    
def insertar_datos():
    i = comb(len(df['Jugador']))
    print(i)
    while i > 0:
        event, v = window2.read()
        window2['pantalla'].update('Cambio'+str(i))
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break     
        if event == 'Datos':
            mostrar_datos()
            continue
        if event == 'OK':
            j1 = v['val1']
            if j1 not in list(df['Jugador']):
                window2['pantalla'].update('Jugador no registrado')
                continue
            j2 = v['val2']
            if j2 not in list(df['Jugador']):
                window2['pantalla'].update('Jugador no registrado')
                continue
            if j1+j2 in enfrentamientos:
                window2['pantalla'].update('Este enfrentamientos ya se ha realizado')
                continue
            ################################################################
            if numeroVueltas[asignacion[j1][0], asignacion[j2][0]] == 0:
                numeroVueltas[asignacion[j1][0], asignacion[j2][0]] = float(v['n1'])
            else:
                numeroVueltas[asignacion[j1][0], asignacion[j2][1]] = float(v['n1'])
            ################################################################
            if numeroVueltas[asignacion[j2][0], asignacion[j1][0]] == 0:
                numeroVueltas[asignacion[j2][0], asignacion[j1][0]] = float(v['n2'])
            else:
                numeroVueltas[asignacion[j2][0], asignacion[j1][1]] = float(v['n2'])
            ################################################################
            if tiempoV[asignacion[j1][0], asignacion[j2][0]] == 0:
                tiempoV[asignacion[j1][0], asignacion[j2][0]] = float(v['t1'])
            else:
                tiempoV[asignacion[j1][0], asignacion[j2][1]] = float(v['t1'])
            ################################################################
            if tiempoV[asignacion[j2][0], asignacion[j1][0]] == 0:
                tiempoV[asignacion[j2][0], asignacion[j1][0]] = float(v['t2'])
            else:
                tiempoV[asignacion[j2][0], asignacion[j1][1]] = float(v['t2'])
            ################################################################
            if vueltaRapida[asignacion[j1][0], asignacion[j2][0]] == 0:
                vueltaRapida[asignacion[j1][0], asignacion[j2][0]] = float(v['v1'])
            else:
                vueltaRapida[asignacion[j1][0], asignacion[j2][1]] = float(v['v1'])
            ################################################################
            if vueltaRapida[asignacion[j2][0], asignacion[j1][0]] == 0:
                vueltaRapida[asignacion[j2][0], asignacion[j1][0]] = float(v['v2'])
            else:
                vueltaRapida[asignacion[j2][0], asignacion[j1][1]] = float(v['v2'])
            ################################################################
            enfrentamientos.append(j1+j2)
            print(enfrentamientos)
        i -= 1
    window2.close()
    
insertar_datos()
mostrar_datos()

def sumar (matriz):
    suma = []
    for i in range(matriz.shape[0]):
        suma.append(matriz[i].sum())
    return suma

def buscarMaximo (matriz):
    suma = sumar(matriz)
    return list(asignacion.keys())[suma.index(max(suma))]

def minimo (matriz):
    minim = []
    matriz.sort()
    for i in range(matriz.shape[0]):
        minim.append(min(matriz[i][2:]))
    return minim

def buscarMenor (matriz):
    minim = minimo(matriz)
    return list(asignacion.keys())[minim.index(min(minim))]

def buscarMinimo(matriz):
    suma = sumar(matriz)
    return list(asignacion.keys())[suma.index(min(suma))]

sg.popup('Ganador por Numero Vueltas', buscarMaximo(numeroVueltas), 'Vueltas totales de cada jugador', list(asignacion.keys()), sumar(numeroVueltas))
sg.popup('Ganador por Tiempos', buscarMinimo(tiempoV), 'Tiempos totales de cada jugador:', list(asignacion.keys()), sumar(tiempoV))
sg.popup('Vuelta Rapida', buscarMenor(vueltaRapida), 'Vueltas Rapidas de cada jugador:', list(asignacion.keys()), minimo(vueltaRapida))

df.index = df['Jugador']
for i in asignacion.keys():
    df.iloc[df.index.get_indexer([i]), df.columns.get_indexer(["NVueltas"])] = numeroVueltas[asignacion[i][0]].sum()
    df.iloc[df.index.get_indexer([i]), df.columns.get_indexer(["Tiempo"])] = tiempoV[asignacion[i][0]].sum()
    df.iloc[df.index.get_indexer([i]), df.columns.get_indexer(["Media"])] = numeroVueltas[asignacion[i][0]].mean()
    df.iloc[df.index.get_indexer([i]), df.columns.get_indexer(["VRapida"])] = sorted(vueltaRapida[asignacion[i][0]])[2]
    
print(df)
#sg.popup(df.columns, df.values)
#df.to_excel(name)

count = 0
archivos = os.listdir()
for i in archivos:
  if (i == name):
    count = 1
if (count == 0):
  df_new = pd.DataFrame(columns=['Fecha', 'Jugador', 'Coche', 'NVueltas', 'Tiempo', 'Media', 'VRapida'])
  df_new.to_excel(name)
df_new = pd.read_excel(name)

df_new = pd.concat([df_new,aux], sort = True)
df_new.to_excel(name)

