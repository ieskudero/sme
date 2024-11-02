#cargamos funciones matemáticas. El fichero debe estar en el mismo path que este fichero
source("math.R")

#########################################################################################################
# Método para conseguir las métricas de varianza,entropia y UAC de un dataframe                	        #
# ******************************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  				      #
#                                                                                         				      #
# Función: get_metricas                                                                      				    #
# Parámetros:                                                                             				      #
#   df: (data.frame) data.frame para el que se desean generar métricas                       				    #
#   AUC_target: (data.frame) Si se desea calcular UAC para algún variable, hay que pasarle una variable #
#               con igual nombre para calcular el target                                                #
# Return: (data.frame) Métricas para cada variable dependiendo de si es númerico discreto o no. 	      #
#########################################################################################################
get_metricas <- function(df, AUC_target = data.frame()) {
  result <- list()
  
  # Iteramos sobre cada columna del dataset
  for (c in colnames(df)) {
    # entropia para variables discretas. Asumimos que son discretos = enumerables (factor)
    if (is.factor(df[[c]]) || is.character(df[[c]])) {
      result[[c]] <- list(Entropia = get_entropia( df[[c]] ) )
    }
    else if (is.numeric(df[[c]])) {
      varianza <- get_varianza( df[[c]] )
      # Miramos si nos han pasado una variable clase binaria para calcular AUC. 
      # Asumimos que nos enviaran una variable con el mismo nombre de comlumna
      if( !is.null( AUC_target[[c]] )) {
        auc_values <- AUC_target[[c]]
        if (length(unique(auc_values)) == 2) {
          # Calcular AUC si la clase es binaria
          auc_data <- calculate_auc(df[[c]], auc_values)
          result[[c]] <- list(Varianza = varianza , AUC = auc_data$AUC)
        }
      } else {
        result[[c]] <- list( Varianza = varianza )
      }
    }
  }
  
  return( result )
}

###########################################################################################
# Método auxiliar para calcular el AUC de una variable                                    #
# ****************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  #
#                                                                                         #
# Función: calculate_auc		                                                              #
# Parámetros:                                                                             #
#   predictions: (vector) Vector numérico en el que se desea calcular el AUC.             #
#   target: (vector) target para el calculo supervisado.    						                  #
#                                                                                         #
# Return: (list) list con AUC=valor AUC, TPR=positive rate y FPR=negative rate.           #
###########################################################################################
# Función privada auxiliar para calcular el AUC manualmente
calculate_auc <- function(predictions, target) {
  # Verificar que la variable de clase sea binaria
  if (length(unique(target)) != 2) {
    stop("La variable clase debe ser binaria.")
  }
  
  # Ordenar los valores de predicciones y las clases reales
  order_index <- order(predictions, decreasing = TRUE)
  predictions <- predictions[order_index]
  target <- target[order_index]
  
  # Convertir la clase binaria a 0 y 1 si no lo está
  target <- as.numeric(factor(target, levels = unique(target))) - 1
  
  # Inicializamos contadores para TP, FP, FN, TN
  total_pos <- sum(target == 1)
  total_neg <- sum(target == 0)
  tpr <- fpr <- numeric(length(target) + 1)
  
  # Iterar sobre los puntos de corte para calcular TPR y FPR
  for (i in seq_along(target)) {
    tp <- sum(target[1:i] == 1)  # Verdaderos Positivos
    fp <- sum(target[1:i] == 0)  # Falsos Positivos
    
    tpr[i + 1] <- tp / total_pos  # TPR: Sensibilidad, positive rate
    fpr[i + 1] <- fp / total_neg  # FPR: Negative rate (1 - TPR)
  }
  
  # Calcular el AUC usando el método del trapecio
  auc_value <- sum(diff(fpr) * (tpr[-1] + tpr[-length(tpr)]) / 2)
  
  result <- list(AUC=auc_value,TPR=tpr,FPR=fpr)
  
  return( result )
}