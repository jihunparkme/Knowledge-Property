def quicksort(x):
    if len(x) <= 1:
        return x

    # 분할(divide)
    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []

    # 정복(conquer)
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quicksort(less) + equal + quicksort(more)

if __name__ == "__main__":
    arr = [7, 9, 2, 10, 3, 8, 1, 4, 5, 6]
    rst = quicksort(arr)
    print(rst)