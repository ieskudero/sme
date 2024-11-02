import os

class Utilities:
	def __init__(self):
		pass

	@staticmethod
	def clean_console():
		"""
		Método auxiliar para borrar la consola
		"""
		os.system('cls' if os.name == 'nt' else 'clear')
