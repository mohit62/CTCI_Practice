matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for layerno in range(len(matrix)/2):
	first=layerno
	last=len(matrix)-layerno-1
	for index in range(first,last):
		top=matrix[first][index]
		#left to top
		matrix[first][index]=matrix[last+first-index][first]
		#bottom to left
		matrix[last+first-index][first]=matrix[last][last+first-index]
		#right to bottom
		matrix[last][last+first-index]=matrix[index][last]
		#top to right
		matrix[index][last]=top
print matrix		
'''
    Analysis:
    Time Complexity O(n^2)
    Space Complexity O(1)
    '''

