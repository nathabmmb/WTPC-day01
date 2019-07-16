def find_prime_factors(n):
	factors = []
	d = 2
	while  n > 1:
		while n%d  == 0:
			factors.append(d)
			n /= d
		d += 1
	return factors

print(max(find_prime_factors(600851475143)))