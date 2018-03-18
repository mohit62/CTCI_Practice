import sys
def URLify(string):
	URL=[]
	for char in range(len(string)-1):
		if string[char]==' ' and string[char+1]!=' ':
			URL.append("%20")
		else:
			URL.append(string[char])
	URL.append(string[-1])
	return ''.join(URL)

sent=sys.argv[1]
print(URLify(sent))				
'''Analysis:
Time Complexity O(n)
Space Complexity O(n)
'''
