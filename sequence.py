n = int(input("Enter the length of the sequence: ")) # Do not change this line

oldest_int = 0
middle_int = 0
newest_int = 1
sum_int = 0
for i in range(0, n):
	oldest_int = middle_int
	middle_int = newest_int
	newest_int = sum_int
	print(oldest_int + middle_int + newest_int)
	sum_int = oldest_int + middle_int + newest_int