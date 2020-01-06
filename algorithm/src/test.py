import collections

def solution(p, l):
    ans = 0
    m = max(p)
    # p = collections.deque(p)

    while True:
        # v = p.popleft()
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans

if __name__ == '__main__':
    priorities = [1,2,3,9,9,9]
    location = 1
    print(solution(priorities, location))