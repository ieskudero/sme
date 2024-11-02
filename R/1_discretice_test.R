# set script file directory as current path
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

#load methods
source("utilities.R")
source("1_discretice.R")

#clean env and console
clean()

# TEST VARIABLES
v1 <- c(11.5, 10.2, 1.2, 0.5, 5.3, 20.5, 8.4)
v2 <- c(11.5, 15, 1.2, 0.5, 5.3, 20.5, 8.4)
df <- data.frame(valor1 = v1, valor2 = v2)
k <- 4


#TEST discretize_vector FUNCTION
clean_console()
test1_width <- discretice_vector(v1,k,"equal_width")
print(test1_width)
test1_freq <- discretice_vector(v1,k,"equal_frequency")
print(test1_freq)

#TEST discretice_attribute FUNCTION
clean_console()
test2_width <- discretice_attribute(df,"valor1",k,"equal_width")
print(test2_width)
test2_freq <- discretice_attribute(df,"valor1",k,"equal_frequency")
print(test2_freq)

#TEST discretice_dataframe FUNCTION
clean_console()
test3_width <- discretice_dataframe(df,k,"equal_width")
print(test3_width)
test3_freq <- discretice_dataframe(df,k,"equal_frequency")
print(test3_freq)