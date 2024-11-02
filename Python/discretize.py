###########################################################################################
# Clase para discretizar valores														  #
# ****************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  #
#                                                                                         #
# Funciones: 				                                                              #	
# 	discretice_vector		                                                              #	
# 	discretice		    		                                                          #	
# 	discretice_attribute	                                                              #	
# 	discretice_dataframe	                                                              #
###########################################################################################
import numpy as np
import pandas as pd

class Discretize:
	def __init(self):
		pass

	def discretice_vector(self, x, cuts, method='equal_width'):
		'''
		Método auxliar para discretizar vectores mediante los métodos "equal width" y "equal frecuency"
		Parámetros:
 		  	x: (list) Vector numérico que se desea discretizar.
 		  	cuts: (int) Número de intervalos en los que se desea discretizar.
 		  	method: (str) String que indica el método de discretización a utilizar.
 		  			"equal_width" para igual anchura o "equal_frequency" para igual frecuencia.
					   
 		Return: (object) Un objeto que contiene los valores discretizados y los puntos de corte.
		'''
		# exceptions check
		if not isinstance(x, (list, np.ndarray)) or not all(isinstance(i, (int, float)) for i in x):
			raise ValueError("use un vector numérico")
		count = len(x)
		if count <= 1:
			raise ValueError("Use un vector con más de un elemento")
		if method not in ["equal_width", "equal_frequency"]:
			raise ValueError("Nombre de método inválido. Use 'equal_width' o 'equal_frequency'.")
		
		cut_points = []

		if method == "equal_width":
			# Encontrar los valores mínimo y máximo
			x_min = min(x)
			x_max = max(x)
			# Calcular los puntos de corte en intervalos de ancho igual
			cut_points = np.linspace(x_min, x_max, num=cuts + 1)
		
		else:  # method == "equal_frequency"
			# calculamos cuantos elementos por tramo
			size = int(np.ceil(count / cuts))
			# ordenar
			sorted_x = sorted(x)

			cut_points = [sorted_x[0]]
			
			# Calculamos los puntos de corte basados en la cantidad de elementos en cada step
			for i in range(1, cuts):
				index = (i * size) - 1
				if index < count:
					cut_points.append(sorted_x[index])

			cut_points.append(sorted_x[-1]) 

    		# eliminar repetidos
			cut_points = sorted(set(cut_points))
			
		return self.discretize(x, cut_points)

	def discretize(self, x, cut_points):
		'''
		Método auxiliar para generar tramos en un vector mediante los puntos de corte
		Parámetros: 
		  	x: (list) Vector numérico que se desea discretizar.
		  	cut_points: (list) Vector numérico con los puntos de corte.
			  
		Return: (object) Un objeto que contiene los valores discretizados y los puntos de corte.
		'''
		# el comienzo del primer tramo se suele considerar -∞ y el final del último como ∞
		cut_points_copy = cut_points.copy()
		cut_points_copy[0] = -np.inf
		cut_points_copy[-1] = np.inf
		
		# crear tramos
		trs = pd.cut(x, bins=cut_points_copy)
		
		#crear objeto para guardar tramos y puntos de corte
		result = {
			'valores': trs,
			'puntos': cut_points
		}
		
		return result

	def discretice_attribute(self, df, column, num_bins, method='equal_width'):
		'''
		Método para discretizar un atributo mediante los métodos "equal width" y "equal frecuency" 	
		Parámetros:                                         
			df: (dataframe) data.frame que se desea discretizar.   
			column: (str) Nombre de la columna/atributo a discretizar. 
			cuts: (int) Número de intervalos en los que se desea discretizar.	
			method: (str) String que indica el método de discretización a utilizar:             
					"equal_width" para igual anchura o "equal_frequency" para igual frecuencia. 

		Return: (object) Un objeto que contiene los valores discretizados y los puntos de corte.
		'''
		#exceptions check
		if df.empty:
			return df
		
		# discretizar
		result = self.discretice_vector(list(df[column]), num_bins, method)
		
		return result

	def discretice_dataframe(self, df, num_bins, method='equal_width'):
		'''
		Método para discretizar un data.frame mediante los métodos "equal width" y "equal frecuency"
		Parámetros:
			df: (dataframe) data.frame que se desea discretizar.
			num_bins: (int) Número de intervalos en los que se desea discretizar.
			method: (str) String que indica el método de discretización a utilizar.
					"equal_width" para igual anchura o "equal_frequency" para igual frecuencia.

		Return: (dataframe) Mismo objeto de entrada con los atributos discretizados.
		'''
		#exceptions check
		if df.empty:
			return df
		
		if method not in ["equal_width", "equal_frequency"]:
			raise ValueError("Nombre de método inválido. Use 'equal_width' o 'equal_frequency'.")
		
		# Obtener nombres de columnas numéricas
		numeric_columns = df.select_dtypes(include=[np.number,int,float]).columns
		if len(numeric_columns) == 0:
			raise ValueError("No hay columnas numéricas para discretizar.")
		
		# Discretizar cada columna numérica
		discreticed_results = {
			col: self.discretice_attribute(df, col, num_bins, method)['valores']
			for col in numeric_columns
		}
		
		# Actualizar el DataFrame con las columnas discretizadas
		for col, discreticed_col in discreticed_results.items():
			df[col] = discreticed_col
		
		return df