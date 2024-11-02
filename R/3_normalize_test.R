# set script file directory as current path
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

#load methods
source("utilities.R")
source("3_normalize.R")

#clean env and console
clean()

# TEST VARIABLES
df <- data.frame( # Caso con valores distintos e iguales
  x=c(10, 20, 30, 40, 50),
  y=c(5, 5, 5, 5, 5)
)

#TEST normalize FUNCTION
n <- normalize(df)

# Imprimir resultados
print("Valores originales:")
print(df)
print("Valores normalizados:")
print(n)

clean_console()

#TEST standardize FUNCTION
n <- standardize(df)

# Imprimir resultados
print("Valores originales:")
print(df)
print("Valores estandarizados:")
print(n)
