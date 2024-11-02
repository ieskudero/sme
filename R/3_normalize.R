#cargamos funciones matemáticas. El fichero debe estar en el mismo path que este fichero
source("math.R")

#########################################################################################################
# Método para normalizar un dataframe                                                         	        #
# ******************************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  				      #
#                                                                                         				      #
# Función: normalize                                                                        				    #
# Parámetros:                                                                             				      #
#   df: (data.frame) data.frame para normalizar                                              				    #
# Return: (data.frame) data.frame normalizado. Solo normaliza columnas numéricas.                	      #
#########################################################################################################
normalize <- function(df) {
  # Identificar las columnas numéricas
  numeric_cols <- sapply(df, is.numeric)
  
  # Normalizar cada columna numérica
  df[numeric_cols] <- lapply(df[numeric_cols], normalize_variable)
  
  return(df)
}

#########################################################################################################
# Método para estandarizar un dataframe                                                         	      #
# ******************************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  				      #
#                                                                                         				      #
# Función: normalize                                                                        				    #
# Parámetros:                                                                             				      #
#   df: (data.frame) data.frame para estandarizar                                            				    #
# Return: (data.frame) data.frame estandarizado. Solo estandariza columnas numéricas.            	      #
#########################################################################################################
standardize <- function(df) {
  # Identificar las columnas numéricas
  numeric_cols <- sapply(df, is.numeric)
  
  # Estandarizar cada columna numérica
  df[numeric_cols] <- lapply(df[numeric_cols], standardize_variable)
  
  return(df)
}