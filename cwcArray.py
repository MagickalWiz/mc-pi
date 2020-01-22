from array import *

m = [[1,1,1,1],
     [1,0,0,1],
     [1,0,0,1],
     [1,1,1,1]]

print(m)

for h in range (0,4):
	for k in range (0,4):
		print(m[h][k],end="")
	print()
