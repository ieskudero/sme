#############################################################################################
# Clase para filtrar un dataframe en base a distintos filtros.                              #		
# ******************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  	#
#                                                                                         	#
# Funciones: 				                                                              	#	
# 	filter_by_entropy		                                                              	#
#############################################################################################
import pandas as pd

#cargamos funciones matemáticas. El fichero debe estar en el mismo path que este fichero
from customMath import CustomMath

class Filter:
	def __init__(self):
		pass
	def filter_by_entropy(self, df, threshold):
		'''
		Método para filtar un dataframe en base a un threshold de entropía
		Parámetros:
			df: (dataframe) data.frame para filtar
			threshold: (float) Threshold para filtar por entropia
		Return: (dataframe) dataframe filtrado, eliminando las variables que no hayan superado el threshold
		'''
		result = pd.DataFrame(index=df.index)

		# Iteramos sobre cada columna del dataset. Solo filtramos aquellas columnas que cumplan:
		# 1.- sean tipo factor
		# 2.- estén por debajo del threshold
		for column in df.columns:
			if df[column].dtype == 'object' or df[column].dtype.name == 'category':
				entropy = CustomMath.get_entropia(list(df[column]))
				if entropy < threshold:
					continue
			
			result[column] = df[column]
		
		return result