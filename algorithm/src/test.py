from itertools import permutations

def solution(baseball):
    lst = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    for i in baseball:
        for item in lst[:]:
            if not check_score([int(i) for i in list(str(i[0]))], item, i[1], i[2]):
                lst.remove(item)
    return len(lst)

def check_score(question, candidate, s, b):
    strike = 0
    for i in range(len(question)):
        if question[i] == candidate[i]:
            strike += 1
    if s != strike:
        return False
    ball = len(set(question) & set(candidate))-strike
    if b != ball:
        return False
    return True

if __name__=='__main__':
    baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
    print(solution(baseball))