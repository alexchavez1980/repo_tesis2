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
color = ['green', 'blue','red','cyan', 'magenta', 'yellow','k','w']
#-----------------------------------------------------------------------
# # Funciones
#-----------------------------------------------------------------------
def to_df(no_df):
    df = pd.DataFrame(no_df) 
    df['sample'] = df.index                                             # Le agrego la columna sample del index para graficarlo.
    return df

# Función para graficar los ocho canales de un .mat DISTINTO al ERP.
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
    plt.axis((0,360000,-300,300))                                              
    plt.grid()
    plt.savefig(dir_savefig)
    plt.show()
    return()    

# Función para graficar los ocho canales del ERP.
def grafic_8cherp(data_frame, titulo, xlabel, ylabel, dir_savefig):     
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
    plt.axis((0,250,-8,8))                                              
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


def grafic_1ch(data_frame, titulo, xlabel, ylabel, dir_savefig, canal): # Función para graficar canales por separado. Con 'sample'.
    plt.figure(figsize=(30,8))                                          # UN canal.
    axes = plt.gca()                                                    # Acá no hay for. OJO.    
    plt.plot(data_frame['sample'], data_frame[canal], color[0])
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

def grafic_1chzoom(data_frame, titulo, xlabel, ylabel, dir_savefig, canal): # Misma que grafic_1ch pero haciendo zoom
    plt.figure(figsize=(30,8))                                          # UN canal.
    axes = plt.gca()                                                    # Acá no hay for. OJO.    
    plt.plot(data_frame['sample'], data_frame[canal], color[1])
    axes.set_title(titulo)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.title.set_size(30)
    axes.xaxis.label.set_size(20)
    axes.yaxis.label.set_size(20)
    plt.axis((140000,150000,-80,70))
    plt.grid()
    plt.savefig(dir_savefig)
    plt.show()

def grafic_1chzoomPRUEBA(data_frame, titulo, xlabel, ylabel, dir_savefig, canal, xmin,xmax,ymin,ymax): # Misma que grafic_1ch pero haciendo zoom
    plt.figure(figsize=(30,8))                                          # UN canal.
    axes = plt.gca()                                                    # Acá no hay for. OJO.    
    plt.plot(data_frame['sample'], data_frame[canal], color[1])
    axes.set_title(titulo)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.title.set_size(30)
    axes.xaxis.label.set_size(20)
    axes.yaxis.label.set_size(20)
    plt.axis((xmin,xmax,ymin,ymax))
    plt.grid()
    plt.savefig(dir_savefig)
    plt.show()


def sumemos(a,b,c):                                                     # Función de prueba. Nada mas.
    d = a+b+c
    return d    
#----------------------------------------------------------------------
# Algunas funciones extra que uso. EN LA MIRA DE SER BORRADAS
#----------------------------------------------------------------------
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