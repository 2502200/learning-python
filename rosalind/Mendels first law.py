k = 2
m = 2  
n = 2
#k is homozygous dominant (AA), m is heterozygous (Aa), n is homozygous recessive (aa)

popul = k + m + n
#the offspring can either be homozygous dominant or heterozygous (Ax)
prob = (k*(k-1) + 2*k*m + 2*k*n + 0.75*(m-1) + 0.5*m*n + 0.5*m*n)/(popul*(popul-1))

print(prob)
