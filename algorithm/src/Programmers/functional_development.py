import operator

def solution(progresses, speeds):
    answer = []
    while progresses:
        progresses = list(map(operator.add, progresses, speeds))

        distribution = 0
        for w in [0] * len(progresses):
            if progresses[w] < 100:
                break
            else:
                distribution += 1
                del progresses[w]
                del speeds[w]

        if distribution != 0:
            answer.append(distribution)

    return answer

if __name__ == '__main__':
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))