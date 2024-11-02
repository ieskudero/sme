import pandas as pd

from discretize import Discretize
from utilities import Utilities

# Instanciar la clase Discretize
discretizer = Discretize()

# Crear datos de prueba
v1 = [11.5, 10.2, 1.2, 0.5, 5.3, 20.5, 8.4]
v2 = [11.5, 15, 1.2, 0.5, 5.3, 20.5, 8.4]
k = 4

#TEST discretize_vector FUNCTION
def test1( v,k):
	Utilities.clean_console()
	test1_width = discretizer.discretice_vector(v,k,"equal_width")
	print(test1_width)
	test1_freq = discretizer.discretice_vector(v,k,"equal_frequency")
	print(test1_freq)

#TEST discretice_attribute FUNCTION
def test2(v1,v2,k):
	Utilities.clean_console()
	df = pd.DataFrame( { 'valor1': v1, 'valor2': v2 } )
	test2_width = discretizer.discretice_attribute(df,"valor1",k,"equal_width")
	print(test2_width)
	df = pd.DataFrame( { 'valor1': v1, 'valor2': v2 } )
	test2_freq = discretizer.discretice_attribute(df,"valor1",k,"equal_frequency")
	print(test2_freq)

#TEST discretice_dataframe FUNCTION
def test3(v1,v2,k):
	Utilities.clean_console()
	df = pd.DataFrame( { 'valor1': v1, 'valor2': v2 } )
	test3_width = discretizer.discretice_dataframe(df,k,"equal_width")
	print(test3_width)
	df = pd.DataFrame( { 'valor1': v1, 'valor2': v2 } )
	test3_freq = discretizer.discretice_dataframe(df,k,"equal_frequency")
	print(test3_freq)

test1(v1,k)
test2(v1,v2,k)
test3(v1,v2,k)