import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from datetime import datetime
from visualizaciones import bar_char, hbar_char, scatter_char

# Define una paleta de colores personalizada
colores_personalizados = [
    '#1f77b4',  # Azul (frío, alto valor)
    '#00bfff',  # Celeste
    '#5dade2',  # Azul intermedio
    '#aec7e8',  # Azul claro
    '#17becf',  # Turquesa
    '#98df8a',  # Verde claro
    '#2ca02c',  # Verde
    '#bcbd22',  # Verde-amarillo
    '#ffd700',  # Amarillo
    '#ffbb78',  # Naranja claro
    '#ff7f0e',  # Naranja
    '#ff9896',  # Rosa claro
    '#ff1493',  # Fucsia
    '#d62728',  # Rojo
    '#c49c94',  # Marrón claro
    '#8c564b',  # Marrón
    '#9467bd',  # Violeta
    '#a55194',  # Violeta oscuro
    '#e377c2',  # Rosa
    '#f7b6d2',  # Rosa pálido
    '#c7c7c7',  # Gris claro
    '#7f7f7f',  # Gris
    '#393b79',  # Azul oscuro
    '#637939',  # Verde oliva
    '#8c6d31',  # Marrón oliva
    '#843c39',  # Marrón rojizo
    '#7b4173',  # Púrpura
    '#dbdb8d',  # Amarillo pálido
    '#9edae5'   # Celeste pálido
]
@st.cache_data(ttl=60)
def seccion(pregunta:str, df, _fig, informe:str):
    """
    Muestra una sección de visualización en Streamlit con pregunta, datos, gráfico y análisis.

    Parámetros:
        pregunta (str): Texto de la pregunta o título de la sección.
        df (DataFrame): DataFrame de pandas con los datos a mostrar.
        fig: Figura de Matplotlib o Plotly a mostrar.
        informe (str): Texto descriptivo o análisis del gráfico.

    Retorna:
        None. La función muestra los elementos en la interfaz de Streamlit.
    """
    import matplotlib.figure
    
    st.subheader(pregunta)
    st.dataframe(df)
    if isinstance(fig, matplotlib.figure.Figure):
        st.pyplot(fig)
    else:
        st.plotly_chart(fig, use_container_width=True)
    st.markdown(informe)
    st.divider()

st.title('Data Insider Proyect')

tab1, tab2, tab3 = st.tabs(['Cuestionario A','Cuestionario B', 'Visualizaciones Extra'])

with tab1:

    st.title('Cuestionario A')

    df_forbes_2022 = pd.read_csv('Data/forbes_2022.csv')

    pregunta = '¿Cuál es el Top 10 de países con más empresas en \
                Forbes para el periodo indicado?'


    top_paises_con_mas_empresas = df_forbes_2022.groupby(['Pais','Codigo'])['Empresa'].count().sort_values(ascending=False).head(10).reset_index()


    fig = bar_char(
        x='Pais',
        y='Empresa',
        hue='Pais',
        data=top_paises_con_mas_empresas,
        title='Top 10 de países con más empresas', 
        suptitle='Paises con mayor número de empresas Forbes Global', 
        xlabel='País',
        ylabel='Número de Empresas', 
        figsize=(15, 8), 
        rotation=25,
        n=10)


    informe = '''**Paises con mayor número de empresas Forbes Global (2022):**\n
    Este gráfico de barras muestra el Top 10 de países con la mayor cantidad de 
    empresas incluidas en el ranking Forbes Global del año 2022. Se observa que
    Estados Unidos lidera la lista con una cantidad significativamente mayor de
    empresas, seguido por China y Japón. Este gráfico resalta la concentración de
    grandes corporaciones a nivel global en estos países.'''

    seccion(pregunta, top_paises_con_mas_empresas, fig, informe)

    pregunta = '¿Cuál es el Top 4 de países con más empresas \
    en el área de tecnología y de telecomunicaciones?'

    top_paises_empresas_tech = df_forbes_2022.loc[(df_forbes_2022['Industria'] == 'Telecommunications Services') |
                                                (df_forbes_2022['Industria'] == 'Technology Hardware & Equipment')].groupby(['Pais','Codigo'])[('Empresa')].count().sort_values(ascending=False).head(4).reset_index()


    fig = bar_char(
        x='Pais',
        y='Empresa',
        hue='Pais',
        data=top_paises_empresas_tech,
        title='Top 4 de países con más empresas Tech', 
        suptitle='Paises con mayor número de empresas en la industria\n tecnológica y telecomunicaciones en el año 2022', 
        xlabel='País',
        ylabel='Número de Empresas', 
        figsize=(15, 8),
        n=.5)




    informe = '''**Paises con mayor número de empresas en la industria tecnológica y telecomunicaciones (2022):**\n
    Este gráfico de barras presenta el Top 4 de países con la mayor cantidad de 
    empresas en las áreas de tecnología y telecomunicaciones según el ranking 
    Forbes Global 2022. Similar al ranking general, Estados Unidos y China ocupan
    los primeros lugares, lo que indica su dominio en estas industrias estratégicas.
    Japón y Taiwan también figuran en este top, mostrando su relevancia en el sector
    tecnológico.'''

    seccion(pregunta, top_paises_empresas_tech, fig, informe)

    pregunta = '¿Cuál fue el margen de pérdida de las 5 empresas que presentaron mayores perjuicios considerando el total de pérdidas \
    registradas en la Industria de los Hoteles, Restaurantes y entretenimiento?'

    top_empresas_margen_perdida = df_forbes_2022.loc[df_forbes_2022['Industria'] == 'Hotels, Restaurants & Leisure' ].groupby(['Empresa'])['Margen_de_rentabilidad (%)'].mean().sort_values().head(5).reset_index()


    fig = bar_char(
        x='Empresa',
        y='Margen_de_rentabilidad (%)',
        hue='Empresa',
        data=top_empresas_margen_perdida,
        title='Top 5 de países con mayor margen de perdida',
        suptitle='Grafico del top paises con el mayor margen de perdida\n en la Industria de los Hoteles, Restaurantes y entretenimiento?',
        xlabel='Empresa',
        ylabel='Margen de rentabilidad (%)',
        figsize=(15, 8),
        pallete='Reds_r',
        n=8,
        symbol='%'
    )

    informe = '''**Margen de Rentabilidad de las Empresas en la Industria de Hoteles, Restaurantes y Entretenimiento (2022):**\n
    Este gráfico de barras muestra el margen de rentabilidad de las 5 empresas con
    mayores pérdidas en la industria de Hoteles, Restaurantes y Entretenimiento en
    el ranking Forbes Global 2022. Se observa que Carnival Corporation presentó el 
    mayor margen de pérdida, seguido por Las Vegas Sands y Caesars Entertainment.
    Esto refleja el impacto negativo que enfrentaron estas empresas en el año 2022.'''

    seccion(pregunta, top_empresas_margen_perdida, fig, informe)

    pregunta = 'Considerando a la Industria Petrolera en Asia,\
                ¿Cuál o cuáles empresas superaron en más del 20% su margen de rentabilidad?'

    margen_rentabilidad_Asia = df_forbes_2022.loc[(df_forbes_2022['Industria'] == 'Oil & Gas Operations') &
                                                (df_forbes_2022['Continente'] == 'Asia')].groupby(['Empresa'])['Margen_de_rentabilidad (%)'].mean().sort_values(ascending=False).head(7).reset_index()

    margen_rentabilidad_Asia.loc[margen_rentabilidad_Asia['Empresa'] == 'Saudi Arabian Oil Company (Saudi Aramco)', 'Empresa'] = 'Saudi Aramco'


    fig = bar_char(
        x='Empresa',
        y='Margen_de_rentabilidad (%)',
        hue='Empresa',
        data=margen_rentabilidad_Asia,
        title='Empresas que superaron más del 20% su margen de rentabilidad',
        suptitle='Margen de Rentabilidad de la Industria Petrolera en Asia',
        xlabel='Empresa',
        ylabel='Margen de rentabilidad (%)',
        figsize=(15, 8),
        pallete='inferno',
        n=1,
        symbol='%'
    )


    informe = '''**Margen de Rentabilidad de la Industria Petrolera en Asia (2022):**\n
    Este gráfico de barras presenta las empresas de la industria petrolera en Asia
    que superaron en más del 20% su margen de rentabilidad según el ranking 
    Forbes Global 2022. Empresas como Novatek, Surgutneftegas y CNOOC destacan con
    altos márgenes de rentabilidad, lo que sugiere un año favorable para estas 
    compañías en el sector petrolero asiático.'''

    seccion(pregunta, margen_rentabilidad_Asia, fig, informe)

    pregunta = '¿Cuáles fueron las empresas norteamericanas con el mayor porcentaje de rentabilidad por industria?'

    empresas_NA_top_rentabilidad = df_forbes_2022.loc[(df_forbes_2022['Continente'] == 'North America')].groupby(['Industria'])[['Empresa','Margen_de_rentabilidad (%)']].max().sort_values(ascending=False, by='Margen_de_rentabilidad (%)').reset_index()


    fig = hbar_char(
        x='Margen_de_rentabilidad (%)',
        y='Empresa',
        hue='Industria',
        data=empresas_NA_top_rentabilidad,
        title='Empresas con mayor margen de rentabilidad por industria',
        suptitle='Margen de Rentabilidad de las Empresas por Industria en Norte America (2022)',
        xlabel='Margen de rentabilidad (%)',
        ylabel='Empresa',
        figsize=(15, 8),
        pallete=colores_personalizados,
        legend=True,
        n=3,
        symbol='%'
    )


    informe = '''**Margen de Rentabilidad de las Empresas por Industria en Norte América (2022):**\n
    Este gráfico de barras horizontal exhibe las empresas norteamericanas con el 
    mayor porcentaje de rentabilidad por industria en el ranking Forbes Global 2022.
    Se puede observar la diversidad de industrias representadas y cómo empresas 
    individuales dentro de cada sector lograron altos márgenes de rentabilidad en 
    Norteamérica durante este año.'''

    seccion(pregunta, margen_rentabilidad_Asia, fig, informe)

    pregunta = 'Excluyendo a la industria Bancaria,\
    ¿Cuáles fueron las empresas europeas con mayores \
    pérdidas registradas por industria a nivel global?'

    empresas_EU_top_perdidas = df_forbes_2022.loc[(df_forbes_2022['Continente'] == 'Europe') &
                                                (df_forbes_2022['Industria'] != 'Banking')].groupby('Industria')[['Empresa','Ganancias']].min().sort_values(by='Ganancias').reset_index()

    fig = hbar_char(
        x='Ganancias',
        y='Empresa',
        hue='Industria',
        data=empresas_EU_top_perdidas.head(),
        title='Empresas con mayores perdidas por industria (Excluyendo la bancaria)',
        suptitle='Mayores perdidas generadas a nivel global por empresas europeas (2022)',
        xlabel='Margen de rentabilidad (%)',
        ylabel='Empresa',
        figsize=(15, 8),
        pallete='Reds_r',
        legend=True,
        n=400,
        symbol='$'
    )

    informe = '''**Mayores pérdidas generadas a nivel global por empresas europeas (2022):** \n
    Este gráfico de barras horizontal ilustra las empresas europeas 
    (excluyendo la industria bancaria) que registraron las mayores 
    pérdidas a nivel global en el ranking Forbes Global 2022.
    BT Group en telecomunicaciones y Aena en transporte se destacan
    con las mayores pérdidas, lo que indica desafíos significativos
    en estos sectores para las empresas europeas.'''

    seccion(pregunta, empresas_EU_top_perdidas, fig, informe)


    Pregunta = '¿Cuál fue la distribución de Ingresos y Activos con respecto a las ganancias\
                de los bancos cuyos activos no superan los 300000 millones de dólares?'

    bancos_dist_activos_ingresos = df_forbes_2022.loc[(df_forbes_2022['Industria'] == 'Banking') &
                                                    (df_forbes_2022['Activos'] <= 300000), ['Ingresos','Activos','Ganancias']]

    fig = scatter_char(
        data=bancos_dist_activos_ingresos,
        x='Ingresos',
        y='Activos',
        size='Ganancias',
        hue='Ganancias',
        sizes=(10, 200),
        title='Distribución de Ingresos y Activos con respecto a las ganancias\n cuyos activos no superan los 300000$ Millones',
        suptitle='Ingresos y Activos con respecto a las ganancias de los bancos (2022)',
        xlabel='Ingresos (en millones de dólares)',
        ylabel='Activos (en millones de dólares)',
        figsize=(15, 8))

    informe = '''Se observa que, en general, a mayor nivel de activos e ingresos,
                las ganancias tienden a incrementarse, aunque existen bancos con 
                altos ingresos y activos relativamente bajos. Esto permite identificar
                bancos eficientes y posibles outliers en el sector.'''

    seccion(pregunta, bancos_dist_activos_ingresos, fig, informe)

    pregunta = 'Considerando el histórico de valores de las acciones en el año 2022 de las 5 empresas de tu elección, \
    Indica ¿Cuál fue la mejor semana para comprar y cuál para vender respectivamente?'

    df_polygon = pd.read_csv('Data/datos_polygon.csv', parse_dates=['Fecha'])

    df_polygon_semanal = pd.read_csv('Data/polygon_semanal.csv', parse_dates=['Fecha'])

    mejor_semana_compra = df_polygon_semanal.loc[df_polygon_semanal.groupby('Symbol')['Precio_Cierre_Promedio'].idxmin()]

    mejor_semana_venta = df_polygon_semanal.loc[df_polygon_semanal.groupby('Symbol')['Precio_Cierre_Promedio'].idxmax()]

    fig = px.line(df_polygon, x='Fecha', y='Precio_Cierre', color='Symbol',
                title=f'Precio de cierre diario de las acciones<br>{df_polygon["Symbol"].unique()}',
                labels={'Precio_Cierre': 'Precio de Cierre'}, width=1500, height=500)

    fig.add_trace(go.Scatter(x=mejor_semana_venta['Fecha'], y=mejor_semana_venta['Precio_Cierre_Promedio'],
                            mode='markers', name='Mejor semana venta', marker=dict(size = 7,color='blue'),
                            hovertext=[f"Simbolo: {row['Symbol']}<br>Fecha: {row['Fecha'].strftime('%d-%m-%Y')}<br>Semana: {row['Semana']}<br>Precio: {row['Precio_Cierre_Promedio']:.2f}$"
                                        for index, row in mejor_semana_venta.iterrows()],
                            hoverinfo='text'))
    fig.add_trace(go.Scatter(x=mejor_semana_compra['Fecha'], y=mejor_semana_compra['Precio_Cierre_Promedio'],
                            mode='markers', name='Mejor semana compra', marker=dict(size = 7,color='green'),
                            hovertext=[f"Simbolo: {row['Symbol']}<br>Fecha: {row['Fecha'].strftime('%d-%m-%Y')}<br>Semana: {row['Semana']}<br>Precio: {row['Precio_Cierre_Promedio']:.2f}$"
                                        for index, row in mejor_semana_compra.iterrows()],
                            hoverinfo='text'))

    informe = '''**Informe del Gráfico: Precio de cierre diario de las acciones (2024):**\n
        Este gráfico de líneas interactivo muestra el precio de cierre diario de
        las acciones de las cinco empresas seleccionadas (NTDOF, EA, KONMY, SQNXF,
        UBSFF) a lo largo del año 2024. Se han añadido marcadores para indicar la
        "mejor semana para comprar" (precio mínimo semanal) en verde y la
        "mejor semana para vender" (precio máximo semanal) en azul para cada empresa,
        según los datos históricos de valores.\n
        Mejores Semanas para Comprar:\n
        EA: Semana 16, Fecha 2024-04-15, Precio de Cierre Promedio: 126.56
        KONMY: Semana 1, Fecha 2024-01-04, Precio de Cierre Promedio: 26.04
        NTDOF: Semana 17, Fecha 2024-04-22, Precio de Cierre Promedio: 48.29
        SQNXF: Semana 25, Fecha 2024-06-17, Precio de Cierre Promedio: 28.81
        UBSFF: Semana 49, Fecha 2024-12-02, Precio de Cierre Promedio: 12.23\n
        Mejores Semanas para Vender:\n
        EA: Semana 49, Fecha 2024-12-02, Precio de Cierre Promedio: 166.74
        KONMY: Semana 39, Fecha 2024-09-25, Precio de Cierre Promedio: 49.50
        NTDOF: Semana 50, Fecha 2024-12-09, Precio de Cierre Promedio: 60.45
        SQNXF: Semana 8, Fecha 2024-02-21, Precio de Cierre Promedio: 44.67
        UBSFF: Semana 7, Fecha 2024-02-16, Precio de Cierre Promedio: 26.09'''

    seccion(pregunta, df_polygon_semanal, fig, informe)

with tab2:

    st.title('Cuestionario B')

    df_forbes_2015_2022 = pd.read_csv('Data/forbes_2015_2022.csv')

    pregunta = '¿Cuál es el Top 10 de países con más empresas en Forbes para el periodo indicado?'

    top_paises_empresas_15_22 = df_forbes_2015_2022.groupby(['Pais','Codigo'])['Empresa'].count().sort_values(ascending=False).head(10).reset_index()

    fig = bar_char(
        x='Pais',
        y='Empresa',
        hue='Pais',
        data=top_paises_empresas_15_22,
        title='Top 10 paises con más empresas', 
        suptitle='Cantidad de empresas por pais en el periodo 2015-2022', 
        xlabel='País',
        ylabel='Número de Empresas', 
        figsize=(15, 8), 
        rotation=10,
        n=75)

    informe = '''**Informe del Gráfico: Cantidad de empresas por país en el periodo 2015-2022:**\n
    Este gráfico de barras presenta el Top 10 de países con la mayor cantidad
    de empresas incluidas en el ranking Forbes Global durante el periodo 2015-2022.
    De manera consistente con el año 2022, Estados Unidos, China y Japón mantienen
    su liderazgo en la concentración de grandes empresas a lo largo de estos años.'''

    seccion(pregunta, top_paises_empresas_15_22, fig, informe)

    pregunta = '¿Cuál es el Top 5 de países con más empresas en el área de tecnología y de telecomunicaciones?'

    top_paises_empresas_tech_15_22 = df_forbes_2015_2022.loc[(df_forbes_2015_2022['Industria'] == 'Telecommunications Services') |
                                                            (df_forbes_2015_2022['Industria'] == 'Technology Hardware & Equipment')].groupby(['Pais','Codigo'])['Empresa'].count().sort_values(ascending=False).head(5).reset_index()

    fig = bar_char(
        x='Pais',
        y='Empresa',
        hue='Pais',
        data=top_paises_empresas_tech_15_22,
        title='Top 5 de países con más empresas Tech', 
        suptitle='Cantidad de empresas del Área de tecnología y telecomunicaciones\n por pais en el periodo 2015-2022', 
        xlabel='País',
        ylabel='Número de Empresas', 
        figsize=(15, 8),
        n=2)

    informe = '''**Informe del Gráfico: Cantidad de empresas del área de\n
    tecnología y telecomunicaciones por país en el periodo 2015-2022:
    Este gráfico de barras muestra el Top 5 de países con la mayor cantidad
    de empresas en las áreas de tecnología y telecomunicaciones en el ranking
    Forbes Global durante el periodo 2015-2022. Estados Unidos y China siguen
    siendo los principales actores, seguidos por Taiwan y Japón, lo que subraya
    su continua importancia en estos sectores a lo largo del tiempo.'''

    seccion(pregunta, top_paises_empresas_tech_15_22, fig, informe)

    pregunta = '¿Cuál fue el margen de pérdida de las 10 empresas que presentaron mayores perjuicios considerando\
                el total de pérdidas registradas en la Industria de los Hoteles, Restaurantes y entretenimiento?'

    top_perdidas_empresas_HRE = df_forbes_2015_2022.loc[df_forbes_2015_2022['Industria'] == 'Hotels, Restaurants & Leisure'].groupby(['Empresa'])['Ganancias'].sum().sort_values().head(10).reset_index()
    colores = ['green' if v >= 0 else 'red' for v in top_perdidas_empresas_HRE['Ganancias']]

    fig = bar_char(
        x='Empresa',
        y='Ganancias',
        hue='Empresa',
        data=top_perdidas_empresas_HRE,
        title='Top 10 Empresas con mayor margen de perdidas',
        suptitle='Grafico del margen de perdida de las empresas del Hoteles, Restaurantes y Entretenimiento\n en el periodo 2015-2022',
        xlabel='Empresa',
        ylabel='Margen de Rentabilidad',
        figsize=(15, 8),
        pallete='coolwarm',
        rotation=15,
        n=200,
        symbol='$'
    )

    informe = '''**Informe del Gráfico: Margen de pérdida de las empresas de la industria de
    Hoteles, Restaurantes y Entretenimiento en el periodo 2015-2022:**\n
    Este gráfico de barras visualiza el margen de pérdida de las 10 empresas
    con mayores perjuicios en la industria de Hoteles, Restaurantes y Entretenimiento
    durante el periodo 2015-2022. Carnival Corporation y Royal Caribbean Group
    muestran las mayores pérdidas acumuladas en este sector a lo largo de los
    años indicados.'''

    seccion(pregunta, top_perdidas_empresas_HRE, fig, informe)

    pregunta = 'Considerando a la Industria Petrolera en las Américas,\
                ¿Cuál o cuáles empresas superaron en más del 20% la rentabilidad de sus activos?'

    top_empresas_ROA = df_forbes_2015_2022.loc[((df_forbes_2015_2022['Continente'] == 'North America') |
                                                                (df_forbes_2015_2022['Continente'] == 'South America')) &
                                                                ((df_forbes_2015_2022['Industria'] == 'Oil & Gas Operations'))].groupby(['Empresa'])['ROA (%)'].mean().round(2).sort_values(ascending=False).reset_index()

    top_empresas_ROA = top_empresas_ROA.loc[top_empresas_ROA['ROA (%)'] >= 20]

    fig = bar_char(
        x='Empresa',
        y='ROA (%)',
        hue='Empresa',
        data=top_empresas_ROA,
        title='Empresas que tienen un ROA superior al 20%',
        suptitle='Rentabilidad de activos en Empresas Americanas de\n la industria petrolera en el periodo 2015-2022',
        xlabel='Empresa',
        ylabel='Rentabilidad de Activos (%)',
        figsize=(15, 8),
        pallete='inferno',
        n=1,
        symbol='%'
    )

    informe = '''**Informe del Gráfico: Rentabilidad de activos en Empresas
    Americanas de la industria petrolera en el periodo 2015-2022:**\n
    Este gráfico de barras presenta las empresas americanas de la industria
    petrolera que tuvieron una rentabilidad de activos (ROA) superior al 20%
    en promedio durante el periodo 2015-2022. Weatherford International y Whitecap
    Resources destacan con un ROA promedio superior a este umbral, indicando una 
    gestión eficiente de sus activos para generar ganancias.'''

    seccion(pregunta, top_empresas_ROA, fig, informe)

    pregunta = '¿Cuáles fueron las empresas europeas con el mayor porcentaje de rentabilidad por industria?'

    empresas_EU_top_rentabilidad = df_forbes_2015_2022.loc[df_forbes_2015_2022['Continente'] == 'Europe'].groupby('Industria')[['Empresa','Margen_de_rentabilidad (%)']].max().sort_values(by='Margen_de_rentabilidad (%)',ascending=False).reset_index()

    fig = hbar_char(
        x='Margen_de_rentabilidad (%)',
        y='Industria',
        hue='Empresa',
        data=empresas_EU_top_rentabilidad,
        title='Empresas con mayor margen de rentabilidad por industria',
        suptitle='Margen de Rentabilidad de las Empresas por Industria en Europa\n durante el periodo 2015-2022',
        xlabel='Margen de rentabilidad (%)',
        ylabel='Industria',
        figsize=(15, 8),
        pallete=colores_personalizados,
        legend=True,
        n=3,
        symbol='%'
    )

    informe = '''**Informe del Gráfico: Margen de Rentabilidad de las Empresas
    por Industria en Europa durante el periodo 2015-2022:**\n
    Este gráfico de barras horizontal exhibe el margen de rentabilidad
    de las empresas europeas con el mayor porcentaje de rentabilidad por
    industria durante el periodo 2015-2022. Se observa la diversidad de 
    industrias y las empresas líderes en rentabilidad dentro de cada sector
    en Europa a lo largo de estos años.'''

    seccion(pregunta, empresas_EU_top_rentabilidad, fig, informe)

    preguntas = '¿Cuáles fueron las 10 empresas norteamericanas con\
                mayores pérdidas registradas por industria a nivel global?'

    empresas_NA_top_perdidas = df_forbes_2015_2022.loc[df_forbes_2015_2022['Continente'] == 'North America'].groupby('Industria')[['Empresa','Ganancias']].min().sort_values(by='Ganancias').head(10).reset_index()

    fig = bar_char(
        x='Empresa',
        y='Ganancias',
        hue='Industria',
        data=empresas_NA_top_perdidas,
        title='Top 10 empresas con mayores perdidas',
        suptitle='Margen de Perdidas de las Empresas Norteamericanas por Industria\n durante el periodo 2015-2022',
        xlabel='Empresa',
        ylabel='Perdidas',
        figsize=(15, 8),
        legend=True,
        n=500,
        symbol='$'
    )

    informe = '''**Informe del Gráfico: Margen de Perdidas de las Empresas
    Norteamericanas por Industria durante el periodo 2015-2022:**\n
    Este gráfico de barras muestra las 10 empresas norteamericanas
    con las mayores pérdidas registradas por industria a nivel global
    durante el periodo 2015-2022. Empresas en sectores como
    Oil & Gas Operations, Conglomerates y Transportation figuran
    entre las que experimentaron mayores pérdidas en este periodo.'''

    seccion(preguntas, empresas_NA_top_perdidas, fig, informe)


    pregunta = '¿Cuál fue la distribución de Ingresos y Activos con respecto\
                a las ganancias de los bancos cuyos activos no superan los 150000 millones de dólares?'

    bancos_dist_activos_ingresos_15_22 = df_forbes_2015_2022.loc[(df_forbes_2015_2022['Industria'] == 'Banking') &
                                                    (df_forbes_2015_2022['Activos'] <= 150000), ['Ingresos','Activos','Ganancias']].reset_index(drop=True)

    fig = scatter_char(
        data = bancos_dist_activos_ingresos_15_22,
        x='Ingresos',
        y='Activos',
        size='Ganancias',
        hue='Ganancias',
        sizes=(10, 200),
        title='Distribución de Ingresos y Activos con respecto a las ganancias\n cuyos activos no superan los 150000 millones de dólares',
        suptitle='Distribución de Ingresos y Activos con respecto a las ganancias de los bancos (2022)',
        xlabel='Ingresos (en millones de dólares)',
        ylabel='Activos (en millones de dólares)',
        figsize=(15, 8)
    )

    informe = '''Se puede observar un crecimiento en los ingresos
    a medida que los activos superan los 50000 millones de dólares
    alcanzando hasta 15000 millones de dolares. tambien se puede
    observar algunos datos con activos menores a 50000 millones
    presentando ingresos muy elevados. Sin embargo, no se aprecia
    un aumento significativo en las ganancias'''

    seccion(pregunta, bancos_dist_activos_ingresos_15_22, fig, informe)


with tab3:

    st.title('Visualizaciones Extra')

    df_valor_mercado_industria = df_forbes_2015_2022.groupby(['Industria','Ano'])[['Valor_de_mercado']].sum().reset_index()

    st.subheader('Valor de mercado por industria a lo largo de los años')

    st.dataframe(df_valor_mercado_industria)

    st.video('Data/valor_mercado_industria.mp4')


    st.divider()


    st.subheader('Empleados por industria a lo largo de los años')

    df_empleados_industria = pd.read_csv('Data/forbes_empleados.csv')

    st.dataframe(df_empleados_industria)

    st.video('Data/Empleados_por_industria.mp4')

    st.divider()

    pregunta = 'Ventas Globales por País (2022)'

    df_ventas_globales = pd.read_csv('Data/ventas_globales.csv')

    fig = px.choropleth(df_ventas_globales, locations="Codigo",
                        color="Ingresos",
                        hover_name="Pais",
                        hover_data={'Ingresos':':.2f'},
                        color_continuous_scale=px.colors.sequential.Inferno,
                        title='Total de Ventas Globales x País (2022)')

    Informe = '''Segun los datos, podemos observar que la mayoria de los paises
    se mantienen con ventas globales por debajo de los 100000 millones 
    de dolares, mientras China y Estados Unidos se destacan con ventas
    por encima de los 800000 millones de dolares y 1400000 millones de 
    dolares respectivamente.'''

    seccion(pregunta, df_ventas_globales, fig, Informe)