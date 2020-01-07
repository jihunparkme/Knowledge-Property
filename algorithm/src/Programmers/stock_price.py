def solution(prices):
    answer = []
    for prc in range(0, len(prices)):
        sec = 0
        for prc2 in range(prc+1, len(prices)):
            sec += 1
            if prices[prc] > prices[prc2]:
               break
        answer.append(sec)
    return answer

if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))