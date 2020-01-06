def solution(phone_book):

    for ph in phone_book:
        temp = list(map(lambda i:i[:len(ph)], phone_book))
        count = temp.count(ph)
        if count >= 2:
            return False

    return True

if __name__ == "__main__":
    phone_book = ['119', '97674223', '119422342']
    print(solution(phone_book))

