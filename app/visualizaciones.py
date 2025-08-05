

def bar_char(x:str, y:str, hue:str, data, title:str, suptitle:str, xlabel:str, ylabel:str, 
             figsize=(10, 6), pallete:str='inferno', legend:bool=False, rotation:int=0, n:int=0, symbol:str=''):
    """
    Crea un gráfico de barras vertical personalizado usando Seaborn y Matplotlib.

    Parámetros:
        n (int): Valor a sumar al valor de la barra para mostrar encima de ella. Por defecto 0.
        x (str): Nombre de la columna para el eje X.
        y (str): Nombre de la columna para el eje Y.
        hue (str): Nombre de la columna para agrupar por color.
        data (DataFrame): DataFrame de pandas con los datos a graficar.
        title (str): Título secundario del gráfico.
        suptitle (str): Título principal del gráfico.
        xlabel (str): Etiqueta del eje X.
        ylabel (str): Etiqueta del eje Y.
        rotation (int, opcional): Rotación de las etiquetas del eje X. Por defecto 0.
        figsize (tuple, opcional): Tamaño de la figura (ancho, alto). Por defecto (10, 6).
        pallete (str, opcional): Paleta de colores de Seaborn. Por defecto 'inferno'.
        legend (bool, opcional): Si se muestra la leyenda. Por defecto False.
    symbol (str): Símbolo a mostrar junto al valor de la barra. Por defecto vacío.

    Retorna:
        fig (matplotlib.figure.Figure): Objeto figura de Matplotlib listo para mostrar en Streamlit.
    """
    

    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    fig = plt.figure(figsize=figsize)

    ax = sns.barplot(x=x, y=y,data=data, hue=hue, palette=pallete, legend=legend)

    plt.suptitle(suptitle, fontsize=18, y=1.01, ha='center')
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.xticks(fontsize=12, rotation=rotation)
    plt.ylabel(ylabel, fontsize=14)
    plt.yticks(fontsize=12)
    ax.set_yticklabels([])
    sns.despine(left=True,bottom=True)
    ax.tick_params(left=False, bottom=False)

    for i,j in enumerate(data[y]):
        ax.text(i,j-n if j < 0 else j+n,str(j) + symbol,color='black',fontsize=12,ha='center',va='center')

    return fig


def hbar_char(x:str, y:str, hue:str, data, title:str, suptitle:str, xlabel:str, ylabel:str, 
             figsize=(10, 6), pallete:str='inferno', legend:bool=False, rotation:int=0, n:int=0, symbol:str=''):
    """
    Crea un gráfico de barras horizontal personalizado usando Seaborn y Matplotlib.

    Parámetros:
        x (str): Nombre de la columna para el eje X (valor numérico).
        y (str): Nombre de la columna para el eje Y (categoría).
        hue (str): Nombre de la columna para agrupar por color.
        data (DataFrame): DataFrame de pandas con los datos a graficar.
        title (str): Título secundario del gráfico.
        suptitle (str): Título principal del gráfico.
        xlabel (str): Etiqueta del eje X.
        ylabel (str): Etiqueta del eje Y.
        rotation (int, opcional): Rotación de las etiquetas del eje Y. Por defecto 0.
        figsize (tuple, opcional): Tamaño de la figura (ancho, alto). Por defecto (10, 6).
        pallete (str, opcional): Paleta de colores de Seaborn. Por defecto 'inferno'.
        legend (bool, opcional): Si se muestra la leyenda. Por defecto False.
        n (int): Valor a sumar al valor de la barra para mostrar encima de ella. Por defecto 0.
        symbol (str): Símbolo a mostrar junto al valor de la barra. Por defecto vacío.

    Retorna:
        fig (matplotlib.figure.Figure): Objeto figura de Matplotlib listo para mostrar en Streamlit.
    """
    

    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    fig = plt.figure(figsize=figsize)


    ax = sns.barplot(x=x, y=y, hue=hue, data=data, orient='h', palette=pallete, legend=legend)

    plt.suptitle(suptitle, fontsize=18)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.yticks(fontsize=12)
    ax.set_xticklabels([])
    ax.tick_params(left=False, bottom=False)
    sns.despine(left=True,bottom=True)
    if legend:
        ax.legend(bbox_to_anchor=(1.25,-0.05), bbox_transform=ax.transAxes,
                  fontsize=10, loc='lower right', title='Industria')

    for i,j in enumerate(data[x]):
        ax.text(j+n,i,str(j) + symbol,color='black',fontsize=12,ha='center',va='center')

    return fig


def scatter_char(xlabel:str, ylabel:str, data, x:str, y:str, size:str=None, sizes:tuple=None, hue:str=None, title:str='', suptitle:str='',
                 figsize=(10, 6), palette:str='inferno_r', legend:bool=True):
    
    import matplotlib.pyplot as plt
    import seaborn as sns


    fig, ax = plt.subplots(figsize=figsize)

    sns.scatterplot(x=x, y=y, data=data, size=size,  sizes=sizes, palette=palette, hue=hue, legend=legend)

    plt.suptitle(suptitle, fontsize=18, y=1.02)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.yticks(fontsize=12)
    plt.xticks(fontsize=12)

    if legend:
        ax.legend(bbox_to_anchor=(1.2,-0.05), bbox_transform=ax.transAxes,
                  fontsize=10, loc='lower right', title=size if size else hue)

    ax.tick_params(left=False, bottom=False)

    return fig