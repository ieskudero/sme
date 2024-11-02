# set script file directory as current path
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

#load methods
source("utilities.R")
source("6_plot.R")

#clean env and console
clean()

# TEST VARIABLES
v <- rnorm(100)
target <- sample(c(0, 1), 100, replace = TRUE)

df <- data.frame(
  a = rnorm(100),
  b = rnorm(100),
  c = rnorm(100),
  d = rnorm(100)
)

# Ver resultados
calculate_plot_auc(v, target)
# Ver resultados
plot_correlation_heatmap(df)
