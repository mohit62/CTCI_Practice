import sys
#Solution using additional data structure
def isUnique1(string):
	unique={};
	for char in string:
		if char in unique.keys():
			return False
		else:
			unique[char]=1;	
	return True
'''Analysis:
Time Complexity O(n)
Space Complexity O(n)
'''
#Solution without additional data structure
def isUnique2(string):
	for char1 in range(len(string)):
		for char2 in range(char1+1,len(string)):
			if string[char1] == string[char2]:
				return False
			else:
				continue	
	return True	
'''Analysis:
Time Complexity O(n^2)
Space Complexity O(1)
'''	
input=sys.argv[1]
print(isUnique1(input));
print(isUnique2(input));



			
