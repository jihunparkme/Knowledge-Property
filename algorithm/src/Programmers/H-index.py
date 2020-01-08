def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

if __name__ == '__main__':
    citations = [6, 5, 3, 1, 0]
    print(solution(citations))
