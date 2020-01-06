import collections
def solution(clothes):
    clothes_dic = dict(clothes)
    type = collections.Counter(list(clothes_dic.values()))
    answer = 1
    for coun in list(type.values()) :
        answer = answer * (coun+1)

    return answer - 1

if __name__ == '__main__' :
    clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
    # clothes = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]
    print(solution(clothes))

sorted(clothes)
dict(zip(['c','d','d','e'], [1,3,2,3]))