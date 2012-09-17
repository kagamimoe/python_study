n = int(raw_input('Please enter the number: '))
len = len(str(n))
#print n

def addx(n):
	temp = 0
	while n > 0:
		temp = temp + 9*(10**(n-2))*(n-1)
		n = n - 1
	#print n
	return temp 

#print int(addx(3))

x = ((n - (10**(len-1)-1))*len) + int(addx(len))
print x

