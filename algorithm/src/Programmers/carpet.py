def solution(brown, red):
    answer = []
    area = brown + red
    for height in range(3, area):
        for width in range(height, brown):
            if width * height == area:
                if (width*2) + (height-2)*2 == brown:
                    answer.append([width, height])
                    break
    return answer[0]

if __name__=='__main__':
    brown = 24
    red = 24
    print(solution(brown, red))