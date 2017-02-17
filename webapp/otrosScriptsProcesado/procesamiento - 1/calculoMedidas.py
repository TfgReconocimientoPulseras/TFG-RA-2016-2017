# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 12:37:33 2016

@author: veronica
"""

import pandas as pd
import matplotlib.pyplot as plt

#calcularMedidas("user1-dancing-30s-1.csv","salida.csv")
def calcularMedidas(archivoEntrada,archivoSalida):
    df= pd.read_csv(archivoEntrada,';',index_col='timestamp')
    i=0
    tiempos=list()
   
    while True:
        tiempos.insert(i,pd.Timestamp(int(df.index[i]*1000)))
        
        i=i+1
        if(i>=len(df)):
            break
    df.index=tiempos
    media = pd.DataFrame()
    maximo=pd.DataFrame()
    minimo=pd.DataFrame()
    desviacion=pd.DataFrame()
   
    maximo=df.resample('500u').max().rolling('1000u').max()
    
    plt.figure('maximo')
    plt.legend(["gyro-alpha","gyro-beta","gyro-gamma","accel-x","accel-y","accel-z"], loc="upper right")
    plt.plot(maximo)
    
    minimo=df.resample('500u').min().rolling('1000u').min()
    plt.legend(["gyro-alpha","gyro-beta","gyro-gamma","accel-x","accel-y","accel-z"], loc="upper right")
    plt.figure('mimimo')
    plt.plot(minimo)
    media=df.resample('500u').mean().rolling('1000u').mean()
    plt.legend(["gyro-alpha","gyro-beta","gyro-gamma","accel-x","accel-y","accel-z"], loc="upper right")
    plt.figure('media')
    plt.plot(media)
    desviacion=df.resample('500u').std().rolling('1000u').std()
    plt.legend(["gyro-alpha","gyro-beta","gyro-gamma","accel-x","accel-y","accel-z"], loc="upper right")
    plt.figure('desviacion')
    plt.plot(desviacion)
     
    mediaNoSegementado = df.resample('500u').mean()
   
  
    media.to_csv(archivoSalida)
  
    mediaNoSegementado.to_csv("r")
   










if __name__ == "__main__":
    archivoEntrada="user1-dancing-30s-1.csv"
    archivoSalida="salida.csv"
  
    calcularMedidas(archivoEntrada,archivoSalida)
    
    
    