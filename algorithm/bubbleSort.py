def bubbleSort(x):
	length = len(x)-1
	for i in range(length):
		for j in range(length-i):
			if x[j] > x[j+1]:
				x[j], x[j+1] = x[j+1], x[j]
	return x

if __name__ == "__main__":
	arr = [7, 9, 2, 10, 3, 8, 1, 4, 5, 6]
	rst = bubbleSort(arr)
	print(rst)