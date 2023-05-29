# Proyecto-Competicion-Kaggle

Este proyecto ha venido por una competición amistosa entre los compañeros de clase del Bootcamp. 
El objetivo era utilizar Machine Learning para predecir el precio de unos portátiles. Para ello hemos partido de un dataframe que hemos tenido que transformar para poder aplicar las técnicas vistas en clase. 

Los datos eran relativamente homogéneos, aunque el mayor problema era que apenas había columnas numéricas.

### Sistema operativo

Viendo la proporción que había de cada uno de los OS hemos decidido transformar esta columna en un valor binario, 1 si Windows, 0 en cualquier otro caso. No es ideal, pues se agrupan los Mac y los Chromebook, por ejempo, pero lo hemos decidido hacer así en base a que tampoco había tantos de cada uno. 

### RAM

Con la memoria RAM simplemente hemos quitado la terminación, todos los datos estaban en GB. 

### Almacenamiento

Para limpiar esta primero hemos separado el string de cada celda por el "+", en caso de que fuesen portátiles con HDD y SDD. Hemos multiplicado cada uno de estos números por el precio medio/GB de cada tipo de almacenamiento. 0,04 por GB de HDD y 0,5 por GB de SSD, luego hemos sumado estos valores y la hemos puesto en su lugar. 
Si sólo tenían un tipo de almacenamiento hemos hecho la operación anterior pero sólo con el correspondiente. 

### Pantalla

La columna del tipo de pantalla y la resolución la hemos limpiado multiplicando los valores de píxeles horizontales y verticales. Este enfoque tiene dos inconvenientes principales, el primero es que el número de píxeles crece mucho más rápido que el precio. Un portátil con pantalla 4k puede tener 20 veces más píxeles que uno con una pantalla 1080, pero no vale 20 veces más en ningún caso. Otro fallo es la distinta tecnología de las pantallas, las tratamos de forma homogénea cuando no es lo mismo un panel IPS que una pantalla táctil. Lo bueno es que estas dos cosas suelen ser cofactores, una pantalla con más resolución suele tener mejor tecnología y hasta cierto punto se anulan. 

### GPU & CPU

Para la GPU y la CPU hemos limpiado los datos de erratas y hemos aplicado label encoding. 


### Modelos

Hemos utilizado el lazy regressor para probar varios. Al final hemos utilizado los que mejor resultados daban, sklearn.ensemble.GradientBoostingRegressor, sklearn.ensemble.RandomForestRegressor, sklearn.linear_model.LinearRegression, sklearn.linear_model.ElasticNet, sklearn.ensemble.RandomForestRegressor y sklearn.tree.ExtraTreeRegressor

Los que mejor resultados nos han acabado dando, dentro de los datos que conocemos antes de que se termine la competición, son RandomForestResgressor y GradientBoostingRegressor

