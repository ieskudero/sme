# Función auxiliar para calcular la entropía
get_entropia <- function(fact) {
  f <- table( fact )
  prob <- f / sum(f)
  return(-sum(prob * log2(prob + 1e-9)))  # Añadimos un pequeño valor para evitar log(0)
}

# Función auxiliar para calcular la varianza
get_varianza <- function(x) {
  # por si acaso, eliminamos NAs
  x <- x[!is.na(x)]
  
  # media
  mean_x <- media_variable(x)
  
  # suma de diferencias respecto a la media al cuadrado dividivo entre n-1
  varianza <- ( sum((x - mean_x) ^ 2) ) / (length(x) - 1)
  
  return( varianza )
}

# Función auxiliar para normalizar valores
normalize_variable <- function(x)
{
  # Safety check
  if (!is.numeric(x)) stop("La variable debe ser numérica")
  
  if (length(unique(x)) == 1) {
    return(rep(0, length(x)))  # Assign 0 or NA if only one unique value
  }
  
  return((x - min(x, na.rm = TRUE)) / (max(x, na.rm = TRUE) - min(x, na.rm = TRUE)))
}

# Función auxiliar para estandarizar valores
standardize_variable <- function(x)
{
  # Safety check
  if (!is.numeric(x)) stop("La variable debe ser numérica")
  
  if (length(unique(x)) == 1) {
    return(rep(0, length(x)))  # Assign 0 or NA if only one unique value
  }
  
  # Estandarización
  return ( (x - media_variable(x)) / sd_variable(x) )
}

# Función auxiliar para sacar la media
media_variable <- function(x)
{
  # Safety check
  if (!is.numeric(x)) stop("La variable debe ser numérica")
  
  return( sum(x, na.rm = TRUE) / length(x) )
}

# Función auxiliar para sacar la desviación estandard
sd_variable <- function(x)
{
  # Safety check
  if (!is.numeric(x)) stop("La variable debe ser numérica")
  
  # Calcular la varianza
  varianza <- get_varianza(x)
  
  # Desviación estándar como la raíz cuadrada de la varianza
  return ( sqrt(varianza) )
}

# Función auxiliar para calcular la correlación de pearson
get_pearson_cor <- function(x, y)
{
  # Safety check
  if (!is.numeric(x) || !is.numeric(y)) stop("Las variables deben ser numéricas")
  
  # Calcular las medias de los dos variablaes
  mean_x <- media_variable(x)
  mean_y <- media_variable(y)
  
  # Calcular la suma de las desviaciones
  cov_xy <- sum((x - mean_x) * (y - mean_y)) / (length(x) - 1)
  
  # desviación estándar de x y y
  sd_x <- sd_variable(x)
  sd_y <- sd_variable(y)
  
  return(cov_xy / (sd_x * sd_y))
}

# Función auxiliar para calcular la información mutua entre dos variables categóricas
get_mutual_information_cor <- function(x, y)
{
  # Safety check
  if (!is.factor(x) || !is.factor(y)) stop("Las variables deben ser categóricas")
  
  # Crear contingency table
  joint_table <- table(x, y) / length(x)
  
  # Probabilidades marginales
  px <- rowSums(joint_table)
  py <- colSums(joint_table)
  
  # Calcular la información mutua
  result <- 0
  for (i in seq_along(px)) {
    for (j in seq_along(py)) {
      if (joint_table[i, j] > 0) {
        result <- result + joint_table[i, j] * log2(joint_table[i, j] / (px[i] * py[j]))
      }
    }
  }
  return( result )
}