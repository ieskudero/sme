#cargamos funciones matemáticas. El fichero debe estar en el mismo path que este fichero
source("math.R")

#########################################################################################################
# Método para calcular la correlación en un data.frame en base al tipo de variable            	        #
# ******************************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  				      #
#                                                                                         				      #
# Función: get_correlation                                                                				      #
# Parámetros:                                                                             				      #
#   df: (data.frame) data.frame para correlacionar                                           				    #
#   max_values: (numeric) cantidad máxima de opciones únicas de un factor a tener en cuenta para ser    #
#                         considerado como variable categórica                                          #
# Return: (matrix) matriz de correlaciones                                                              #
#########################################################################################################
get_correlation <- function(df, max_values = 5)
{
  # Nombres de las columnas
  c_names <- names(df)
  
  # Longitud de las variables
  count <- length(c_names)
  
  # Crear una matriz vacía countxcount para almacenar las correlaciones
  cor_m <- matrix(NA, nrow = count, ncol = count)
  rownames(cor_m) <- c_names
  colnames(cor_m) <- c_names
  
  # Calcular la correlación para cada par de columnas
  for (i in 1:count) {
    for (j in i:count) {
      v1 <- df[[c_names[i]]]
      v2 <- df[[c_names[j]]]
      
      corr <- NA
      if (is.numeric(v1) && is.numeric(v2)) {  # Correlación de Pearson
        corr <- get_pearson_cor(v1, v2)
      } else if (is.factor(v1) && is.factor(v2) && 
                 length(unique(v1)) <= max_values && 
                 length(unique(v2)) <= max_values) {  # Información mutua
        corr <- get_mutual_information_cor(v1, v2)
      }
      
      # Asignar la correlación de forma simétrica
      cor_m[i, j] <- corr
      cor_m[j, i] <- corr
    }
  }
  
  return( cor_m )
}