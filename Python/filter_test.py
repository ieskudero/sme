import pandas as pd

from filter import Filter
from utilities import Utilities

# Instanciar la clase Discretize
filter = Filter()

# TEST VARIABLES
df = pd.DataFrame( {
  "categoria1": pd.Series(["A", "A", "B", "A", "B", "B"]).astype("category"),
  "categoria2": pd.Series(["X", "X", "X", "X", "X", "X"]).astype("category"),  # Entropía baja
  "valores": [10, 20, 30, 40, 50, 60],
  "texto": ["uno", "dos", "tres", "uno", "dos", "tres"]
})
threshold = 0.0001

def test(df, threshold):
	Utilities.clean_console()
	test_result = filter.filter_by_entropy(df, threshold)
	print(test_result)

test(df, threshold)