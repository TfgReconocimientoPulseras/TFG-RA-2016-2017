# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 12:37:33 2016

@author: veronica
"""

import pandas as pd

#calcularMedidas("user1-dancing-30s-1.csv","salida.csv",30)
def calcularMedidas(archivoEntrada,archivoSalida,freq):
    df= pd.read_csv(archivoEntrada,';',index_col='timestamp')
    i=0
    tiempos=list()
   
    while True:
        tiempos.insert(i,pd.Timestamp(df.index[i]))
        i=i+1
        if(i>=len(df)):
            break
    df.index=tiempos
  
    media= df.rolling(freq).mean()
    maximo= df.rolling(freq).max()
    minimo= df.rolling(freq).min()
    
   
    print(media)
    media.to_csv(archivoSalida)



if __name__ == "__main__":
    archivoEntrada="user1-dancing-30s-1.csv"
    archivoSalida="salida.csv"
    freq='1s'
    calcularMedidas(archivoEntrada,archivoSalida,freq)
    
    
    
    
    