
import os.path 

import csv

#segmentamos el archivo y guardamos cada segmento en un csv
def segmentar(nombreArchivo):
  
    actividad=nombreArchivo.split('_')
    actividad=actividad[1]
    
    archivo = open(nombreArchivo)
    lectura = csv.reader(archivo,delimiter=';')
    datos = list(lectura)
    directorioActual=os.getcwd()
  
    os.makedirs( "datosSegmentados", 0777 );
    os.chdir(directorioActual+"\datosSegmentados")
    numeroSegmento=0
    i=3;
    cont=2
    while True:
        inicio=datos[cont][0]    
        while True:
            if(float(datos[i][0]) - float(inicio) >=1000):
                j=cont               
                cont=(i+cont)/2;
                numeroSegmento=numeroSegmento+1
                archivoSalida = open("s"+str(numeroSegmento)+"_"+actividad+".csv","w")
                segmento=csv.writer(archivoSalida,lineterminator='\n')
                while True:
                    segmento.writerow(datos[j])
                    j=j+1
                    if(j>=i):
                        archivoSalida.close()
                        break
                break
            else:
               i=i+1
        i=cont+1;
        if(cont>len(datos)-cont):
          os.chdir(directorioActual)
          break
       
  
  #A partir de la segmentacion anterior,cargamos los csv segmentados y calculamos distintas medidas     
def calcular(nombreArchivo):
    import csv
    import numpy as np
   
    
    numeroSegmento=1
    
    actividad=nombreArchivo.split('_')
    actividad=actividad[1]
    
    mediaSalida = open("media.csv","w")
    media=csv.writer(mediaSalida,lineterminator='\n')
    
    varianzaSalida = open("varianza.csv","w")
    varianza=csv.writer(varianzaSalida,lineterminator='\n')
    
    desviacionSalida = open("deviacion.csv","w")
    desviacion=csv.writer(desviacionSalida,lineterminator='\n')
    
    maximoSalida = open("maximo.csv","w")
    maximo=csv.writer(maximoSalida,lineterminator='\n')
    
    minimoSalida = open("minimo.csv","w")
    minimo=csv.writer(minimoSalida,lineterminator='\n')
    directorioActual=os.getcwd()    
    os.chdir(directorioActual+"\datosSegmentados")
    while True:
       
        datos = np.loadtxt("s"+str(numeroSegmento)+"_"+actividad+".csv", delimiter = ',')
        media1=list(np.median(datos,axis=0))
        desviacion1=list(np.std(datos,axis=0))
        varianza1=list(np.var(datos,axis=0))
        minimo1=list(np.amin(datos,axis=0))
        maximo1=list(np.amax(datos,axis=0))
        
        #añadimos la actividad que se realiza
        
        media1.append(actividad)
        desviacion1.append(actividad)
        varianza1.append(actividad)
        minimo1.append(actividad)
        maximo1.append(actividad)
        #añadimos el numero de ventana
        media1.insert(0,numeroSegmento)
        desviacion1.insert(0,numeroSegmento)
        varianza1.insert(0,numeroSegmento)
        minimo1.insert(0,numeroSegmento)
        maximo1.insert(0,numeroSegmento)
       
      
        media.writerow(media1)    
       
        varianza.writerow(varianza1)        
        
        desviacion.writerow(desviacion1)
       
        maximo.writerow(maximo1)       
       
        minimo.writerow(minimo1)
        numeroSegmento=numeroSegmento+1
        if not(os.path.exists("s"+str(numeroSegmento)+"_"+actividad+".csv")):         
            break
        
        
        
    
    mediaSalida.close()
    varianzaSalida.close()
    desviacionSalida.close()
    maximoSalida.close()
    minimoSalida.close()
    
def analizarDatos(nombreArchivo):
    segmentar(nombreArchivo)
    calcular(nombreArchivo)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    