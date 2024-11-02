# set script file directory as current path
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

#load methods
source("utilities.R")
source("5_correlation.R")

#clean env and console
clean()

# TEST VARIABLES
df <- data.frame(
  x = rnorm(100),
  y = rnorm(100),
  a = factor(sample(letters[1:3], 100, replace = TRUE)),
  b = factor(sample(letters[1:3], 100, replace = TRUE))
)

# Calcular correlación
results <- get_correlation(df)

# Imprimir resultados
print(results)