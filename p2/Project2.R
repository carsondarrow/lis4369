rm(list = ls(envir = globalenv()), envir = globalenv()); if(!is.null(dev.list())) dev.off(); gc(); cat("\014")
sink("lis4369_p2_requirements_output", append=FALSE, split=TRUE)

cat("###################################################################################","\n")
cat("R Language Reference Notes:\n",
    "\tUse head and tail to look at first few and last few records.\n",
    "\tUse str and names to look at structure and column names of a data frame.\n",
    "\tUse $ notation to look at a particular column name.\n",
    "\tUse [] square brakcets (row,column) notation to look at a particular value.\n\n",
    "\tAlso, conditional section in R:\n",
    "\tSelect data in I row and J column (one field) for DataFrameX: DataFrame[I,J]\n",
    "\tAlternatively:\n",
    "\tData in I row: DataFrameX[I,] # display row/record I with column names\n",
    "\tData in J column: DataFrameX$J_Column_Name, or DataFrameX[,J]\n",
    "\tNOTE: R uses 1 for first record/row. Pyton uses 0!",
    "\n\n")

cat("*** Assignment Requirements ***","\n\n")

cat("1. Use Assignment 5 Screenshots and R Manual to backward-engineer the following requirements:","\n")

cat("2. Resources:\n",
    "\ta. R Manual: https://cran.r-project.org/doc/manuals/r-release/R-lang.pdf\n",
    "\tb. b. R for Data Science: https://r4ds.had.co.nz/", "\n")

cat("3. Use Motor Trend Car Road Tests data:\n",
    "\ta. Research the data! https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html\n",
    "\tb. url = \"http://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv\"", "\n")

cat("Note: Use variable \"mtcars\" to read file into. (See Assignment 5 for reading .csv files.)","\n")
cat("###################################################", "\n\n")

url = "http://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv"
mtcars <- read.csv(file=url,head=TRUE,sep=",")

cat("*** Report/Command Requirements ***","\n")

cat("1) Display all data from file:","\n")
mtcars

cat("\n", "2) Display 1st 10 records:","\n")
head(mtcars,10)

cat("\n", "3.) Display last 10 records:","\n")
tail(mtcars,10)

cat("\n", "4) Display file structure (see notes above):","\n")
str(mtcars)

cat("\n", "5) Display column names (see notes above):","\n")
names(mtcars)

cat("\n", "6) Display 1st record/row with column names (see notes above):","\n")
mtcars[1,]

cat("\n", "7) Display 2nd column data (mpg), using column number:","\n",
    "Note: does *not* include column name", "\n")
mtcars[2,]

cat("\n", "8) Display column data (cyl), using column name:","\n",
    "Note: return does *not* display column name","\n")
mtcars$cyl

cat("\n", "9) Display row/column data (3,4), that is, one field, using square bracket notation (see above):","\n")
mtcars[3,4]

cat("\n", "10) Display all data for cars having greater than 4 cylinders:","\n")
mtcars[mtcars$cyl>4,]

cat("\n", "11) Display all data for cars having greater than 4 cylinders *and* greater than 4 gears:","\n")
mtcars[mtcars$cyl>4 &mtcars$gear>4,]

cat("\n", "12) Display all cars having more than 4 cylinders *and* exactly 4 gears:","\n")
mtcars[mtcars$cyl>4 &mtcars$gear==4,]

cat("\n", "13) Display all cars having more than 4 cylinders *or* exactly 4 gears:","\n")
mtcars[mtcars$cyl>4 |mtcars$gear==4,]

cat("\n", "14) Display all cars having more than 4 cylinders that do *not* have 4 gears:","\n")
mtcars[mtcars$cyl>4 &mtcars$gear!=4,]

cat("\n", "15) Display total number of rows (only the number):","\n")
nrow(mtcars)

cat("\n", "16) Display total number of columns (only the number):","\n")
ncol(mtcars)

cat("\n", "17) Display total number of dimensions (i.e. rows and columns):","\n")
dim(mtcars)

cat("\n", "18) Display data frame structure - same as info in Python:","\n")
str(mtcars)

cat("\n", "19) Get mean, median, minimum, maximum, quantiles, variance, and standard deviation of horsepower:","\n",
    "Note: Remove any missing values.\n")

cat("\t","a. Mean: ")
mean(mtcars$hp, na.rm=TRUE)

cat("\t", "b. Median: ")
median(mtcars$hp, na.rm=TRUE)

cat("\t", "c. Min: ")
min(mtcars$hp, na.rm=TRUE)

cat("\t", "d. Max: ")
max(mtcars$hp, na.rm=TRUE)

cat("\t", "e. Quantile:\n")
quantile(mtcars$hp, na.rm=TRUE)

cat("\t", "f. Variance: ")
var(mtcars$hp, na.rm=TRUE)

cat("\t", "g. Standard Deviation: ")
sd(mtcars$hp, na.rm=TRUE)

cat("\t", "20) summary() function prints min, max, mean, median, and quantiles (also, numbers of NA's, if any.):","\n")
summary(mtcars$hp, na.rm=TRUE)

cat("\t", "Two plots (*must* include *your* name in title): 1) Uses qplot(); 2) Uses plot()","\n")
library(ggplot2)

png("plot_disp_and_mpg_1.png")
qplot(disp, mpg, data=mtcars,
      xlab="Displacement",
      ylab="MPG",
      colour = cyl,
      main = "Carson Darrow: Displacement vs MPG")


png("plot_weight_and_mpg.png")

plot(mtcars$wt,mtcars$mpg,
     main="Carson Darrow: Weight vs MPG",
     xlab="Weight in Thousands",
     ylab="MPG",
     las=1)



sink.reset <- function(){
  for(i in seq_len(sink.number())){
    sink(NULL)
  }
}

sink.reset















