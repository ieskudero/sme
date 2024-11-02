import numpy as np

class CustomMath:

	@staticmethod
	def get_entropia(fact):
		"""
		Método auxiliar para calcular la entropía
		Parámetros:
			fact: (list) vector con los valores de la categoría
		Return: (float) entropía
		"""
		# Calcular las frecuencias de cada categoría(panda Series || string list)
		f, counts = np.unique(fact, return_counts=True)
		prob = counts / counts.sum()
		# Añadimos un pequeño valor para evitar log(0)
		return -np.sum(prob * np.log2(prob + 1e-9)).item() 

	@staticmethod
	def get_varianza(x):
		"""
		Método auxiliar para calcular la varianza
		Parámetros: 
			x: (list) vector numérico para el cálculo de la varianza.
		Return: (float) varianza
		"""
		# Convertir array y borrar NaNs
		npx = np.array([val for val in x if val is not None])

		# media
		mean_x = CustomMath.media_variable(x)

		# suma de diferencias respecto a la media al cuadrado dividivo entre n-1
		varianza = np.sum((npx - mean_x) ** 2) / (len(npx) - 1) if len(npx) > 1 else 0

		return varianza.item()

	@staticmethod
	def normalize_variable(x):
		"""
		Método auxiliar para normalizar valores
		Parámetros: 
			x: (list) vector numérico a normalizar entre 0 y 1
		Return: (list) vector normalizado
		"""
		x = np.array(x)
		if not np.issubdtype(x.dtype, np.number):
			raise ValueError("La variable debe ser numérica")
		
		if len(np.unique(x)) == 1:
			return np.zeros_like(x)  # Retorna un array de ceros si todos los valores son iguales
		
		# Normalización entre 0 y 1
		return (x - np.min(x)) / (np.max(x) - np.min(x)).item()
	
	@staticmethod
	def standardize_variable(x):
		"""
		Método auxiliar para la estandarización de valores (media=0, desviación estándar=1)
		Parámetros: 
			x: (list) vector numérico a estandarizar
		Return: (list) vector estandarizado
		"""
		npx = np.array(x)
		if not np.issubdtype(npx.dtype, np.number):
			raise ValueError("La variable debe ser numérica")
		
		if len(np.unique(x)) == 1:
			return np.zeros_like(x)  # Retorna un array de ceros si todos los valores son iguales
		
		media_x = CustomMath.media_variable(x)
		sd_x = CustomMath.sd_variable(x)
		return (x - media_x) / sd_x
	
	@staticmethod
	def media_variable(x):
		"""
		Método auxiliar para lcalcular la media
		Parámetros: 
			x: (list) vector numérico para el cálculo de la media
		Return: (float) media
		"""
		npx = np.array(x)
		if not np.issubdtype(npx.dtype, np.number):
			raise ValueError("La variable debe ser numérica")
		
		return (np.sum(x) / len(x)).item()
	
	@staticmethod
	def sd_variable(x):
		"""
		Método auxiliar para lcalcular la desviación estandard
		Parámetros: 
			x: (list) vector numérico para el cálculo de la desviación estandard
		Return: (float) desviación estandard
		"""
		npx = np.array(x)
		if not np.issubdtype(npx.dtype, np.number):
			raise ValueError("La variable debe ser numérica")
		
		varianza = CustomMath.get_varianza(x)

		return np.sqrt(varianza).item()
	
	@staticmethod
	def get_pearson_cor(x, y):
		"""
		Método auxiliar para calcular la correlación de pearson
		Parámetros:
			x: (list) vector numérico para el cálculo de la correlación
			x: (list) vector numérico para el cálculo de la correlación
		Return: (float) correlación de pearson
		"""
		npx, npy = np.array(x), np.array(y)
		
		if not (np.issubdtype(npx.dtype, np.number) and np.issubdtype(npy.dtype, np.number)):
			raise ValueError("Las variables deben ser numéricas")
		
		mean_x, mean_y = CustomMath.media_variable(x), CustomMath.media_variable(y)
		
		# Calcular la suma de las desviaciones. Covarianza
		cov_xy = np.sum((x - mean_x) * (y - mean_y)) / (len(x) - 1) if len(x) > 1 else 0
		
		return (cov_xy / (CustomMath.sd_variable(x) * CustomMath.sd_variable(y))).item()
	
	@staticmethod
	def get_mutual_information_cor(x, y):
		"""
		Método auxiliar para calcular la información mutua entre dos variables categóricas
		Parámetros:
			x: (list) vector str para el cálculo de la información mutua
			x: (list) vector str para el cálculo de la información mutua
		Return: (float) información mutua
		"""
		# Crear tabla de contingencia
		joint_freq = {}
		for xi, yi in zip(x, y):
			joint_freq[(xi, yi)] = joint_freq.get((xi, yi), 0) + 1
		
		total = len(x)
		
		# Calculamos frecuencias
		px = {}
		py = {}
		for (xi, yi), count in joint_freq.items():
			px[xi] = px.get(xi, 0) + count
			py[yi] = py.get(yi, 0) + count
		
		# Convertimos a probabilidades marginales
		px = {k: v / total for k, v in px.items()}
		py = {k: v / total for k, v in py.items()}
		joint_prob = {k: v / total for k, v in joint_freq.items()}
		
		# Calcular la información mutua
		result = 0
		for (xi, yi), pxy in joint_prob.items():
			if pxy > 0:
				result += pxy * np.log2(pxy / (px[xi] * py[yi]))
		
		return result
