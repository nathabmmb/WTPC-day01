sum = 0 #define la variable sum
for i in range(1000):
	if (i%3 == 0 or i%5 == 0): #check si es multiplo de 3 ó 5 y suma a "sum"
		sum += i 
print(sum)