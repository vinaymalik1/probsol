'''Write a function that reverses a string without using any library functions.'''

string=raw_input('Input string')
new_str=''
for x in range(len(string)):
	new_str += string[-(x+1)]
print new_str