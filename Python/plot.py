#############################################################################################
# Clase dibujar plots de AUC y matriz de correlación			                            #		
# ******************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  	#
#                                                                                         	#
# Funciones: 				                                                              	#	
# 	calculate_plot_auc		                                                           		#
# 	plot_correlation_heatmap                                                           		#
#############################################################################################
import matplotlib.pyplot as plt

from metrics import Metrics
from correlation import Correlation

import numpy as np

class Plot:
	def __init__(self):
		self.metr = Metrics()
		self.corr = Correlation()
		pass

	def calculate_plot_auc(self,variable, target):
		"""
		Método para mostrar el plot del AUC de una variable
		Parámetros:
			variable: (list) Vector numérico en el que se desea calcular el AUC.
			target: (list) target para el calculo supervisado.
		"""
		# conseguir datos para el plot AUC
		auc_data = self.metr.calculate_auc(variable, target)
		
		# Plotear la curva ROC
		plt.plot(auc_data['FPR'], auc_data['TPR'], color="blue", linewidth=2, label="ROC curve")
		plt.plot([0, 1], [0, 1], linestyle="--", color="gray")  # Línea diagonal como referencia
		plt.xlabel("False Positive Rate (FPR)")
		plt.ylabel("True Positive Rate (TPR)")
		plt.title("Curva ROC")
		plt.legend()
		plt.show()
		
		print("AUC:", auc_data['AUC'])

	def plot_correlation_heatmap(self,df):
		"""
		Método para mostrar el plot de la matriz de correlación de un data.frame
		Parámetros:
			df: (dataframe) dataframe para el cálculo de la matriz de correlación.
		"""
		# Calcular lcorrelación
		cor_matrix = self.corr.get_correlation(df)
		print(cor_matrix)
		n_count = cor_matrix.shape[0]

		# Crear un plot vacío
		fig, plot = plt.subplots()
		plot.set_title("Mapa de Calor de Correlación/Información Mutua")
		
		# Asumimos que los valores están ya entre -1<->1 y asignamos color entre rojo<->azul
		for i in range(n_count):
			for j in range(n_count):
				color_value = cor_matrix[i, j]
				color = (1, 1, 1)  # Blanco por defecto
				if isinstance(color_value, (int, float)) and not np.isnan(color_value):
					if color_value > 0:
						# safety check
						if (color_value > 0.99999):
							color_value = 0.999
						color = (1 - color_value, 1 - color_value, 1)  # Tonos de azul
					else:
						# safety check
						if (color_value < -0.99999):
							color_value = -0.999
						color = (1, 1 + color_value, 1 + color_value)  # Tonos de rojo

				# Dibujar el rectángulo
				plot.add_patch(plt.Rectangle((i, j), 1, 1, color=color, edgecolor="white"))
		
		plt.xticks(ticks=np.arange(n_count) + 0.5, labels=df.columns)
		plt.yticks(ticks=np.arange(n_count) + 0.5, labels=df.columns)
		
		plt.show()
