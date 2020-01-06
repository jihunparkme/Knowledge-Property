def mergeSort(x):
    # 집합의 원소가 1개 남았을 경우 해당 원소 반환
    if len(x) <= 1:
        return x

    # 분할(divide), 정복(conquer) 단계
    m = len(x) // 2
    L = mergeSort(x[:m])
    R = mergeSort(x[m:])

    # 결합(combine) 단계
    result = []
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
    result += L[i:]
    result += R[j:]
    return result

if __name__ == "__main__":
    arr = [7, 9, 2, 10, 3, 8, 1, 4, 5, 6]
    rst = mergeSort(arr)
    print(rst)