# set script file directory as current path
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

#load methods
source("utilities.R")
source("2_metrics.R")

#clean env and console
clean()

# TEST VARIABLES
df <- data.frame(
  x = rnorm(100),
  y = rnorm(100),
  z = factor(sample(c("A", "B"), 100, replace = TRUE))
)

AUC_target <- data.frame(
  x = sample(c(0, 1), 100, replace = TRUE),
  y = sample(c(0, 1), 100, replace = TRUE)
)


#TEST get_metricas FUNCTION
metrics <- get_metricas(df, AUC_target = AUC_target)

# Ver resultados
print(metrics)