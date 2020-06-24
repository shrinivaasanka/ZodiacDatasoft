cagraphprojections <- function(coeffglm,infected,recovered,deaths,recoverytime)
{
  print("1:")
  print(coeffglm[1])
  print("2:")
  print(coeffglm[2])
  print("3:")
  print(coeffglm[3])
  print("4")
  print(coeffglm[4])
  print("5")
  print(coeffglm[5])
  perdiem <- 400*as.numeric(8*abs(coeffglm[2])*infected - abs(coeffglm[4])*recovered - abs(coeffglm[3])*deaths + abs(coeffglm[5])*recoverytime + coeffglm[1])
  print("Per day spread(abs):")
  print(abs(perdiem))
  perdiem <- 400*as.numeric(8*(coeffglm[2])*infected - (coeffglm[4])*recovered - (coeffglm[3])*deaths + (coeffglm[5])*recoverytime + coeffglm[1])
  print("Per day spread:")
  print(perdiem)
}

cagraphlogit <- function(filename,weights=c())
{
  print(filename)
  layout(matrix(1:3,3,1))
  coronavirus2019dataset <- read.table(filename, header=TRUE)
  print(coronavirus2019dataset)
  Infected <- coronavirus2019dataset$Infected
  Deaths <- coronavirus2019dataset$Deaths
  Recovered <- coronavirus2019dataset$Recovered
  Perdiem <- coronavirus2019dataset$Perdiem
  RecoveryTime <- coronavirus2019dataset$RecoveryTime
  print("CAGraph Logit:")
  print("==================")
  print("GLM:")
  if(length(weights) > 0)
  {
  	coronavirus2019logit1 <- glm(Perdiem ~ Infected + Deaths + Recovered + RecoveryTime, family = poisson(), weights=weights)
  }
  else
  {
  	coronavirus2019logit1 <- glm(Perdiem ~ Infected + Deaths + Recovered + RecoveryTime, family = poisson())
  }
  print(summary(coronavirus2019logit1))
  print("=================================")
  print("LM:")
  if(length(weights) > 0)
  {
  	coronavirus2019logit2 <- lm(Perdiem ~ Infected + Deaths + Recovered + RecoveryTime, weights=weights)
  }
  else
  {
  	coronavirus2019logit2 <- lm(Perdiem ~ Infected + Deaths + Recovered + RecoveryTime)
  }
  print(summary(coronavirus2019logit2))
  print("=================================")
  c(coronavirus2019logit1,coronavirus2019logit2)
}
#print("===================================")
#print("CAGraph Logit - Predefined weights:")
#print("===================================")
#covid19logit <- cagraphlogit("./CAGraphLogit.dat",c(1,1,8,1,1,0.1))
print("===================================")
print("CAGraph Logit - R learnt weights - Iterative Weighted Least Squares (IWLS):")
print("===================================")
covid19logit <- cagraphlogit("./CAGraphLogit.dat")
print("===================================")
print("Summary:")
print("===================================")
print(covid19logit)
print("===================================")
print("Global - Per day Projections from learnt model:")
print("===================================")
coeffglm <- coef(covid19logit[1])
cagraphprojections(coeffglm,9100000,4900000,474000,15)
