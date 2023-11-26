k = "AA" 
n = "Aa"  
m = "aa"

popul = k + m + n

prob(Ax) = (k(k-1) + 2*k*m + 2*k*n + 0.75*(m-1) + 0.5*m*n + 0.5*m*n)/(popul*(popul-1))

print(prob)