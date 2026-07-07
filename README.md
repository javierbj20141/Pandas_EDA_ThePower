#  Limpieza y analisis de datos (EDA), con Pandas 😃

  <img src="Pandas.jpg" width="250"> </p>


**Estructura del repositorio**:

1. Archivos en bruto y resultado: Contiene los archivos con los que se empezó el proyecto, las instrucciones y el archivo resultante del analisis, llamado: clientes_merged_resultado

2. Apuntes y pasos seguidos: Contiene un archivo py con los apuntes del estudio a través de lo módulos (no relevante para el proyecto), y otro archivo py donde he ido aplicando las transofrmaciones, y realizado el análisis de datos utilizando la libreria **pandas**

3. Archivos sueltos dentro del repositorio: el informe del análisis con las principales conclusiones, el archivo README y una foto.

**Objetivo**:

El objetivo de este proyecto fue analizar una base de datos de clientes con el fin de identificar patrones de comportamiento y variables relevantes para el diseño y evaluación de campañas de marketing.
Para ello, se trabajó con diferentes fuentes de datos que contenían información demográfica, histórica y de comportamiento de los clientes. El propósito final fue transformar y consolidar la información disponible para obtener insights significativos que permitieran comprender mejor las características de los clientes y los factores potencialmente relacionados con su respuesta ante acciones de marketing. El objetivo fue seguir estos pasos: Integración → Limpieza → Transformación → Análisis → Visualización. 🚀

**Metodologia**:

El proyecto comenzó con la integración de diferentes fuentes de datos mediante **Concat**, consolidando la información de clientes en un único DataFrame. Posteriormente, se llevó a cabo un proceso de limpieza y preparación de datos, revisando valores nulos, tipos de datos y creando nuevas variables mediante Apply para facilitar el análisis.
Una vez preparados los datos, ambos conjuntos se unificaron utilizando **Merge** a través del identificador único de cliente. Sobre la base de datos resultante se realizaron diferentes análisis utilizando técnicas como **Group By**, **Pivot Tables** y creación de métricas derivadas para identificar patrones y tendencias relevantes.
Por último, se desarrolló la fase de visualización mediante **Matplotlib** y **Seaborn**, seleccionando las representaciones gráficas más adecuadas para comunicar los principales hallazgos obtenidos.

**Autor:** Javier Bartolomé Jalvo
