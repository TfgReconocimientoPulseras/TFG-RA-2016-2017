
# coding: utf-8

# In[1]:

import pandas as pd
import math


# In[2]:

#programa de prueba -> adaptar rutaaaaaaaaa
mis_datos = pd.read_csv("/home/daniel/Escritorio/user1-dancing-30s-1.csv", ";")    


# In[3]:

num_filas = len(mis_datos)
long_ventana = 1000 #1000ms
dif_timestamp = 32  #32 ms


# In[4]:

estadisticas_ventanas = pd.DataFrame()


# In[5]:

primer_timestamp = mis_datos.ix[0, 'timestamp']


# In[6]:

def obtener_estadisticas(ventana):
    est_ventana_aux = pd.DataFrame()
    
    media = pd.DataFrame(primera_ventana.mean())
    media.rename(index = {'gyro-alpha'   : 'media_gyro-alpha', 
                            'gyro-beta'  : 'media_gyro-beta',
                            'gyro-gamma' : 'media_gyro-gamma',
                            'accel-x'    : 'media_accel-x',
                            'accel-y'    : 'media_accel-y',
                            'accel-z'    : 'media_accel-z'
                           }, inplace = True)

    maximo = pd.DataFrame(primera_ventana.max())
    maximo.rename(index = {'gyro-alpha'  : 'maximo_gyro-alpha', 
                            'gyro-beta'  : 'maximo_gyro-beta',
                            'gyro-gamma' : 'maximo_gyro-gamma',
                            'accel-x'    : 'maximo_accel-x',
                            'accel-y'    : 'maximo_accel-y',
                            'accel-z'    : 'maximo_accel-z'
                           }, inplace = True)

    minimo = pd.DataFrame(primera_ventana.min())
    minimo.rename(index = {'gyro-alpha'  : 'minimo_gyro-alpha', 
                            'gyro-beta'  : 'minimo_gyro-beta',
                            'gyro-gamma' : 'minimo_gyro-gamma',
                            'accel-x'    : 'minimo_accel-x',
                            'accel-y'    : 'minimo_accel-y',
                            'accel-z'    : 'minimo_accel-z'
                           }, inplace = True)

    desviacion = pd.DataFrame(primera_ventana.std())
    desviacion.rename(index = {'gyro-alpha' : 'desviacion_gyro-alpha', 
                            'gyro-beta'  : 'desviacion_gyro-beta',
                            'gyro-gamma' : 'desviacion_gyro-gamma',
                            'accel-x'    : 'desviacion_accel-x',
                            'accel-y'    : 'desviacion_accel-y',
                            'accel-z'    : 'desviacion_accel-z'
                           }, inplace = True)

    
    est_ventana_aux = est_ventana_aux.append(media)
    est_ventana_aux = est_ventana_aux.append(maximo)
    est_ventana_aux = est_ventana_aux.append(minimo)
    est_ventana_aux = est_ventana_aux.append(desviacion)
    
    return est_ventana_aux.T


# In[7]:

fila_inicial = 0
fila_tope = long_ventana / dif_timestamp


# In[8]:

primera_ventana = mis_datos.ix[:(long_ventana / dif_timestamp), ['gyro-alpha', 'gyro-beta', 
                                                                 'gyro-gamma', 'accel-x', 
                                                                 'accel-y', 'accel-z']]
estadisticas_ventanas = obtener_estadisticas(primera_ventana)


# In[9]:

final = len(mis_datos.index) - 1
i = 0
while (fila_tope != final):
    
    aux = pd.DataFrame()
    
    fila_inicial = fila_tope - (dif_timestamp / 2)
    fila_inicial = math.floor(fila_inicial) #redondeo hacia abajo
    
    fila_tope = fila_tope + (dif_timestamp / 2)
    fila_tope = math.floor(fila_tope) #redondeo hacia abajo
    
    if(fila_tope > final):
        fila_tope = final
    
    primera_ventana = mis_datos.ix[fila_inicial:fila_tope, ['gyro-alpha', 'gyro-beta', 
                                                                 'gyro-gamma', 'accel-x', 
                                                                 'accel-y', 'accel-z']]
    
    aux = obtener_estadisticas(primera_ventana)
    estadisticas_ventanas = estadisticas_ventanas.append(aux, ignore_index=True)
    i = i + 1


# In[10]:

estadisticas_ventanas


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



