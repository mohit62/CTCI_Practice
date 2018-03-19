import sys
def isRotation(s1,s2):
	s1+=s1
	if s2 in s1:
		return True
	else:
		return False	
str1=sys.argv[1]
str2=sys.argv[2]
print "is string 2 rotation of string 1",isRotation(str1,str2)
'''
Analysis:
Time Complexity O(n)
Space Complexity O(n)
'''		