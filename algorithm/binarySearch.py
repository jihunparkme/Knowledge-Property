import math

def binarySearch(arr, n):
    start = 0
    end = len(arr)-1
    while end-start >= 0:
        mid = math.ceil((start+end)/2)
        # 어떤 방향의 중간값으로 탐색할지 결정
        if arr[mid]==n:
            return mid+1
        if arr[mid]<n:
            start = mid+1
        else:
            end = mid-1
    return -1;

if __name__ == "__main__":
    arr = [1,3,4,6,7,9,13,15]
    num = 3
    print(binarySearch(arr, num))