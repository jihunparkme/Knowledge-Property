from itertools import permutations
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    all_num = []
    for i in range(len(numbers)):
        for j in permutations(numbers,i+1):
            all_num.append(int(''.join(j)))

    for num in set(all_num):
        flag = True
        if num != 1 and num != 0:
            for di in range(2, num) :
                if num % di == 0 :
                    flag = False
                    break
            if flag == True: answer += 1
    return answer

if __name__=='__main__':
    numbers = "17"
    print(solution(numbers))