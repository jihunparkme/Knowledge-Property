def solution(arrangement):
    answer = 0
    stack = []
    for a in list(arrangement):
        if a == '(':
            stack.append(a)
            last = a
        else:
            stack.pop()
            if last == '(':
                answer += len(stack)
                last = a
            else:
                answer += 1
    return answer

if __name__ == "__main__":
    arrangement = "()(((()())(())()))(())"
    print(solution(arrangement))