
#ricker <- function(r,K=1,serieslen=100)
#{
  K <- 0.6
  r <- 4.9
  serieslen <- 100
  print(K)
  print(serieslen)
  N <- 1:serieslen
  for(i in 1:serieslen) {
	  N[i+1] <- N[i] * exp(r*(1 - N[i]/K))
  }
  tsN <- ts(N)
  xaxis <- 0:serieslen
  yaxis <- N
  plot(xaxis,yaxis)
  plot.ts(yaxis)
  print(yaxis)
#}

#x11()
#layout(matrix(1:3,3,1))
#ricker(4.9,0.6,100)
