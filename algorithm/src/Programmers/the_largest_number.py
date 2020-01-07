def solution(numbers):
    num = list(map(lambda x:str(x)*3, numbers))
    num.sort(reverse=True)
    res = list(map(lambda x:x[:(len(x)//3)], num))
    return str(int((''.join(res))))

if __name__ == '__main__':
    # numbers = [3, 30, 34, 5, 9]
    numbers = [0,0,0]
    print(solution(numbers))