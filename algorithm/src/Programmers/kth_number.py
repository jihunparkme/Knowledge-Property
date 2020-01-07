def solution(array, commands):
    answer = []
    for com in commands:
        ar = array[com[0]-1:com[1]]
        ar.sort()
        answer.append(ar[com[2]-1])
    return answer

if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array, commands))