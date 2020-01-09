from itertools import permutations
def solution(baseball):
    # Preparation of the number of cases
    num_list = list(permutations(range(1,10), 3))
    # num_list = []
    # for i in permutations(range(1,10), 3):
    #     num_list.append(int(''.join(map(str,i))))

    while baseball:
        game, s, b = baseball.pop()
        game = list(map(int, list(str(game))))
        for n in num_list[:]:
            strike = 0
            # Comparison of strikes
            for i in range(len(game)):
                if game[i] == n[i]:
                    strike += 1
            if strike != s:
                num_list.remove(n)
            else: # Comparison of ball
                ball = len(set(game) & set(n)) - strike
                if ball != b:
                    num_list.remove(n)
    return len(num_list)

if __name__=='__main__':
    baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
    print(solution(baseball))


test = [1,2,3]
test[:]
test.remove(3)