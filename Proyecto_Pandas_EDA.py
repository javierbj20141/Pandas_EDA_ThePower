# %% [markdown]
# Las conclusiones y los gráficos derivados del análisis de las diferentes variables se indican en el archivo: "Informe explicativo del análisis_proyecto librería Pandas"
# 

# %% [markdown]
# Transoformación, Limpieza de datos, y análisis general

# %%
pip install matplotlib ##instalamos matplotlib para la visualización

# %%
pip install seaborn ##instalamos seaborn para la visualización

# %%
import pandas as pd ##importamos pandas como "pd"
import numpy as np ##importamos numpy como "np" 
import matplotlib.pyplot as plt ##importamos matplotlib como "plt"
import seaborn as sns ##importamos seaborn como "sns" 

# %%
pip install openpyxl ##indicamos esto para abrir archivos excel

# %%
##asignamos variables a cada archivo, y hacemos que muestre todas sus columnas aunque haya que hacer scroll
general_clientes = pd.read_csv('c:\\Users\\jbartolomej\\Desktop\\Especialización\\Data\\Pyhton_librerias\\Proyecto_Pandas\\bank-additional.csv',sep=',')
clientes_2012 = pd.read_excel('c:\\Users\\jbartolomej\\Desktop\\Especialización\\Data\\Pyhton_librerias\\Proyecto_Pandas\\customer-details.xlsx',sheet_name="2012")
clientes_2013 = pd.read_excel('c:\\Users\\jbartolomej\\Desktop\\Especialización\\Data\\Pyhton_librerias\\Proyecto_Pandas\\customer-details.xlsx',sheet_name="2013")
clientes_2014 = pd.read_excel('c:\\Users\\jbartolomej\\Desktop\\Especialización\\Data\\Pyhton_librerias\\Proyecto_Pandas\\customer-details.xlsx',sheet_name="2014")
pd.set_option('display.max_columns',None)
copia_DF_1 = general_clientes.copy()
copia_DF_2 = clientes_2012.copy()
copia_DF_3 = clientes_2013.copy()
copia_DF_4 = clientes_2014.copy()

# %%
clientes_2012.info()##del archivo de clientes de 2012, 5 columnas son de tipo int, 1 de formato fecha y otra object
clientes_2012.isnull().sum()##no tiene valores nulos
clientes_2012.duplicated().sum()##no tiene duplicadas
clientes_2012.describe().T## trasponemos para verlo mejor
clientes_2012["ID"].count() ##el DF de clientes 2012 tiene 20115 registros

# %%
clientes_2013.info()##del archivo de clientes de 2013, 5 columnas son de tipo int, 1 de formato fecha y otra object
clientes_2013.isnull().sum()##no tiene valores nulos
clientes_2013.duplicated().sum()##no tiene duplicadas
clientes_2013.describe().T
clientes_2013.shape## el DF de clientes 2013 tiene 8965 registros

# %%
clientes_2014.info()##del archivo de clientes de 2012, 5 columnas son de tipo int, 1 de formato fecha y otra object
clientes_2014.isnull().sum()##no tiene valores nulos
clientes_2014.duplicated().sum()##no tiene duplicadas
clientes_2014.describe().T## trasponemos para verlo mejor
clientes_2014["ID"].count() ##el DF de clientes 2012 tiene 14090 registros

# %%
##como los tres archivos son iguales, siendo la principal diferencia la del año de registro, vamos a juntarlos
clientes_2012_2013_2014 = pd.concat([clientes_2014,clientes_2013,clientes_2012],axis=0,join="outer")


# %%
##eliminamos la columna de numeración que no tiene nombre
clientes_2012_2013_2014.drop("Unnamed: 0",axis=1,inplace=True)

# %%
##añado una columna llamada "Year become Client" al lado de la fecha, que indique el año solo, para poder hacer el análisis por años mejor.
clientes_2012_2013_2014.insert(4,"Year become Client",clientes_2012_2013_2014["Dt_Customer"].dt.year)


# %%
##Cambiamos los datos de la columna salario a float para no confundirlos con el resto de datos numericos
clientes_2012_2013_2014["Income"] = clientes_2012_2013_2014 ["Income"].apply(lambda e: float(e))

# %%
##hacemos el mismo ejercicio que con los anteriores DF, para analizar un poco su forma, estructura, duplicados, etc.
general_clientes.info()
general_clientes.isnull().sum()##vemos que hay algunas columnas con valores nulos
general_clientes.duplicated().sum()##vemos que no hay filas duplicadas
general_clientes.describe().T##la edad mínima es 17, la maxima 98 y la media cerca de 40
general_clientes.shape## 43.000 filas y 24 columnas
(general_clientes["default"] ==1).sum()##solo hay 3 clientes que tienen historial de impagos
(general_clientes["pdays"] ==999).sum()##más de 40.000 clientes que indica 999 dias.
(general_clientes["previous"] ==0).sum() ##clientes contactados por primera vez
(general_clientes["days since last contact"] ==999).sum()##clientes que ya han pasado mas de 999 días

# %%
general_clientes.drop("Unnamed: 0",axis=1,inplace=True) ##eliminamos columna que no nos da información

# %%
def minúsculas (texto):##creamos una funcion que pase a str y luego ponga el texto en minuscula, para homogeneizar los datos
    cambio = str(texto)
    retorno = cambio.lower()
    return retorno

general_clientes["marital"] = general_clientes["marital"].apply(minúsculas)
general_clientes["poutcome"] = general_clientes["poutcome"].apply(lambda t:t.lower())


# %%
general_clientes.rename(columns={"y":"product_subscription"},inplace=True)##cambiamos el nombre de una columna para hacerlo mas intuitivo

# %%
def convert_float (numero):
    reemplazo = numero.replace(",",".")
    flo = float(reemplazo)
    return flo

general_clientes ["cons.conf.idx"] = general_clientes ["cons.conf.idx"].apply(convert_float) ##pasamos a float la columna de indice de confianza del consumidor

# %%
def convert_float_no_NaN (numero):
    if pd.isna(numero):
        return numero
    reemplazo = numero.replace(",",".")
    flo = float(reemplazo)
    return flo

general_clientes["cons.price.idx"] = general_clientes["cons.price.idx"].apply(convert_float_no_NaN)##ahora pasamos la de indice de precios, ignornado los Nulos

# %%
general_clientes["euribor3m"] = general_clientes["euribor3m"].apply(convert_float_no_NaN)##hacemos lo mismo con la del euribor

# %%
def convert_int (numero):
    reemplazo = numero.replace(",","")[:-1]
    inter = int(reemplazo)
    return inter

general_clientes["nr.employed"]= general_clientes["nr.employed"].apply(convert_int)## ahora lo hacemos para la columna de empleado, ya que no tiene sentido los decimales

# %%
def convert_int_no_NaN(numero):
    if pd.isna(numero):
        return numero
    try:
        return int(float(numero))  
    except ValueError:
        return numero

general_clientes["age"] = general_clientes["age"].apply(convert_int_no_NaN).astype("Int64")## convertimos la edad a int, ya que no nos importan los decimales.

# %%
##cambiamos el nombre de estás columnas para mayor claridad
general_clientes.rename(columns={"default":"payment default"},inplace=True)
general_clientes.rename(columns={"duration":"last interaction duration"},inplace=True)
general_clientes.rename(columns={"campaign":"contacts made in this campaign"},inplace=True)
general_clientes.rename(columns={"pdays":"days since last contact"},inplace=True)
general_clientes.rename(columns={"previous":"previously contacted?"},inplace=True)
general_clientes.rename(columns={"poutcome":"previous campaign outcome"},inplace=True) 
general_clientes.rename(columns={"nr.employed":"number of employees"},inplace=True) 

# %%
def categoria_edades (edad): ## el objetivo es categorizar la columna de edad para facilitr el analisis. Utilizamos el metodo insert para que no quede al final.
    if pd.isna(edad):
        return "desconocido"  
    if edad >=0 and edad <= 18:
        return "menor de edad"
    elif edad >=19 and edad <=30:
        return "adultos jóvenes"
    elif edad >=31 and edad <= 50:
        return "adultos"
    elif edad >=51 and edad <=68:
        return "adultos mayores"
    elif edad > 68:
        return "personas mayores"

general_clientes["edad_categoria"] = general_clientes["age"].apply(categoria_edades)
columna_edad_categoria_mover = general_clientes.pop("edad_categoria")
general_clientes.insert(1,"edad_categoria",columna_edad_categoria_mover)


# %%
def entero (numero): ##El objetivo es cambiar en las 3 columnas e tipo de dato a entero, para hacerlo más manejable, y dejando los nulos sin tocar
    if pd.isna(numero):
        return numero
    return int(numero)

general_clientes["housing"] = general_clientes["housing"].apply(entero).astype("Int64")
general_clientes["payment default"] = general_clientes["payment default"].apply(entero).astype("Int64")
general_clientes["loan"] = general_clientes["loan"].apply(entero).astype("Int64")

    

# %%
general_clientes["date"].isna().sum()##hay 248 fechas en las que se realizó la interacción con el cliente, nulas

# %%
meses_español = {'enero': '01',
    'febrero': '02',
    'marzo': '03',
    'abril': '04',
    'mayo': '05',
    'junio': '06',
    'julio': '07',
    'agosto': '08',
    'septiembre': '09',
    'octubre': '10',
    'noviembre': '11',
    'diciembre': '12'}##creamos un diccionario, para luego iterar por el y sacar columnas de meses

# %%
def convertir_fecha(fecha_str):## evitamos los nulos, y hacemos que los nombres de los meses se cambien a numeros, y devuelve el resultado en formato datetime
    if pd.isna(fecha_str):
        return pd.NaT
    for nombre_mes, numero_mes in meses_español.items():
        if nombre_mes in fecha_str:
            fecha_str = fecha_str.replace(nombre_mes, numero_mes)
            break
    return pd.to_datetime(fecha_str, format='%d-%m-%Y',errors="coerce")

general_clientes["date_dt"] = general_clientes["date"].apply(convertir_fecha)##creamos la nueva columna en formato datetime
general_clientes["contact_month"] = general_clientes["date_dt"].dt.month##creamos otra con los meses
general_clientes["contact_year"] = general_clientes["date_dt"].dt.year##creamos otra con los años

# %%
general_clientes["date_dt"].isna().sum()##sigue habiendo 248 fechas nulas en la nueva columna ya con formato datetime

# %%
##los cambiamos a Int64 para no afectar a los nulos
general_clientes["contact_month"] = general_clientes["contact_month"].astype("Int64")
general_clientes["contact_year"] = general_clientes["contact_year"].astype("Int64")

# %%
##elimnamos y cambiamos nombre a más columnas para mayor claridad
general_clientes.rename(columns={"edad_categoria":"age category"},inplace=True)
general_clientes.drop("date",axis=1,inplace=True)
general_clientes.rename(columns={"date_dt":"contact_date"},inplace=True)


# %%
def category_duration (duracion):##categorizamos la duración de la última interacción del cliente
    if pd.isna(duracion):
        return duracion
    if duracion >= 0.0 and duracion <= 60.0:
        return "Interacción corta"
    elif duracion >= 61.0 and duracion <= 150.0:
        return "Interacción media"
    elif duracion >= 151.0 and duracion <= 300.0:
        return "Interacción larga"
    elif duracion >=301.0:
        return "Interacción muy larga"
    
general_clientes.insert(10,"last interaction duration category",general_clientes["last interaction duration"].apply(category_duration))##insertamos columna después de la duración
    

# %%
general_clientes.rename(columns={"id_":"ID"},inplace=True)##para hacer el merge, cambiamos el nombre de la columna ID para dejarlo igual


# %%
general_clientes["ID"].count()

# %%
clientes_2012_2013_2014["ID"].count()

# %%
df_merged_general = general_clientes.merge(clientes_2012_2013_2014,how="inner",on="ID")##aqui unimos solo valores coincidentes de ID. Salen 43.000 registros
df_merged_clientes = clientes_2012_2013_2014.merge(general_clientes,how="left",on="ID")##aqui unimos todos los valores de clientes, y los coincidentes de general. Usaremos este para no dejar clientes fuera.



# %% [markdown]
# Análisis por salario

# %%
##media de salario según categoria de edades
df_merged_clientes.groupby("age category") ["Income"].mean().reset_index().sort_values(by="Income",ascending=True)
##raro porque todas son muy parecidas menos la de menor de edad. Veremos por que.
(df_merged_clientes["age category"]=="menor de edad").sum()##hay 33 menores de edad
df_merged_clientes[(df_merged_clientes["age category"] == "menor de edad") & (df_merged_clientes["Income"]> 130000.0)]##13de ellos sobrepasan los 130.000€
df_merged_clientes["Income"].mean()##media del salario


# %%
Ingresos_edad = df_merged_clientes.groupby("age category") ["Income"].mean().reset_index().sort_values(by="Income",ascending=True)
plt.figure(figsize=(10,6))
plt.bar(Ingresos_edad ["age category"],Ingresos_edad["Income"], color="skyblue") 
plt.ylabel("Average Income")
plt.title("Average salary x age category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
##media del salrio según el trabajo
df_merged_clientes["job"].value_counts()
df_merged_clientes.groupby ("job") ["Income"].mean().reset_index().sort_values(by="Income",ascending=False)
##vemos que destaca ligeramente el salario como empleado del hogar
df_merged_clientes[(df_merged_clientes["job"] == "housemaid") & (df_merged_clientes["Income"] > 130000.0)]
## 369 empleados del hogar ganan más de 130.000€ al año. Conclusión no relevante para gráfico. 


# %%
##media del salario según nivel de estudios
df_merged_clientes["education"].value_counts()
df_merged_clientes.groupby("education") ["Income"].mean().reset_index().sort_values(by="Income",ascending= False)
##media de salario según nivel de estudios muy similar. Estudiantes con título universitario no destacan.

# %%
Ingresos_education = df_merged_clientes.groupby("education") ["Income"].mean().reset_index().sort_values(by="Income",ascending= False)
plt.figure(figsize=(10,6))
plt.fill_between(Ingresos_education ["education"],Ingresos_education["Income"], color="lightgreen") 
plt.ylabel("Average Income")
plt.title("Education x Average Income")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %% [markdown]
# Análisis por fecha

# %%
##Cantidad de contactos según el mes y año
df_merged_clientes.groupby("contact_month") ["ID"].count().reset_index().sort_values(by="ID",ascending=False)
df_merged_clientes.groupby("contact_year") ["ID"].count().reset_index().sort_values(by="ID",ascending=False)
##A lo largo de la campaña, se ha mantenido una frecuencia de contacto a clientes por cada mes y año muy similar.
##conclusión no relevante para gráfico


# %%
##Número de visitas a la web según el año en el que se hicieron clientes 
df_merged_clientes.groupby("Year become Client")["NumWebVisitsMonth"].sum().reset_index()
## la cantidad de visitas a la web según el año, mantiene correlación con la cantidad de clientes que se han unido cada año. A más numero de clientes, más visitas a la web.
visitas_year_client = df_merged_clientes.groupby("Year become Client")["NumWebVisitsMonth"].sum().reset_index()
plt.figure(figsize=(3,3))
plt.scatter(visitas_year_client ["Year become Client"],visitas_year_client["NumWebVisitsMonth"], color="gold") 
plt.title("web visitis x year become to client") 
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
df_merged_clientes.groupby("Year become Client").mean(numeric_only=True)
media_año_ingreso = df_merged_clientes.groupby("Year become Client").mean(numeric_only=True)
data = {
    'Year become Client': [2012, 2013, 2014],
    'Income': [93087.21, 92788.95, 93706.47],
    'Kidhome': [1.004, 0.991, 1.014],
    'Teenhome': [0.999, 0.996, 0.999],
    'NumWebVisitsMonth': [16.54, 16.58, 16.67],
    'age': [39.87, 40.66, 39.69],
    'payment default': [0.0, 0.0004, 0.0],
    'housing': [0.492, 0.586, 0.566],
    'loan': [0.154, 0.156, 0.158],
    'last interaction duration': [260.71, 239.14, 265.30],
    'contacts made in this campaign': [2.91, 2.44, 2.17],
    'days since last contact': [999.0, 992.98, 890.70],
    'previously contacted?': [0.0, 0.125, 0.453],
    'emp.var.rate': [1.285, 0.288, -1.776],
    'cons.price.idx': [94.036, 93.282, 93.101],
    'cons.conf.idx': [-39.664, -40.315, -41.834],
    'euribor3m': [4.916, 4.073, 1.415],
    'number of employees': [3424.66, 5194.38, 4964.36],
    'latitude': [36.799, 36.903, 36.909],
    'longitude': [-95.920, -95.926, -95.974]}## creamos un diccionario con el resultado de agrupar la meda de todas las variables, por el año de unión de clientes
##dibujamos un mapa de calor 
media_año_ingreso = pd.DataFrame(data).set_index('Year become Client')
plt.figure(figsize=(16, 10))
sns.heatmap(media_año_ingreso.T, cmap='plasma', annot=True, fmt=".2f", linewidths=0.5, cbar_kws={'label': 'Valor'})
plt.title("Media de variables según año de ingreso", fontsize=16)
plt.xlabel("Año en que se volvió cliente")
plt.ylabel("Variables")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
## Algunas conclusiones: 
## Solo 3 clientes tienen historial de impagos, y los tres se unieron en el 2013
## Ningún cliente que se unió en el 2012 había sido contactado previamente en otra campaña.
## en esta camapaña, se ha contactado más a los clientes que se unieron en el 2012. 
## menos de la mitad de los clientes que se unieron en el 2012, tenían una casa en propiedad. 
## La duración de la última interacción es algo menor en los clientes que se unieron en el 2013.
## los clientes que se unieron en el 2014, se les tarda menos en volver a contactar

# %%
dinámica_años_edades = df_merged_clientes.pivot_table(index='Year become Client',columns='age category',values='ID',aggfunc='count',fill_value=0)
dinámica_años_edades.loc["Total"] = dinámica_años_edades.sum()

dinámica_años_edades_no_total = dinámica_años_edades.drop("Total",axis=0)
dinámica_años_edades_no_total.plot(kind='bar', stacked=True, figsize=(10,6), colormap='viridis')
plt.title("Clientes por categoría de edad y año de ingreso")
plt.xlabel("Año en que se convirtió en cliente")
plt.ylabel("Cantidad de clientes")
plt.legend(title="Categoría de edad", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
## conclusiones:
## La mayoría están en la categoría de adultos (entre los 31 y los 50 años)
## en el 2012, no se unió nadie meno de edad (10 o menos), ni perona mayor (mayor de 68)
## casi todas las personas mayores se unierón en el 2014
## En el 2012 y 2013, muchos de los clientes que se unieron estaban en la categoría de adulto.

# %% [markdown]
# Análisis según número de visitas a la web

# %%
## Análisis según categoria de edad y cantidad de visitas a la web
df_visitas_edades = df_merged_clientes.groupby("age category") ["NumWebVisitsMonth"].sum().reset_index()
df_cantidad_cat_edades = df_merged_clientes.groupby("age category") ["ID"].count().reset_index()
df_visitas_edades.insert(1,"Número de clientes",df_cantidad_cat_edades["ID"])
categoria_de_edades = df_visitas_edades["age category"]
numero_clientes_por_categoria = df_visitas_edades["Número de clientes"]
visitas_por_edad = df_visitas_edades["NumWebVisitsMonth"]
##visualización:
x = np.arange(len(categoria_de_edades))  # categorías ya guardadas
plt.figure(figsize=(6,4))
plt.bar(x - 0.15, numero_clientes_por_categoria, width=0.5, label="Clientes", color="skyblue")
plt.bar(x + 0.15, visitas_por_edad, width=0.3, label="Visitas", color="orange")
plt.xticks(x, categoria_de_edades, rotation=45)
plt.title("Número de Clientes y visitas web por edad")
plt.legend()
plt.tight_layout()
plt.show()

# %%
## visualización con un gráfico de lineas
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(categoria_de_edades, numero_clientes_por_categoria, color='skyblue', label='Número de clientes', marker='o')
ax.plot(categoria_de_edades, visitas_por_edad, color='orange', label='Visitas web', marker='s')
ax.set_xlabel('Categoría de edad')
ax.set_ylabel('Cantidad')
plt.title('Clientes y Visitas Web por Categoría de Edad')
plt.xticks(rotation=45, ha='right')
ax.legend(loc='upper left')
fig.tight_layout()
plt.show()

# %%
job_x_visitas = df_merged_clientes.groupby("job") ["NumWebVisitsMonth"].sum().reset_index()
cuenta_job=df_merged_clientes.groupby("job")["ID"].count().reset_index()
job_x_visitas.insert(1,"Cantidad clientes",cuenta_job["ID"])
job_x_visitas
categoria_trabajo = job_x_visitas["job"]
num_clientes = job_x_visitas["Cantidad clientes"]
visitas_por_job = job_x_visitas["NumWebVisitsMonth"]
##visualización gráfico de líneas:
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(categoria_trabajo, num_clientes, color='skyblue', label='Número de clientes', marker='o')
ax.plot(categoria_trabajo, visitas_por_job, color='orange', label='Visitas web', marker='s')
ax.set_xlabel('Tipo de trabajo')
ax.set_ylabel('Cantidad')
plt.title('Clientes y Visitas Web por tipo de trabajo')
plt.xticks(rotation=45, ha='right')
ax.legend(loc='upper left')
fig.tight_layout()
plt.show()

# %%
## también añadir una columna que sea "menor en casa" kidhome + teenhome
marital_x_visitas = df_merged_clientes.groupby("marital")["NumWebVisitsMonth"].sum().reset_index()
cuenta_marital=df_merged_clientes.groupby("marital")["ID"].count().reset_index()
marital_x_visitas.insert(1,"Cantidad_de_clientes",cuenta_marital["ID"])
categoria_marital = marital_x_visitas["marital"]
nume_clientes = marital_x_visitas["Cantidad_de_clientes"]
visitas_por_marital = marital_x_visitas["NumWebVisitsMonth"]

## visualización por gráfico de líneas
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(categoria_marital, nume_clientes, color='skyblue', label='Número de clientes', marker='o')
ax.plot(categoria_marital, visitas_por_marital, color='orange', label='Visitas web', marker='s')
ax.set_xlabel('Estado civil')
ax.set_ylabel('Cantidad')
plt.title('Clientes y Visitas Web por Estado civil')
plt.xticks(rotation=45, ha='right')
ax.legend(loc='upper left')
fig.tight_layout()
plt.show()

# %%
marital_x_visitas.insert(3,"ratio",marital_x_visitas["NumWebVisitsMonth"]/marital_x_visitas["Cantidad_de_clientes"])
marital_x_visitas["ratio"]## El ratio de visitas por cliente muestra poca variación entre las diferentes categorías de estado civil.

# %%
##queremos insertar una columna que nos diga si el cliente tiene niños o adolescentes
df_merged_clientes.insert(3,"Have any kids or teens",df_merged_clientes.apply(lambda columna: "Yes"if columna["Kidhome"]>0 or columna["Teenhome"]>0 else "No",axis=1))


# %%
hijos_x_visitas = df_merged_clientes.groupby("Have any kids or teens")["NumWebVisitsMonth"].sum().reset_index()
tiene_hijos = df_merged_clientes.groupby("Have any kids or teens")["ID"].count().reset_index()
hijos_x_visitas.insert(1,"cantidad_personas",tiene_hijos["ID"])
hijos_x_visitas.insert(3,"ratio",hijos_x_visitas["NumWebVisitsMonth"]/hijos_x_visitas["cantidad_personas"])

categoria_hijos = hijos_x_visitas["Have any kids or teens"]
cantidad_personas_hijos = hijos_x_visitas["cantidad_personas"]
vistias_hijos = hijos_x_visitas["NumWebVisitsMonth"]

##visualización por gráfico de líneas
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(categoria_hijos, cantidad_personas_hijos, color='skyblue', label='Número de clientes', marker='o')
ax.plot(categoria_hijos, vistias_hijos, color='orange', label='Visitas web', marker='s')
ax.set_xlabel('¿Tiene hijos en casa?')
ax.set_ylabel('Cantidad de personas')
plt.title("Visitas Web según con o sin hijos")
plt.xticks(rotation=45, ha='right')
ax.legend(loc='upper left')
fig.tight_layout()
plt.show() 


# %% [markdown]
# Análisis camapaña previa y contactos

# %%
## Ya hacer analisis de camapaña y llamadas
## veri si hay relacíon entre exito o fracaso si se les contacta más de una vez (anterior camapaña)
modo_contacto = df_merged_clientes.groupby("contact")["ID"].count().reset_index() 
total = modo_contacto["ID"].sum()
modo_contacto.insert(2,"Porcentaje",((modo_contacto["ID"]/total)*100).round(2)) ##agregamos el procentaje de personas de clientes contactados de un modo u otro
modo_contacto 


# %%
df_merged_clientes["last interaction duration"].mean()
df_merged_clientes["contacts made in this campaign"].mean()
(df_merged_clientes["previously contacted?"] ==1.0).sum() 
resultado_anterior = df_merged_clientes.groupby("previous campaign outcome")["ID"].count().reset_index() 
resultado_anterior_sin_nulos = resultado_anterior[resultado_anterior["previous campaign outcome"]!="nonexistent"]## quitamos la fila de non existent ya que hace ruido innecesario
total_sin_non = resultado_anterior_sin_nulos["ID"].sum()
resultado_anterior_sin_nulos.insert(2,"porcentaje",((resultado_anterior_sin_nulos["ID"]/total_sin_non)*100).round(2))
resultado_anterior_sin_nulos ##en esta tabla observamos el porcentaje de clietes contactados, que en anteriores camapañas tuvieron resultado positvo o negativo
##visualización 
plt.figure(figsize=(10,6))
plt.bar(resultado_anterior_sin_nulos ["previous campaign outcome"],resultado_anterior_sin_nulos["ID"], color="skyblue") 
plt.ylabel("Personas contactadas en la anterior campaña")
plt.title("Éxito de la campaña anterior entre clientes también contactados en la actual")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# %%
cateogria_edad_interacciones = df_merged_clientes.pivot_table(index='last interaction duration category',columns='age category',values='ID',aggfunc='count',fill_value=0)
##visualización
plt.figure(figsize=(10, 6))
sns.heatmap(cateogria_edad_interacciones, annot=True, fmt='d', cmap='Blues')
##visualización
plt.title('Número de clientes por duración de interacción y categoría de edad')
plt.xlabel('Categoría de edad')
plt.ylabel('Duración de la última interacción')
plt.tight_layout()
plt.show()

# %% [markdown]
# Análisis de índice de precios e Índice de confianza

# %%
sns.histplot(df_merged_clientes['cons.price.idx'], kde=True, color='blue')
plt.title('Distribución del índice de precios')
plt.show()##distribución del índice de precios 

# %%
sns.histplot(df_merged_clientes['cons.conf.idx'], kde=True, color='green')
plt.title('Distribución del índice de confianza del consumidor')
plt.show() ##distribución del índice de confianza del consumidor

# %%
plt.figure(figsize=(12, 6))  
sns.boxplot(x='age category', y='cons.conf.idx', data=df_merged_clientes)
plt.title('Índice de confianza por categoría de edad')
plt.xlabel('Categoría de edad')
plt.ylabel('Índice de confianza')
plt.tight_layout()  
plt.show()

# %%
precio_evolucion = df_merged_clientes.groupby("contact_year")['cons.price.idx'].mean().reset_index()
from matplotlib.ticker import MaxNLocator
##visualización
plt.figure(figsize=(10, 6))
plt.plot(precio_evolucion["contact_year"], precio_evolucion["cons.price.idx"], marker='o')
plt.title("Tasa de variación del indice de precios por año de contacto")
plt.xlabel("Año de contacto")
plt.ylabel("Tasa de variación de indice de precios")
plt.grid(True)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))##esto fuerza números enteros en el eje X de los años
plt.show()

# %%
df_merged_clientes["emp.var.rate"].describe()
tasa_tiempo = df_merged_clientes.groupby("contact_year")["emp.var.rate"].mean().reset_index()
tasa_tiempo["contact_year"] = tasa_tiempo["contact_year"].astype(int)

##visualización
plt.figure(figsize=(10, 6))
plt.plot(tasa_tiempo["contact_year"], tasa_tiempo["emp.var.rate"], marker='o')
plt.title("Tasa de variación del empleo por año de contacto")
plt.xlabel("Año de contacto")
plt.ylabel("Tasa de variación del empleo")
plt.grid(True)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))##esto fuerza números enteros en el eje X de los años
plt.show()

# %%
producto_empleo = df_merged_clientes.groupby("product_subscription")["emp.var.rate"].mean().reset_index()
##visualización
plt.figure(figsize=(8, 5))
plt.bar(producto_empleo["product_subscription"], producto_empleo["emp.var.rate"], color='skyblue')
plt.title("Tasa media de variación del empleo por suscripción a producto")
plt.xlabel("¿Suscribió al producto?")
plt.ylabel("Tasa media de variación del empleo")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# %% [markdown]
# Análisis por producto suscrito

# %%
(df_merged_clientes["product_subscription"] =="yes").sum()##clientes que han contatado un producto
(df_merged_clientes["product_subscription"] =="no").sum()##clientes que no han contratado un producto

subsc_yes = df_merged_clientes[df_merged_clientes["product_subscription"]=="yes"]##hacemos un DF solo con los clientes que suscribieron un producto
tabla_subscripcion = subsc_yes.pivot_table(index='Year become Client',columns='age category',values='product_subscription',aggfunc='count',fill_value=0)
##visualización
plt.figure(figsize=(10, 6))
sns.heatmap(tabla_subscripcion, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Clientes que han suscrito un producto por año y categoría de edad')
plt.ylabel('Año de incorporación del cliente')
plt.xlabel('Categoría de edad')
plt.tight_layout()
plt.show()

# %%
df_merged_clientes["Income"].describe().T## ver como están distribuido el nivel de salario de cada cliente

# %%
def categoria_salario (income): ##creamos una función que categorice en función del nivel de salarios
    if pd.isna(income):
        return "desconocido"  
    if income >=0.0 and income <= 50000.0:
        return "salario bajo"
    elif income >=50001.0 and income <= 93000.0:
        return "salario medio"
    elif income >=93001.0 and income <= 150000.0:
        return "salario alto"
    elif income >=150001.0:
        return "salario muy alto"
    
df_merged_clientes.insert(1,"Income category",df_merged_clientes["Income"].apply(categoria_salario))##incluimos esa columna en el DF principal
    

# %%
subsc_yes.insert(1,"Income category",df_merged_clientes["Income category"])##copiamos esa columna en el DF donde estamos analizando relación entre salario y producto suscrito

# %%
Income_sub = subsc_yes.groupby("Income category")["product_subscription"].count().reset_index()##agrupamos producto suscrito según categoría
Income_cat_total = df_merged_clientes.groupby("Income category")["ID"].count().reset_index()##vemos cuantos clientes pertenecen a cada categoria de nivel de salario
Union = Income_cat_total.merge(Income_sub,how="inner",on="Income category") ##unimos ambos DF a través de la columna coincidente, Income category
Union.insert(3,"ratio compra producto",((Union["product_subscription"]/Union["ID"])*100).round(2))##creamos una columna mas con el ratio de suscripción por categoria de ingresos
##visualización
plt.figure(figsize=(10, 6))
plt.bar(Union["Income category"], Union["ID"], width=0.4, label="Total Clientes", align="center")
plt.bar(Union["Income category"], Union["product_subscription"], width=0.4, label="Clientes Suscritos", align="edge")
plt.title('Comparación de Clientes Totales vs Clientes Suscritos por Categoría de Ingreso')
plt.xlabel('Categoría de Ingreso')
plt.ylabel('Número de Clientes')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# %%
df_merged_clientes.to_excel("clientes_merged_resultado.xlsx", index=False) ##exportamos a Excel el archivo único, derivado de la unión de los diferentes DF, y donde se ha realizado el análisis


