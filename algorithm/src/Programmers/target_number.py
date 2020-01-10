def calculate(numbers, target, i):
    if i == len(numbers):
        if sum(numbers) == target:
            global cnt
            cnt += 1
    else:
        numbers[i] *= 1
        calculate(numbers, target, i + 1)

        numbers[i] *= -1
        calculate(numbers, target, i+1)

def solution(numbers, target):
    global cnt
    cnt = 0

    calculate(numbers, target, 0)
    return cnt

if __name__=='__main__':
    numbers = [1, 1, 1]
    target = 3
    print(solution(numbers, target))