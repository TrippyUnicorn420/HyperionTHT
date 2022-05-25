def verify(isbn):
	sum = 0
	if len(isbn) == 10:
		for i in range(9, -1, -1):
			if isbn[10 - (i + 1)] != 'X':
				sum += int(int(isbn[10 - (i + 1)]) * (i + 1))
			else:
				sum += 10
		print("ISBN-13: 978" + isbn[0:8] + str((int(isbn[9]) + 1)))
		if sum % 11 == 0:
			print("Valid")
			return
	if len(isbn) == 13:
		for i in range(0, 13):
			multiplicator = 1;
			if (i + 1) % 2 == 0:
				multiplicator = 3
			else:
				multiplicator = 1
			if isbn[i] != 'X':
				sum += int(int(isbn[i]) * multiplicator)
			else:
				sum += 10
		if sum % 10 == 0:
			print("Valid")
			return
	print("Invalid")
	return
			
if __name__ == "__main__":
	verify(input("Type in an ISBN: "))
