import sys
def URLify(string):
	URL=""
	for char in range(len(string)-1):
		if string[char]==' ' and string[char+1]!=' ':
			URL+="%20"
		else:
			URL+=string[char]
	URL+=string[-1]		
	return URL

sent=sys.argv[1]
print(URLify(sent))				
'''Analysis:
Time Complexity O(n)
Space Complexity O(1)
'''