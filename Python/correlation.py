#############################################################################################
# Clase para calcular la matriz de correlaciones de un dataframe                            #		
# ******************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  	#
#                                                                                         	#
# Funciones: 				                                                              	#	
# 	get_correlation		                                                              		#
#############################################################################################
import numpy as np
import pandas as pd

#cargamos funciones matemáticas. El fichero debe estar en el mismo path que este fichero
from customMath import CustomMath

class Correlation:
	def __init__(self):
		pass
	def get_correlation(self, df, max_values=5):
		'''
		Método para calcular la correlación en un data.frame en base al tipo de variable
		Parámetros:
			df: (dataframe) dataframe para correlacionar
			max_values: (int) cantidad máxima de opciones únicas de un factor a tener en cuenta para ser
								  considerado como variable categórica
		Return: (matrix) matriz de correlaciones
		'''
		# Nombres de las columnas
		c_names = df.columns

		# Longitud de las variables
		count = len(c_names)
		
		# Crear una matriz vacía cxc para almacenar las correlaciones
		cor_m = np.full((count, count), np.nan)
		
		# Calcular la correlación para cada par de columnas
		for i in range(count):
			for j in range(i, count):
				v1 = df[c_names[i]]
				v2 = df[c_names[j]]
				
				corr = np.nan
				
				# Correlación de Pearson
				if pd.api.types.is_numeric_dtype(v1) and pd.api.types.is_numeric_dtype(v2):
					corr = CustomMath.get_pearson_cor(v1, v2)
				
				# Información mutua
				elif (self._areCategory(v1,v2) and 
					v1.nunique() <= max_values and v2.nunique() <= max_values):
					corr = CustomMath.get_mutual_information_cor(v1, v2)
				
				# Asignar la correlación de forma simétrica
				cor_m[i, j] = corr
				cor_m[j, i] = corr
		
		return cor_m
	
	def _areCategory(self,v1,v2):
		'''
		Método privado para determinar si dos variables son categóricas
		Parámetros:
			v1: (series) variable 1
			v2: (series) variable 2
		Return: (boolean) True si ambas variables son categóricas
		'''
		return (v1.dtype == 'object' or v1.dtype.name == 'category') and ( v2.dtype == 'object' or v2.dtype.name == 'category')