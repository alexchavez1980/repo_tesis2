#-----------------------------------------------------------------------
# Librerías
#-----------------------------------------------------------------------
import mne                                                              # pip install mne
mne.set_log_level('WARNING')                                            # Luego averiguar ¿para qué?
import scipy.io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb                                                    # Por ahora lo voy a usar para cambiar los nombres de las columnas
color = ['green', 'blue','red','cyan', 'magenta', 'yellow','k','w']     # Paleta de colores para diferenciar las ondas
#-----------------------------------------------------------------------
# Mis funciones
#-----------------------------------------------------------------------
def to_df(no_df):
    df = pd.DataFrame(no_df) 
    df['sample'] = df.index
    return df

def grafico(data_frame, titulo, xlabel, ylabel, dir_savefig):
    plt.figure(figsize=(30,8))
    axes = plt.gca()
    for i in range(0,7):
        plt.plot(data_frame['index'], data_frame[i], color[i])
    axes.set_title(titulo)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.title.set_size(30)
    axes.xaxis.label.set_size(20)
    axes.yaxis.label.set_size(20)
    plt.axis((0,350000,-1700,2000))                                     #plt.axis((eje_ploteo))
    plt.grid()
    plt.savefig(dir_savefig)
    plt.show()
    return()    

def sumemos(a,b,c):
    d = a+b+c
    return d    
#-----------------------------------------------------------------------