import pandas as pd
import argparse


#inputFile - Nombre del archvivo del que leer los datos
#outputFile - Nombre del archivo de salida
#time - Tiempo de la ventana (Por defecto 1s)
#freq - Frecuencia de recogida de los datos (Datos de ejemplo = 31.25Hz)
#overlap - Solapamiento entre ventanas (Por defecto solapamiento 50%)

def getStatisticsValues(inputFile, outputFile, time=1, freq=31.25, overlap=0.5):
    df = pd.read_csv(inputFile, ';')

    windowsz = time * freq  # Ancho de la ventana
    step = int(windowsz * overlap)

    dfMean = pd.DataFrame()
    dfMin = pd.DataFrame()
    dfMax = pd.DataFrame()

    for i in range(0, len(df.index), step):
        dfMean[i] = df.ix[i:i + windowsz, 1:].mean()  # Media
        dfMin[i] = df.ix[i:i + windowsz, 1:].min()  # Min
        dfMax[i] = df.ix[i:i + windowsz, 1:].max()  # Max

    dfMean = dfMean.append(dfMin)
    dfMean = dfMean.append(dfMax)

    dfMean = dfMean.T  # Traspuesta para cambiar los nombres a las columnas
    dfMean.columns = ['avg_gyro-alpha', 'avg_gyro-beta', 'avg_gyro-gamma', 'avg_ax', 'avg_ay', 'avg_az',
                    'min_gyro-alpha', 'min_gyro-beta', 'min_gyro-gamma', 'min_ax', 'min_ay', 'min_az',
                    'max_gyro-alpha', 'max_gyro-beta', 'max_gyro-gamma', 'max_ax', 'max_ay', 'max_az']  # Renombrado de columnas

    dfMean.T.to_csv(outputFile, ';')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract features from inputFile and save them in outputFile')

    parser.add_argument("i",
                        help="File to be analyzed")
    parser.add_argument("o",
                        help="Output file")
    parser.add_argument("-t", "--time", help="Time of window, i.e.= 1 second",
                    default=1)
    parser.add_argument("-f", "--freq", help="Frequency, i.e.= 31.25 Hz",
                    default=31.25)
    parser.add_argument("-p", "--perc", help="overlap, i.e. = 0.5 -> 50 Overlap",
                    default=0.5)
    args = parser.parse_args()
    #print args.i
    #print args.o
    #print args.time
    #print args.freq
    #print args.perc
    getStatisticsValues(args.i, args.o, args.time, args.freq, args.perc)
