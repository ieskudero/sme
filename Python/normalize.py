#############################################################################################
# Clase para calcular la normalización y estandarización								  	#
# ******************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  	#
#                                                                                         	#
# Funciones: 				                                                              	#	
# 	normalize		                                                              		#
# 	standardize																			#	
#############################################################################################
import numpy as np

#cargamos funciones matemáticas. El fichero debe estar en el mismo path que este fichero
from customMath import CustomMath

class Normalize:
	def __init__(self):
		pass

	def normalize(self,df):
		'''
		Método para normalizar un dataframe
		Parámetros:
			df: (dataframe) dataframe para normalizar
		Return: (dataframe) dataframe normalizado. Solo normaliza columnas numéricas. 
		'''
		# Identificar las columnas numéricas
		numeric_cols = df.select_dtypes(include=[np.number,int,float]).columns
		
		# Normalizar cada columna numérica
		df[numeric_cols] = df[numeric_cols].apply(CustomMath.normalize_variable)
		
		return df
	
	def standardize(self,df):
		'''
		Método para estandarizar un dataframe
		Parámetros:
			df: (dataframe) dataframe para estandarizar
		Return: (dataframe) estandarizado. Solo estandariza columnas numéricas 
		'''
		# Identificar las columnas numéricas
		numeric_cols = df.select_dtypes(include=[np.number,int,float]).columns
		
		# Estandarizar cada columna numérica
		df[numeric_cols] = df[numeric_cols].apply(CustomMath.standardize_variable)
		
		return df
