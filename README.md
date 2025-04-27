# Profile Plotter

## ENG 

This Python program is a sample personal project based on some of the work I do at my job.
Sometimes, we have to analize electrical energy parameters from electrical substations. This is 
usually done using Excel sheets (it gets really slow with medium to big data sets).

The general concept is to have a GUI using Tkinter that lets the user select a .csv file containing
information about "load profiles" (related to electric metering).Then the data is transformed into
a dataframe using Pandas and fed to a plotting app made using the Dash framework. 

The Dash framework allows us to add styling, filters and multiple variables plotted together to our chart
without much effort.

The different .csv files have to be placed into a "data" folder placed at the root of the project.
For the moment, the program will work only if the data files follow some basic naming conventions.


## ESP

Este programa de Python es un proyecto personal de muestra, basado en tareas que realizo en mi trabajo actual.
Algunas veces, tenemos que analizar parámetros de energía eléctrica de subestaciones transformadoras. Esto, 
normalmente se realiza utilizando hojas de cálculo en Excel (las cuales se ralentizan bastante con
 datasets medianos a grandes).

El concepto general se trata de tener una interfaz gráfica usando Tkinter de la cual un usuario puede seleccionar
un archivo .csv que contiene información sobre perfiles de carga (relacionados a mediciones eléctricas). Luego,
esta información es transformada en un dataframe usando Pandas y se usa para alimentar una aplicación graficadora
hecha con el framework Dash.

El framework Dash nos permite implementar estilo, filtros y graficar distintas variables simultáneamente en el 
diagrama sin mucho esfuerzo.

Los archivos .csv deben estar alojados en una carpeta "data" en el nivel base del proyecto.
Por el momento, la aplicación solo funciona si los archivos conteniendo los datos siguen algunas reglas con los
nombres de los archivos y variables.