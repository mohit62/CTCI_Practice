def setzeroes(matrix):
	colHaszero=False
	rowHaszero=False
	#check if any elemnt in first col is zero
	for row in range(len(matrix)):
		if(matrix[row][0]==0):
			colHaszero=True
			break
	#check if any elemnt in first row is zero		
	for col in range(len(matrix[0])):
		if(matrix[0][col]==0):
			rowHasZero=True
			break
	#check and set other elements to zero		
	for row in range(1,len(matrix)):
		for col in range(1,len(matrix[0])):
			if(matrix[row][col]==0):
				matrix[row][0]=0
				matrix[0][col]=0
	for row in range(1,len(matrix)):
		if(matrix[row][0]==0):
			for col in range(len(matrix[0])):
				matrix[row][col]=0
	for col in range(1,len(matrix[0])):
		if(matrix[0][col]==0):
			for row in range(len(matrix)):
				matrix[row][col]=0			
	if colHaszero:
		for row in range(len(matrix)):
				matrix[row][0]=0
	if rowHaszero:
		for col in range(len(matrix[0])):
				matrix[0][col]=0			
	print matrix
mat=[[2,3,0],[4,3,1],[0,4,5]]	
print mat
setzeroes(mat)				
