import sys
def isreplace(string1,string2):
	differ=0
	for char1,char2 in zip(string1,string2):
		if char1!=char2:
		    differ+=1
		else:
			continue
	if 	differ==1:	
		return True
	else:
		return False				
def isinsert_delete(s1,s2):
	index1=0
	index2=0
	while(index1<len(s1) and index2<len(s2)):
		if (s1[index1]!=s2[index2]):
			if index1!=index2:
				return False
			index2+=1
		else:
			index1+=1
			index2+=1	
	return True		
def oneAway(string1,string2):
	if len(string1)==len(string2):
		return isreplace(string1,string2)
	elif len(string1)-1==len(string2):
		return isinsert_delete(string2,string1)
	elif len(string1)+1==len(string2):
		return isinsert_delete(string1,string2)
	else:
		return False	
inp1=sys.argv[1]
inp2=sys.argv[2]
print(oneAway(inp1,inp2))
'''
Analysis:
Time Complexity O(n)
Space Complexity O(1)
'''		