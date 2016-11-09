# Script python para extraccion y almacenamiento de características de los datos
## Uso
1. Ejecutar el script cargarDatos:
2. python cargarDatos.py user1-dancing-30s-1.csv (sin sep=;) archivoSegmentado.csv
3. Por defecto, ancho ventana=1s,solapamiento 50% y frecuencia 31.25Hz
4. En el archivo archivoSegmentado.csv tenemos la media, el máximo y el mínimo de los valores de cada ventana aplicada al archivo.
5. Para obtener información acerca del uso ejecutar en un consola: python cargarDatos.py -h
