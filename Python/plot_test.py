import pandas as pd
import numpy as np

from plot import Plot

# Instanciar la clase Discretize
plot = Plot()

# TEST VARIABLES
v = np.random.normal(size=100)
target = np.random.choice([0, 1], size=100)

df = pd.DataFrame({
    'a': np.random.normal(size=100),
    'b': np.random.normal(size=100),
    'c': np.random.normal(size=100),
    'd': np.random.normal(size=100),
})

def test1(v,target):
	plot.calculate_plot_auc(v, target)

def test2(df):
	plot.plot_correlation_heatmap(df)

test1(v,target)
test2(df)
