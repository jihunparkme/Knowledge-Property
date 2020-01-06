def solution(heights):
    answer = []
    for n in range(len(heights)-1, 0, -1):
        for comp in range(n-1, -1, -1):
            if heights[n] < heights[comp]:
                answer.append(comp+1)
                break
            if comp == 0: answer.append(0)
    answer.append(0)
    return list(reversed(answer))

if __name__ == "__main__":
    heights = [3,9,9,3,5,7,2]
    print(solution(heights))