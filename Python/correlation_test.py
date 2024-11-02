import pandas as pd
import numpy as np

from correlation import Correlation
from utilities import Utilities

# Instanciar la clase Discretize
correlation = Correlation()

# TEST VARIABLES
df = pd.DataFrame({
    'x': np.random.normal(size=100),
    'y': np.random.normal(size=100),
    'a': pd.Series(np.random.choice(['A', 'B', 'C'], size=100)).astype('category'),
    'b': pd.Series(np.random.choice(['A', 'B', 'C'], size=100)).astype('category')
})

def test(df):
	Utilities.clean_console()
	test_result = correlation.get_correlation(df)
	print(test_result)

test(df)