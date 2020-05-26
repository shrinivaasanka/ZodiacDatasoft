
fileiovect <- function(filename,test=1)
{
  print(filename)
  layout(matrix(1:3,3,1))
  coronavirus2019dataset <- read.table(filename, header=TRUE)
  print(coronavirus2019dataset[[2]])
  covid2019df <- data.frame(as.numeric(coronavirus2019dataset[[2]]))
  covid2019ts <- ts(coronavirus2019dataset[[2]])
  ts.plot(covid2019ts)
  attach(covid2019df)
  print("Mean-Median-Quantile:")
  print(summary(covid2019df))
  covid2019fact <- as.factor(coronavirus2019dataset[[2]])
  covid2019num <- as.numeric(coronavirus2019dataset[[2]])
  covid2019len <- length(coronavirus2019dataset[[2]])
  print(covid2019num)
  print("Histogram:")
  hist(covid2019num)
  print("Rug:")
  rug(covid2019num)
  print("Stem:")
  stem(covid2019num)
  print("Density:")
  lines(density(covid2019num))
  print("ECDF:")
  plot(ecdf(covid2019num))
  if (test == 1)
  {
    print("Kolmogorov-Smirnov Bell curve test:")
    print(ks.test(covid2019num,"pnorm"))
  }
  if (test == 2)
  {
    print("Shapiro Bell curve test:")
    print(shapiro.test(covid2019num))
  }
  if (test == 3)
  {
    print("Two sample test:")
    print(t.test(covid2019num[1:covid2019len/2],covid2019num[covid2019len/2:covid2019len]))
  }
  print("---------------------------------------------")
}
fileiovect("./FileIOVectStats.dat",1)
fileiovect("./FileIOVectStats.dat",2)
fileiovect("./FileIOVectStats.dat",3)
