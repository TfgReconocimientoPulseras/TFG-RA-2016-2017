
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

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

primera_ventana = mis_datos.ix[:(long_ventana / dif_timestamp), ['gyro-alpha', 'gyro-beta', 
                                                                 'gyro-gamma', 'accel-x', 
                                                                 'accel-y', 'accel-z']]


# In[7]:

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


# In[9]:

estadisticas_ventanas = estadisticas_ventanas.append(media)
estadisticas_ventanas = estadisticas_ventanas.append(maximo)
estadisticas_ventanas = estadisticas_ventanas.append(minimo)
estadisticas_ventanas = estadisticas_ventanas.append(desviacion)


# In[11]:

estadisticas_ventanas

