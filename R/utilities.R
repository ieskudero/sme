clean_console <- function() {
  # clear console
  cat("\014")
}

clean_env <- function() {
  # get all objects in the global environment
  objs <- ls(envir = .GlobalEnv)
  
  # filter out functions, keeping only non-function objects (variables)
  vars <- objs[sapply(objs, function(x) !is.function(get(x, envir = .GlobalEnv)))]
  
  # remove only the variables from the global environment
  rm(list = vars, envir = .GlobalEnv)
}

clean <- function() {
  clean_console()
  clean_env()
}

readFile <- function( filePath ) {
  result <- read.table(filePath, sep=";",
                       header=TRUE,
                       stringsAsFactors=FALSE, 
                       fileEncoding="latin1", encoding="UTF-8",quote="\"")
  return (result)
}

readFilesFromFolder <- function(folder) {
  # read files
  files <- list.files(path=folder, all.files=FALSE, full.names=TRUE)
  
  # TODO: make this recursive to iterate over subfolders
  
  #read first for headers
  result <- readFile(files[1])
  
  for( i in 2:length(files) ) {
    # read nexts
    dat <- readFile(files[i])
    
    # merge
    result <- rbind(result,dat, deparse.level = 0)
  }
  
  return (result) 
}