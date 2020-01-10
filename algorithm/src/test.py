from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

if __name__=='__main__':
    numbers = [1, 1, 1]
    target = 3
    print(solution(numbers, target))

    list(map(sum, product(*l)))
list(product(*l))
list(product(l, repeat=5))