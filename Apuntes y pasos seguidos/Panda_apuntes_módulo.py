# %%
import pandas as pd
import numpy as np

# %%
pip install openpyxl


# %%
pip install --upgrade pandas


# %%
import os

# %% [markdown]
# Creación de series en base a arrays, listas o diccionarios

# %%
serie_vacias = pd.Series()
serie_vacias
array_uni = np.arange(10)
series_array = pd.Series(array_uni)##series a partir de un array
lista = ["hola","semana",34,"calabaza",37,93,52,"ama",["sol","noche"]]##esto estaría mal porque tiene datos de diferente tipo
series_lista = pd.Series(lista)##Series a partir de una lista
diccionario = {"Spain":"Europe","Canada":"America","Madagascar":"Africa","Australia":"Oceania"}
serie_diccionario = pd.Series(diccionario)

# %% [markdown]
# Indexación en series. 4 tipos: Posición, rango, lista de índices y etiqueta

# %%
series_array[1]##indexación por posición
series_array[1:4]##indexación por rango, en este caso la posición de la 1 a la 3. Se pone dos puntos
lista_indices = [3,5,8]##indexación por lista de indices Simplemente hacer una lista con las posiciónes que quieres de tu serie
series_lista[lista_indices]##en corchetes poner la variable con la lista de los indices

##indexación por etiquetas
array2 = np.arange(10)
etiquetas_serie_array2 = ["a","b","c","d","e","f","g","h","i","j"]
serie_array2 = pd.Series(array2,etiquetas_serie_array2)
print(serie_array2)
serie_array2["e"]

# %% [markdown]
# Dataframes a partir de diccionario

# %%
diccionario_dataframe = {"carrera":["Mates","informatica"],"nota de corte": [9.8,9.3],"universidad":["urjc","UCM"],"plazas":[1000,2000]}
pd.DataFrame(diccionario_dataframe,index=["ciencias","tecnologia"])##los valores se consideran columnas

# %% [markdown]
# Dataframes a partir de un array

# %%
array_dataframe = np.random.randint(0,100,(2,3))
pd.DataFrame(array_dataframe,index=["notas alumno 1","notas alumno 2"],columns=[2022,2023,2024])##como el array tiene tres columnas, debemos poner tres columnas

# %% [markdown]
# Dataframe a partir de una lista

# %%
lista_dataframe = ["Rodilla","Tierra","Burger"]
pd.DataFrame(lista_dataframe,index=["bocadillos","tacos","hamburgesas"],columns=["restaurantes"])##como es un 3x1, solo le puedes poner 3 filas y una columna

# %% [markdown]
# Dataframe a partir de una lista de varias listas

# %%
lista1_dataframe = ["Examen1","Examen2"]
lista2_dataframe = [7.9,4.6]
pd.DataFrame([lista1_dataframe,lista2_dataframe]).T##el "t" se pone para trasponer

# %% [markdown]
# Apertura de archivos Excel, CSV y JSON

# %%
##apertura de archivo excel
os.getcwd()
df_excel = pd.read_excel('c:\\Users\\jbartolomej\\Desktop\\Especialización\\Data\\Pyhton_librerias\\Archivos a subir\\Gastos.xlsx',sheet_name="Follow-up",header=6)
df_excel 

# %%
##abrir un archivo CSV
df_CSV = pd.read_csv('c:\\Users\\jbartolomej\\Desktop\\Especialización\\Data\\Pyhton_librerias\\Archivos a subir\\User_Download_27032025_corto.csv',sep=',')
df_CSV

# %%
##abrir un archivo JSON
df_JSON = pd.read_json('c:\\Users\\jbartolomej\\Desktop\\Especialización\\Data\\Pyhton_librerias\\Archivos a subir\\JSON_corto.json')
df_JSON

# %% [markdown]
# Métodos básicos a aplicar en los Dataframe

# %%
##he cambiado el directorio con los metodos os.chdir y os.getchd a la carpeta donde está el archivo guardado para no escribir toda la ruta
df_unis = pd.read_csv('c:\\Users\\jbartolomej\\Desktop\\Especialización\\Data\\Pyhton_librerias\\Archivos a subir\\DatosPandasUniversidades.csv')
pd.set_option('display.max_columns',None)##esto es para configurar que se vean todas las columnas de los Dataframe
pd.read_csv('c:\\Users\\jbartolomej\\Desktop\\Especialización\\Data\\Pyhton_librerias\\Archivos a subir\\DatosPandasUniversidades.csv',index_col=2)##para cambiar el el indice ponemos Index col
df_unis.head()##te muestra las cinco primeras filas, o el número que pongamos en el parentesis 
df_unis.tail()## te muestra las cinco ultimas filas, o el número que pongamos en el parentesis
df_unis.sample()##muestra filas al azar
df_unis.info()##muestra info general del datafram (nulos,tipos de datos)
df_unis.select_dtypes(include='float')##te filtra las columnas con un tipo de dato específico
df_unis.isnull()##te da los datos que son nulos
df_unis.isnull().sum()##te suma los valores nulos de cada columna
df_unis.duplicated().sum()##te dice cuantas columnas duplicadas hay
df_unis.describe().T##te dice información estádistica de la table
df_unis["academic_reputation"].mean()##la media de esa columna
df_unis["country"].count()
df_unis['rank'].unique()##te dice los vlaores unicos de una columna en un array
df_unis['rank'].value_counts()##te dice cuantas veces se repite cada valor
df_unis["country"].value_counts()## cuantas veces se repite cada país

# %% [markdown]
# Propiedades

# %%
df_unis.shape ##muestra el numero de filas y columnas en una tupla.
df_unis.size##muestra la cantidad de datos del dataframe
df_unis.columns##muestra el nombre de las columnas en un 
df_unis.dtypes## nos devuelve que tipo de datos tenemos por columna

# %% [markdown]
# Modelos Loc e Iloc

# %%
df_u=pd.read_csv('c:Archivos a subir\\DatosPandasUniversidades.csv',index_col=2)##nos tenemos que basar en la columna indice que queramos, en este caso las universidades
df_u

# %%
df_u.loc["The University of Sheffield","overall_score"]##dame la puntación de la university de Sheffield
df_u.iloc[2,1]##dime el valor de la tercera universidad y la segunda columna
df_u.loc["Pontificia Universidad CatÃ³lica de Chile (UC)",:]##toda la información de las clumnas de esa universidad
df_u.iloc[7,:]##toda la info de la universidad en la posición 7, que es la de Singapore 
df_u.loc[:,"country"]##la columna country respecto a universidades
df_u.iloc[:,13]##lo mismo pero con indices
df_u.loc[["Uppsala University","University of Nottingham"],"rank"]##información de dos universidades
df_u.iloc[[2,10],1]##el rank de esas dos universidades
df_u.loc[:,"country"]##toda la columna de country

# %% [markdown]
# Filtrado de datos

# %%
##crear una condición en una variable
condicion_USA = df_u["country"] == "United States"##filtro unis de USA
df_u[condicion_USA]
df_u[df_u["country"]=="United Kingdom"]##también puede hacerse así para indicarse dos veces.
puntuacion_alta = df_u["overall_score"] >90##filtro unis con alta puntuación
df_u[puntuacion_alta]
df_u[condicion_USA & puntuacion_alta]##aqui estamos combinando ambas condiciones anteriores
##se puede hacer una variable con varios filtros, y aplicar el método "isin"
filtro_paises= ["Chile","Sweden","China"]
China_SE_Chile = df_u[df_u["country"].isin(filtro_paises)]
China_SE_Chile
##metodo between, para filtrar entre un rango númerico
rank_0_10 = df_u[df_u["rank"].between(90,100,inclusive="both")]##las unis entre 90 y 100 por ranking
rank_0_10
##metodo str.contains(), para filtrar por texto EN LOS DATOS
df_u[df_u["country"].str.contains("United",na=False)]##filtro por las columnas que contienen "united"
##Método FILTER para filtrar por texto en las columnas o filas
df_u.filter(items=["rank","university"])##filtrar por columnas
df_u.filter(like="Institute",axis=0)##filtrar por filas que contienen la palabra "Institute"

# %% [markdown]
# Operaciones aritméticas

# %%
diccionario = {"ana":{"peso":70,"altura": 190},"Juan":{"peso":99,"altura":203},"Pepe":{"altura":178,"peso":145}}
df_dicc = pd.DataFrame(diccionario)
df_dicc +10##sumar 10 a los datos del DF
df_dicc.add(10)##sumar 10 con el método
df_dicc - 30##restarle 30
df_dicc.sub(30)##restarle 30
df_dicc * 23
df_dicc.mul(23)##multiplicar por 23
df_dicc / 2
df_dicc.div(2).astype(int)##dividir entre 2
df_dicc.mod(2)##para el resto, asi sabes si son pares o impares
df_dicc**3
df_dicc.pow(3)##potencias

# %% [markdown]
# Eliminar columnas o filas

# %%
df_u.drop("sequence",axis=1,inplace=True)##aqui eliminamos la columna sequence del original


# %%
df_u.head(7)##vemos que ya no está la columna sequence

# %%
df_u_no_oxford = df_u.drop("University of Oxford",axis=0,inplace=False)
df_u_no_oxford##en este DF no está la de Oxford
df_u##en este sigue estando la de Oxford, pero no la columna sequence

# %% [markdown]
# Generar columnas

# %%
copia_df_u = df_u.copy()##hacemos una copia por si acaso....
df_u

# %%
##por asiganción directa, a través del calculo de algo
calculo_media = (df_u["academic_reputation"] + df_u["employer_reputation"])/2##sumas dos coulmas numericas y divides entre dos para hacer la media
df_u["mean_reputation_(media)"] = calculo_media##aplicas la varibale a la nueva columna
df_u

# %%
##Método assign()
df_u_columnas = df_u.assign(rank_por_2 = df_u["rank"]*2)##hacer la operación dentro del método. En este caso la columna rango por 2
df_u_columnas.head()

# %%
##Método Insert()
len(df_u_columnas.columns)##así ves cuantas columnas tiene tu DF
df_u_columnas.insert(14,"puntuación total ente rango",(df_u_columnas["overall_score"]/df_u_columnas["rank"]))##igual que el anterior pero puedes indicar la posición

# %%
##Método eval()
df_u_columnas.eval("media_total = overall_score.mean()",inplace=True)##es una columna con la meda total. Se hace todo con strings
df_u_columnas.head()

# %% [markdown]
# GROUP BY

# %%
df_rrhh = pd.read_csv('c:Archivos a subir\\DatosUsuariosRedesSociales.csv',sep=',')
df_rrhh_copy = df_rrhh.copy()
df_rrhh.sample(4)

# %%
##edad media por plataforma
serie_medias = df_rrhh.groupby("platform")["age"].mean(numeric_only=True)##nos devuelve una Serie si especificamos columna. Si no especificamos columna hay que poer numeric only, si especificamos no hace falta.
edad_media = serie_medias.reset_index()##para devolverlo a DF usamos reset index
edad_media

# %%
##mediana de los ingresos en función de su area de residencia
df_rrhh.groupby("demographics")["income"].median().reset_index()

# %%
##tiempo total de uso de las RRHH por pais
df_rrhh.groupby("location")["time_spent"].sum().reset_index()

# %%
##calcular la media, mediana, desviación, máximo y mínimo del salario de los usuarios en función de su profesión
df_rrhh.groupby("profession")["income"].agg(["mean","median","std","max","min"]).reset_index()##para calcular varios metodos estadísticos, utilizamos metodo agg(), y pasamos en una lista de str los métodos

# %%
df_rrhh.groupby("platform").get_group("Facebook")##filtrar por platform y dentro facebook

# %% [markdown]
# Método Apply

# %%
## Jóvenes adultos: De 18 a 28 años.
## Adultos jóvenes: De 29 a 39 años.
## Mediana edad: De 40 a 50.
##Adultos mayores: Por encima de los 51 años.
def categorización_edades(edad):
    if edad >=18 and edad <=28:
        return "Jóvenes adultos"
    elif edad >=29 and edad <=39:
        return "Adultos Jóvenes"
    elif edad >=40 and edad <=50:
        return "Mediana edad"
    elif edad >=51:
        return "Adultos mayores"

# %%
df_rrhh["edad_categorización"] = df_rrhh["age"].apply(categorización_edades)##crear una columna llamada "edad categorización" que sea igual a la funcion aplicada a la columna edad
df_rrhh.head()##se nos ha creado la columna "age category"

# %%
df_rrhh["income"] = df_rrhh["income"].astype(float)##con el método astype, también se puede cmabiar el tipo de dato en una columna
df_rrhh["income"]

# %%
def dato_int(numero):##hacemos una función que cambie los datos a int
    return int(numero)

# %%
df_rrhh["income"] = df_rrhh["income"].apply(dato_int)##podemos aplicar la función para cambiar el tipo de dato de una columna
df_rrhh["income"]##aquí ya vuelven a estar de tipo int

# %%
##para funciones faciles, se puede utilizar una Lambda. Ejemplo parecido
df_rrhh["time_spent"] = df_rrhh["time_spent"].apply(lambda numero: float(numero))##cambiar a float el dato de la columna time spent a través de Lambda
df_rrhh["time_spent"].dtype

# %%
##si la funcion es un condicional con un if y else, se puede hacer con lambda. Si la función tiene elif NO se puede
df_rrhh['Owns_Car'] = df_rrhh['Owns_Car'].apply(lambda x: "yes" if x == True else "no")
df_rrhh["Owns_Car"]##SOLO DARLE UNA VEZ

# %%
##funciones con mas de un parametro
def viajera_mujer(columna_interes,columna_gender):
    if columna_interes == "Travel" and columna_gender == "female":
        return True
    else:
        return False
df_rrhh["Audiencia_objetivo"] = df_rrhh.apply(lambda x: viajera_mujer(x["interests"],x["gender"]),axis=1)##no entiendo muy bien el código
df_rrhh ["Audiencia_objetivo"].value_counts()


# %%
df_rrhh[(df_rrhh["interests"]=="Travel") & (df_rrhh["gender"]=="female")] ##realmente aquí estás filtrando y haciendo mas o menos lo mismo

# %%
##funcion dos parametros sin utilizar Lambda
def age_update (edad,numero):
    return edad + numero

df_rrhh["age"] = df_rrhh["age"].apply(age_update,numero=2)##aqui estamos sumando 2 a la columna edad, indicando solo el parametro numero
df_rrhh.head()##cada vezque ejecutemos sumará 2!!!

# %% [markdown]
# Combinación de Data Frames: Concat, Merge, Join

# %%
coches_2023 = pd.read_csv('c:Archivos a subir\\Combinación de archivos\\datos_ford_2023.csv',sep=',',index_col=0)##ponemos la primera columna como indice en todas
coches_2024 = pd.read_csv('c:Archivos a subir\\Combinación de archivos\\datos_ford_2024.csv',sep=',',index_col=0)
coches_caracteristicas = pd.read_csv('c:Archivos a subir\\Combinación de archivos\\datos_ford_caracteristicas.csv',sep=',',index_col=0)

# %%
##método concat. Lo mas imporntate es saber si concatenamos por filas o columnas
df_concat_filas = pd.concat([coches_2023,coches_2024],axis=0,join="outer")##aqui se añaden filas para integrar los datos
df_concat_columnas = pd.concat([coches_2023,coches_2024],axis=1)##aquí se añaden columnas para integrar los datos
df_concat_filas.head(3)##en este caso, la concatenación por filas es la mejor opción ya que 


# %%
##metodo merge, es como en SQL, hay que decidir como queremos que sea el join e indicar la columna común con un on.
coches_2023_caracteristicas = coches_2023.merge(coches_caracteristicas,how="inner",on="VIN")
coches_2023_caracteristicas##vemos que no hay ningun dato coincidente en el VIN de coches 2023 y caracteristicas.
##por tanto, todos los datos de caracteristicas son de coches de 2024

# %%
coches_2024_caracterisitcas = coches_2024.merge(coches_caracteristicas,how="inner",on="VIN")
coches_2024_caracterisitcas ##aqui si, se han combinado datos en base a la columna VIN, por eso solo aparece una vez. 

# %%
## el metodo join es igual que el merge pero las columnas ON deben ser los indices...por lo que hay que establecer los indices en ambas columnas VIN
coches_2024_VIN = coches_2024.set_index(["VIN"],inplace=False)
coches_caracteristicas_VIN = coches_caracteristicas.set_index(["VIN"],inplace=False)
coches_2024_caracterisitcas_join = coches_2024_VIN.join(coches_caracteristicas_VIN,how="inner",on="VIN")
coches_2024_caracterisitcas_join##lo mismo que con el merge, pero con la columna VIN como índice. NO MUY IMPORTANTE.

# %% [markdown]
# Pivotado de datos

# %%
##cuantos modelos de coche ha vendido cada vendedor entre los años 2023 y 2024.
df_concat_filas
df_concat_filas.groupby("id_del_vendedor")["modelo_coche"].count().reset_index()##a tarvés de un group by solosabemos cuantos coches ha vendido cada vendedor, no los modelos
df_concat_filas.pivot_table(values="fecha_venta",index="id_del_vendedor",columns="modelo_coche",aggfunc="count").head()
##4 parametros. index son los datos de la columna que iran en las filas. columns es la columna, aggfunc es la función que se aplicará a los datos.
##values es como la columna base en la que se hace el calculo, que no puede coincidir con las demás.

# %% [markdown]
# Melt

# %%
coches_2024_caracterisitcas = coches_2024_caracterisitcas.head(3)
##fusionar las columnas, ’numero_puertas’, ‘camara_trasera’ y sensor_aparcamiento’ y usaremos como índice el modelo del coche.
coches_2024_caracterisitcas.melt(id_vars="modelo_coche",value_vars=["fecha_venta","numero_puertas","camara_trasera","sensor_aparcamiento"],var_name="caracteristicas_generales",value_name="valores")
## te va dando los valores de cada modelo en una misma columna. Si solo queremos caracteristicas de los tres primeros modelos, e indicamos 4 columnas, el DF tendra 4*3=12 filas.

# %% [markdown]
# Conexión SQL con Python

# %%
pip install psycopg2


