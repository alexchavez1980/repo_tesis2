#-----------------------------------------------------------------------
# Librerías y algunas variables
#-----------------------------------------------------------------------
import mne                                                              # pip install mne
mne.set_log_level('WARNING')                                            # Luego averiguar ¿para qué?
import scipy.io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb                                                    # Por ahora lo voy a usar para cambiar los nombres de las columnas#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
# # Funciones
#-----------------------------------------------------------------------
def to_df(no_df):
    df = pd.DataFrame(no_df) 
    df['sample'] = df.index                                             # Le agrego la columna sample del index para graficarlo.
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

# Función para graficar los ocho canales.
def grafic_8ch(data_frame, titulo, xlabel, ylabel, dir_savefig):     
    plt.figure(figsize=(30,8))                                          
    axes = plt.gca()                                                    
    for i in range(0,7):
        plt.plot(data_frame['sample'], data_frame[i], color[i])
    axes.set_title(titulo)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.title.set_size(30)
    axes.xaxis.label.set_size(20)
    axes.yaxis.label.set_size(20)
    plt.axis((0,250,-4,7))                                              #plt.axis((eje_ploteo))
    plt.grid()
    plt.savefig(dir_savefig)
    plt.show()
    return()      

# Función para graficar UN canal del p300-subject-25.mat, que a su vez se le extrae el p300subject25['data'][0][0][0].
def grafic_signal(data_frame, titulo, xlabel, ylabel, dir_savefig, canal):          
    plt.figure(figsize=(30,8))                                          
    axes = plt.gca()
    plt.plot(data_frame['sample'], data_frame[canal], color[1])
    axes.set_title(titulo)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.title.set_size(30)
    axes.xaxis.label.set_size(20)
    axes.yaxis.label.set_size(20)
    plt.axis((0,350000,-80,70))
    plt.grid()
    plt.savefig(dir_savefig)
    plt.show()


def grafic_1ch(data_frame, titulo, xlabel, ylabel, dir_savefig, canal):          # Función para graficar canales por separado. Con 'index'
    plt.figure(figsize=(30,8))                                          # Acá no hay for. OJO.
    axes = plt.gca()
    plt.plot(data_frame['index'], data_frame[canal], color[1])
    axes.set_title(titulo)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.title.set_size(30)
    axes.xaxis.label.set_size(20)
    axes.yaxis.label.set_size(20)
    plt.axis((0,350000,-80,70))
    plt.grid()
    plt.savefig(dir_savefig)
    plt.show()

def sumemos(a,b,c):
    d = a+b+c
    return d    


#----------------------------------------------------------------------
# Algunas funciones extra que uso.
#----------------------------------------------------------------------
def grafico1(data_frame, titulo, xlabel, ylabel, dir_savefig):          # Función para graficar los ocho canales. Con 'index'
    plt.figure(figsize=(30,8))                                          # Se usa para signal, tirals o flash, que vienen de mat['data'][0][0][X] 
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

def grafico2(data_frame, titulo, xlabel, ylabel, dir_savefig):          # Función para graficar los ocho canales. Con 'Sample'
    plt.figure(figsize=(30,8))                                          # Se usa para erptemplate, que es mat['routput'].
    axes = plt.gca()                                                    # Revisar ¿por qué?
    for i in range(0,7):
        plt.plot(data_frame['sample'], data_frame[i], color[i])
    axes.set_title(titulo)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.title.set_size(30)
    axes.xaxis.label.set_size(20)
    axes.yaxis.label.set_size(20)
    plt.axis((0,250,-4,7))                                              #plt.axis((eje_ploteo))
    plt.grid()
    plt.savefig(dir_savefig)
    plt.show()
    return()   
#-----------------------------------------------------------------------