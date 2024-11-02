import pandas as pd
import numpy as np

from metrics import Metrics
from utilities import Utilities

# Instanciar la clase Discretize
metrics = Metrics()

# TEST VARIABLES
df = pd.DataFrame({
    'x': np.random.normal(size=100),
    'y': np.random.normal(size=100),
    'z': pd.Series(np.random.choice(['A', 'B'], size=100)).astype('category')
})

AUC_target = pd.DataFrame({
    'x': np.random.choice([0, 1], size=100),
    'y': np.random.choice([0, 1], size=100)
})

#TEST get_metricas FUNCTION
def test(df,AUC_target):
	Utilities.clean_console()
	test_result = metrics.get_metricas(df,AUC_target)
	print(test_result)

test(df,AUC_target)
