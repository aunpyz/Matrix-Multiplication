m1 = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
m2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def printMatrix(m):
	print('size:',len(m),'*',len(m))
	for i in m:
		print(i)
		
def addMatrix(m1,m2):
	c=list()
	for i,j in zip(m1,m2):
		c.append([a+b for a,b in zip(i,j)])
	return c
	
def makeSubMatrix(m, pos):
	c=list()
	pos=str(pos)
	x=int(len(m)/2)
	if(pos[0]=='1'):
		for i in m[:x]:
			y=int(len(i)/2)
			if(pos[1]=='1'):
				c.append(i[:y])
			elif(pos[1]=='2'):
				c.append(i[y:])
	elif(pos[0]=='2'):
		for i in m[x:]:
			y=int(len(i)/2)
			if(pos[1]=='1'):
				c.append(i[:y])
			elif(pos[1]=='2'):
				c.append(i[y:])
	return c
	
def mergeMatrix(m11,m12,m21,m22):
	c=list()
	m1=zip(m11,m12)
	m2=zip(m21,m22)
	for i,j in m1:
		c.append(i+j)
	for i,j in m2:
		c.append(i+j)
		
	return c
	
def multiplyMatrix(m1,m2):
	#m1 and m2 is same in size
	l = len(m1)
	if(l==1):
		return [[m1[0][0]*m2[0][0]]]
	a11=makeSubMatrix(m1,11)
	a12=makeSubMatrix(m1,12)
	a21=makeSubMatrix(m1,21)
	a22=makeSubMatrix(m1,22)
	b11=makeSubMatrix(m2,11)
	b12=makeSubMatrix(m2,12)
	b21=makeSubMatrix(m2,21)
	b22=makeSubMatrix(m2,22)
	
	c11=addMatrix(multiplyMatrix(a11,b11),multiplyMatrix(a12,b21))
	c12=addMatrix(multiplyMatrix(a11,b12),multiplyMatrix(a12,b22))
	c21=addMatrix(multiplyMatrix(a21,b11),multiplyMatrix(a22,b21))
	c22=addMatrix(multiplyMatrix(a21,b12),multiplyMatrix(a22,b22))
	return mergeMatrix(c11,c12,c21,c22)
		
print('Multiply')
m=multiplyMatrix(m1,m2)
printMatrix(m)