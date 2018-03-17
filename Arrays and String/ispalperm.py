import sys
def isPalindromepermutation(string):
	string_Dict={}
	count_2=0
	for char in string:
		if char!=' ':
			if char not in string_Dict:
				string_Dict[char]=1
			else:
				string_Dict[char]+=1
			if string_Dict[char]==2:
				count_2+=1	
	if 2*count_2==sum(string_Dict.values())-1:
		return True
	else:
		return False
input=sys.argv[1]
print(isPalindromepermutation(input))		
'''
Analysis:
Time Complexity O(n)
Space Complexity O(n)
'''