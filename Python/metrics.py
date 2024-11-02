#############################################################################################
# Clase para sacar las métricas														  		#
# ******************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  	#
#                                                                                         	#
# Funciones: 				                                                              	#	
# 	get_metricas		                                                              		#
# 	calculate_auc																			#	
#############################################################################################
import numpy as np
import pandas as pd

#cargamos funciones matemáticas. El fichero debe estar en el mismo path que este fichero
from customMath import CustomMath

class Metrics:
	def __init__(self):
		pass
	def get_metricas(self,df,AUC_target):
		'''
		Método para conseguir las métricas de varianza,entropia y UAC de un dataframe
		Parámetros:
			df: (dataframe) data.frame para el que se desean generar métricas
			AUC_target: (dataframe) Si se desea calcular UAC para algún variable, hay que pasarle una variable
			            con igual nombre para calcular el target
		Return: (dataframe) Métricas para cada variable dependiendo de si es númerico discreto o no.
		'''
		result = {}
  		# Iteramos sobre cada columna del dataset
		for column in df.columns:
			# Calcular entropía para variables categóricas
			if df[column].dtype == 'object' or df[column].dtype.name == 'category':
				result[column] = {
					'Entropia': CustomMath.get_entropia(list(df[column]))
				}
			
			# Calcular varianza y AUC para variables numéricas
			elif pd.api.types.is_numeric_dtype(df[column]):
				varianza = CustomMath.get_varianza(list(df[column]))
				metrics = {
					'Varianza': varianza
				}

				# Verificar si se proporcionó un target para calcular AUC
				if AUC_target is not None and column in AUC_target.columns:
					auc_values = AUC_target[column]
					
					# Calcular AUC si el target es binario
					if len(auc_values.unique()) == 2:
						auc_data = self.calculate_auc(list(df[column]), auc_values)
						metrics['AUC'] = auc_data['AUC']
				
				# Agregar métricas calculadas al resultado
				result[column] = metrics

		return result
	
	def calculate_auc(self,predictions,target):
		'''
		Método auxiliar para calcular el AUC de una variable
		Parámetros:
			predictions: (list) Vector numérico en el que se desea calcular el AUC.
			target: (list) target para el calculo supervisado.
		
		Return: (object) Object con AUC=valor AUC, TPR=positive rate y FPR=negative rate.
		'''
		 # Verificar que el target sea binario
		if len(np.unique(target)) != 2:
			raise ValueError("La variable clase debe ser binaria.")
		
		# Ordenar predicciones y las clases reales, orden ascendente
		order_index = np.argsort(predictions)[::-1]
		predictions = np.array(predictions)[order_index]
		target = np.array(target)[order_index]
		
		# Convertir la clase binaria a 0 y 1 si no lo está
		unique_classes = np.unique(target)
		target = np.where(target == unique_classes[1], 1, 0)
		
		# Inicializar contadores para TP, FP, FN, TN
		total_pos = np.sum(target == 1)
		total_neg = np.sum(target == 0)
		tpr = np.zeros(len(target) + 1)
		fpr = np.zeros(len(target) + 1)
		
  		# Iterar sobre los puntos de corte para calcular TPR y FPR
		for i in range(len(target)):
			tp = np.sum(target[:i+1] == 1)  # Verdaderos Positivos
			fp = np.sum(target[:i+1] == 0)  # Falsos Positivos
			
			tpr[i + 1] = (tp / total_pos).item()  # TPR: Sensibilidad, positive rate
			fpr[i + 1] = (fp / total_neg).item()  # FPR: Negative rate (1 - TPR)
		
		# Calcular el AUC usando el método del trapecio
		auc_value = np.sum(np.diff(fpr) * (tpr[1:] + tpr[:-1]) / 2)
		
		return {
			'AUC': auc_value.item(),
			'TPR': tpr,
			'FPR': fpr
		}
