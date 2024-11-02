import pandas as pd

from normalize import Normalize
from utilities import Utilities

# Instanciar la clase Discretize
normalize = Normalize()

# TEST VARIABLES
df = pd.DataFrame( {# Caso con valores distintos e iguales
  "x": [10, 20, 30, 40, 50],
  "y":[5, 5, 5, 5, 5]
})

def test1(df):
  Utilities.clean_console()
  test_result = normalize.normalize(df)
  print(test_result)

def test2(df):
  Utilities.clean_console()
  test_result = normalize.standardize(df)
  print(test_result)

test1(df)
test2(df)
