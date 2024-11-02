source("2_metrics.R")
source("5_correlation.R")

###########################################################################################
# Método para mostrar el plot del AUC de una variable                                     #
# ****************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  #
#                                                                                         #
# Función: calculate_plot_auc		                                                          #
# Parámetros:                                                                             #
#   variable: (vector) Vector numérico en el que se desea calcular el AUC.                #
#   target: (vector) target para el calculo supervisado.    						                  #
#                                                                                         #
###########################################################################################
calculate_plot_auc <- function(variable, target) {
  
  # conseguir datos para el plot AUC
  auc_data <- calculate_auc( variable, target )
  
  # Plotear la curva ROC
  plot(auc_data$FPR, auc_data$TPR, type = "l", col = "blue", lwd = 2,
       xlab = "False Positive Rate (FPR)", ylab = "True Positive Rate (TPR)",
       main = "Curva ROC")
  abline(a = 0, b = 1, lty = 2, col = "gray")  # Línea diagonal como referencia
  
  cat("AUC:", auc_data$AUC)
}

###########################################################################################
# Método para mostrar el plot de la matriz de correlación de un data.frame                #
# ****************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  #
#                                                                                         #
# Función: plot_correlation_heatmap		                                                    #
# Parámetros:                                                                             #
#   df: (data.frame) data.frame para el cálculo de la matriz de correlación.              #
#                                                                                         #
###########################################################################################
plot_correlation_heatmap <- function(df) {
  
  # Calcular correlación
  cor_matrix <- get_correlation(df)
  print(cor_matrix)
  n_count <- nrow(cor_matrix)
  
  # Configurar los límites del gráfico
  #par(mar = c(5, 4, 4, 2) + 0.1)  # Márgenes
  
  # Crear un plot vacío
  plot(c(0, n_count + 1), c(0, n_count + 1), type = "n", xaxt = "n", yaxt = "n", 
       xlab = "", ylab = "", main = "Mapa de Calor de Correlación/Información Mutua")
  
  # Dibujar el mapa de calor con la función ?rect
  # Asumimos que los valores están ya entre -1<->1 y asignamos color entre rojo<->azul
  for (i in 1:n_count) {
    for (j in 1:n_count) {
      color_value <- cor_matrix[i, j]
      # get color
      color <- rgb(1, 1, 1)
      if( is.numeric( color_value ) && !is.na(color_value) )
      {
        if (color_value > 0) {
          #safety check
          if( color_value > 0.99999 ) color_value = 0.999
          color <- rgb(1 - color_value, 1 - color_value, 1)  # Tonos de azul
        } else {
          if( color_value < -0.99999 ) color_value = -0.999
          color <- rgb(1, 1 + color_value, 1 + color_value)  # Tonos de rojo
        }
      }
      # pintar rectangulo
      rect(i - 0.5, j - 0.5, i + 0.5, j + 0.5, col = color, border = "white")
    }
  }
  
  # Añadir nombres en eje x (aparecen rotados por lo que usamos text, en vez de axis)
  axis(1, at = 1:n_count, labels = FALSE)  # Dibujar el eje sin etiquetas
  text(x = 1:n_count, y = par("usr")[3] - 0.3, labels = rownames(cor_matrix), adj = 1, xpd = TRUE)
  # Añadir nombres en eje y
  axis(2, at = 1:n_count, labels = colnames(cor_matrix), las = 2)
}