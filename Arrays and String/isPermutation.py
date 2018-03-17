import sys
#Naive soln
def sorted(str):
	sortedstring=[];
	for char in str:
		sortedstring.append(char)
	sortedstring.sort()	
	return sortedstring
def isPermutation(string1,string2):
	if sorted(string1) == sorted(string2):
		return True
	else:
		return False
'''
Analysis:
Time Complexity O(nlogn)
Space Complexity O(n)
'''
def isPermutation2(string1,string2):
	string1dict={}
	for char1 in string1:
		if char1 in string1dict:
			string1dict[char1]+=1
		else:
			string1dict[char1]=1
	for char2 in string2:
		if char2 in string1dict:
			string1dict[char2]-=1
		if(string1dict[char2]<0):
			return False
	return True	
'''
Analysis:
Time Complexity O(n)
Space Complexity O(n)
'''			
(string1,string2)=sys.argv[1:3]		
print(isPermutation(string1,string2))
print(isPermutation2(string1,string2))		