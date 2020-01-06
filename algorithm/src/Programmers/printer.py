def solution(priorities, location):
    print = []
    works = [(i, pri) for i, pri in enumerate(priorities)]
    while works:
        w = works.pop(0)
        m = max(priorities)
        del priorities[0]
        if w[1] < m:
            works.append(w)
            priorities.append(w[1])
        else:
            print.append(w)

    for i, a in enumerate(print):
        if a[0] == location:
            answer = i
    return answer+1

if __name__ == '__main__':
    priorities = [1,2,3,9,9,9]
    location = 1
    print(solution(priorities, location))