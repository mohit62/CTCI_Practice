import sys
def compr(inp):
	count=0
	compress=[]
	for index in range(len(inp)):
		count+=1
		if index+1>=len(inp) or inp[index]!=inp[index+1]:
			compress.append(inp[index]+str(count))
			count=0
	return ''.join(compress)
inp=sys.argv[1]
print("Compressed string is: "+compr(inp))
'''
Analysis:
Time Complexity O(n)
Space Complexity O(n)
'''		