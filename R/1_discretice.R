#####################################################################################################
# Método auxliar para discretizar vectores mediante los métodos "equal width" y "equal frecuency" 	#
# **************************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  			    #
#                                                                                         			    #
# Función: discretice_vector                                                              			    #
# Parámetros:                                                                             			    #
#   x: (vector) Vector numérico que se desea discretizar.                                 			    #
#   cuts: (numeric) Número de intervalos en los que se desea discretizar.				  			            #
#   method: (character) String que indica el método de discretización a utilizar:         			    #
#           "equal_width" para igual anchura o "equal_frequency" para igual frecuencia.   			    #
#                                                                                         			    #
# Return: (list) Un objeto que contiene los valores discretizados y los puntos de corte.  			    #
#####################################################################################################
discretice_vector <- function(x, cuts, method="equal_width") {
	
  #exceptions check
  if( class(x) != "numeric" ) stop( "use a numeric vector" )
  count <- length(x)
  if( count <=1 ) stop( "use a vector with more than one element" )
  if( method != "equal_width" && method != "equal_frequency" ) stop("Method name invalid. Use 'equal_width' o 'equal_frequency'.")
  
  streches <- vector()
  cut_points <- vector()
  
  if( method == "equal_width" ) {
    
    # Encontramos los valores mínimo y máximo del vector x
    x_min <- min(x)
    x_max <- max(x)
    
    # Calculamos los puntos de corte
    cut_points <- seq(x_min, x_max, length.out = cuts + 1)
  } else {  #method == "equal_frequency"
    
	  # calculamos cuantos elementos por tramo
    size <- ceiling( count / cuts )
    
    # Cogemos el vector ordenado
    sorted_x <- sort(x)
    
    # Creamos vector para almacenar los puntos de corte. Metemos el primer y último valor como min y max
    cut_points <- numeric(cuts + 1)
    cut_points[1] <-sorted_x[1]
    cut_points[length(cut_points)] <- sorted_x[length(sorted_x)]
    
    # Calculamos los puntos de corte basados en la cantidad de elementos en cada step
    for (i in 2:cuts) {
      index <- (i - 1) * size  # Índice de cada step será el punto de corte
      if (index <= count) {
        cut_points[i] <- sorted_x[min(index, count)]  # Aseguramos que no se salga del rango
      }
    }
    
    # eliminar repetidos
    cut_points <- unique(cut_points)
  }
  
  return (discretice(x, cut_points))
}


###########################################################################################
# Método auxiliar para generar tramos en un vector mediante los puntos de corte           #
# ****************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  #
#                                                                                         #
# Función: discretice		                                                                  #
# Parámetros:                                                                             #
#   x: (vector) Vector numérico que se desea discretizar.                                 #
#   cut.points: (vector) Vector numérico con los puntos de corte.						              #
#                                                                                         #
# Return: (list) Un objeto que contiene los valores discretizados y los puntos de corte.  #
###########################################################################################
discretice <- function(x, cut.points) {
  
  # el comienzo del primer tramo se suele considerar -∞ y el final del último como ∞
  cut_points_copy <- rep(cut.points)
  cut_points_copy[1] <- -Inf
  cut_points_copy[length(cut_points_copy)] <- Inf
  
  # crear tramos
  streches <- cut(x, breaks = cut_points_copy)
  
  #crear objeto para guardar tramos y puntos de corte
  result <- list(valores=streches,puntos=cut.points)
  
  return (result)
}

#########################################################################################################
# Método para discretizar un atributo mediante los métodos "equal width" y "equal frecuency" 	          #
# ******************************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  				      #
#                                                                                         				      #
# Función: discretice_attribute                                                              				    #
# Parámetros:                                                                             				      #
#   df: (data.frame) data.frame que se desea discretizar.                                   				    #
#   column: (character) Nombre de la columna/atributo a discretizar.                                   	#
#   cuts: (numeric) Número de intervalos en los que se desea discretizar.				  				              #
#   method: (character) String que indica el método de discretización a utilizar:         				      #
#           "equal_width" para igual anchura o "equal_frequency" para igual frecuencia.   				      #
#                                                                                         				      #
# Return: (list) Un objeto que contiene los valores discretizados y los puntos de corte.  				      #
#########################################################################################################
discretice_attribute <- function(df, column, num.bins, method = "equal_width") {
  
  #exceptions check
  if( nrow(df) == 0 ) return (df)
  
  # discretizar
  result <- discretice_vector( df[[column]], num.bins, method )
  
  # Devolver el resultado
  return(result)
}

#########################################################################################################
# Método para discretizar un data.frame mediante los métodos "equal width" y "equal frecuency" 	        #
# ******************************************************************************************************#
# Autor/a: Ibon Eskudero                                                                  				      #
#                                                                                         				      #
# Función: discretice_dataframe                                                              				    #
# Parámetros:                                                                             				      #
#   df: (data.frame) data.frame que se desea discretizar.                                   				    #
#   num.bins: (numeric) Número de intervalos en los que se desea discretizar.				  				          #
#   method: (character) String que indica el método de discretización a utilizar:         				      #
#           "equal_width" para igual anchura o "equal_frequency" para igual frecuencia.   				      #
#                                                                                         				      #
# Return: (data.frame) Mismo objeto de entrada con los atributos discretizados.           				      #
#########################################################################################################
discretice_dataframe <- function(df, num.bins, method = "equal_width") {
  
  #exceptions check
  if( nrow(df) == 0 ) return (df)
  if( method != "equal_width" && method != "equal_frequency" ) stop("Method name invalid. Use 'equal_width' o 'equal_frequency'.")
  
  # Obtener nombres de columnas numéricas
  number_columns <- sapply(df, is.numeric)  
  if (!any(number_columns)) stop("No hay columnas numéricas para discretizar.")
  
  # discretizar. Evitar hacer un for por columna
  discreticed_results <- lapply(names(df)[number_columns], function(c) {
    discreticed <- discretice_attribute( df, c, num.bins, method )
  	return ( discreticed$valores )
  })
  
  # Devolver el data.frame actualizado. No devolvemos una copia, ya que puede haber columnas no numéricas que deveríamos copiar si no
  df[names(df)[number_columns]] <- discreticed_results
  
  # Devolver el data.frame actualizado
  return(df)
}