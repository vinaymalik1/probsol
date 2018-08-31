'''
Write a program that prints the numbers from 1 to 100. If a number is
divisible by 3, print Fizz instead of the number, if a number is divisible by
5, print Buzz instead of the number, and if a number is divisible by both 3
and 5, print FizzBuzz instead of the number.
'''

#First Type
for x in range(1,101):
	if x%15==0:
		print "FizzBuzz"
	elif x%3==0:
		print "Fizz"
	elif x%5==0:
		print "Buzz"
	else:
		print x


#Second Type
def replacement(x):
	replaced=''
	if x%3==0:
		replaced += 'Fizz'
	if x%5==0:
		replaced += 'Buzz'

	if not replaced:
		replaced=x
	return replaced

for x in range(1,101):
	print replacement(x)