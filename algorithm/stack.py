class stack:
    def __init__(self):
        self.items = []

    # pop
    def pop(self):
        item_length = len(self.items)
        # 스택이 비어있을 경우
        if item_length < 1:
            print("Stack is empty!")
            return False
        # else 가장 위에 있는 item을 반환하며 삭제
        result = self.items[item_length - 1]
        del self.items[item_length - 1]
        return result

    # push
    def push(self, x):
        self.items.append(x)

    # isEmpty
    def isEmpty(self):
        return not self.items

if __name__ == "__main__":
    # test
    test = stack()
    test.push(1)
    test.push(3)
    test.push(5)
    print(test.items)
    print(test.pop())
    print(test.pop())
    print(test.pop())
    print(test.isEmpty())