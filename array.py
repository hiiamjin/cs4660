import random

a = []
b = [1,2,3,4]

for x in range(len(b)):
	a.append([random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)])
	
print(a)
print(a[0])