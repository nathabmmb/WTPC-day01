def fibbolist(top):
	seq = [0, 1]
	while True:
		x = seq[-1] + seq[-2]
		if x < top:
			seq.append(x)
		else: break
	return seq

# print(len(fibbolist(1e6)))
sum = 0
for i in fibbolist(1e6):
	if i%2 != 0 :
		sum += i
print(sum)