# set script file directory as current path
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

#load methods
source("utilities.R")
source("4_filter.R")

#clean env and console
clean()

# TEST VARIABLES
df_test <- data.frame(
  categoria1 = factor(c("A", "A", "B", "A", "B", "B")),
  categoria2 = factor(c("X", "X", "X", "X", "X", "X")),  # Entropía baja
  valores = c(10, 20, 30, 40, 50, 60),
  texto = c("uno", "dos", "tres", "uno", "dos", "tres")
)
threshold <- 0.0001

# Filtrar columnas con entropía muy baja, rondando el 0
df_filtered <- filter_by_entropy(df_test, threshold)

# Imprimir resultado
print("Dataset original:")
print(df_test)

print("Dataset filtrado por entropía:")
print(df_filtered)
