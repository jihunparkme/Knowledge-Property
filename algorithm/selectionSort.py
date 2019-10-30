def selectionSort(x):
	length = len(x)
	for i in range(length-1):
		for j in range(i+1, length):
			if x[i] > x[j]:
				x[i], x[j] = x[j], x[i]
	return x

if __name__ == "__main__":
	arr = [7, 9, 2, 10, 3, 8, 1, 4, 5, 6]
	rst = selectionSort(arr)
	print(rst)