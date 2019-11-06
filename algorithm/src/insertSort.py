def insertSort(x):
	for i in range(1, len(x)):
		j = i - 1
		key = x[i]
		while x[j] > key and j >= 0:
			x[j+1]  = x[j]
			j = j - 1
		x[j+1] = key
	return x

if __name__ == "__main__":
	arr = [7, 9, 2, 10, 3, 8, 1, 4, 5, 6]
	rst = insertSort(arr)
	print(rst)