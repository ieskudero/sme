#cargamos funciones matemáticas. El fichero debe estar en el mismo path que este fichero
source("math.R")

#########################################################################################################
# Método para filtar un data.frame en base a un threshold de entropía                          	        #
# ******************************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  				      #
#                                                                                         				      #
# Función: filter_by_entropy                                                                				    #
# Parámetros:                                                                             				      #
#   df: (data.frame) data.frame para filtar                                                 				    #
#   threshold: (numeric) Threshold para filtar por entropia                                  				    #
# Return: (data.frame) data.frame filtrado, eliminando las variables que no hayan superado el threshold #
#########################################################################################################
filter_by_entropy <- function( df, threshold )
{
  result <- df[0]
  
  # Iteramos sobre cada columna del dataset. Solo filtramos aquellas columnas que cumplan:
  # 1.- sean tipo factor
  # 2.- estén por debajo del threshold
  for (c in colnames(df)) {
    if (is.factor(df[[c]]) || is.character(df[[c]])) {
      entr <- get_entropia( df[[c]] )
      if ( entr < threshold ) next
    }
    
    result[[c]] <- df[[c]]
  }
  
  return( result )
}