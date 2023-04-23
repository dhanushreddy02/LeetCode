def calculatedigitsOfone(A):
	n, factors, count, remainder = A, 1, 0, 0
	while n > 0:
		temp = factors
		# check for remainders three cases mentioned in
		# the approach
		if n % 10 == 0:
			remainder = 0
		elif n % 10 > 1:
			remainder = temp
		elif n % 10 == 1:
			remainder = (A % temp) + 1
		factors *= 10 # incrementing factors for checking
					# different locations such as ones,
					# tens, hundreds places ones
		count += (A // factors) * temp + remainder
		n //= 10
	return count

# Example usage
n = 100
print(calculatedigitsOfone(n))
n = 113
print(calculatedigitsOfone(n))
n = 235
print(calculatedigitsOfone(n))


# This code is contributed by shiv1o43g
