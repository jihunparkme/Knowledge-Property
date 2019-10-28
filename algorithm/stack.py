class stack:
    def __init__(self):
        self.stack_items = []

    # pop
    def pop(self):
        item_length = len(self.stack_items)
        # 스택이 비어있을 경우
        if item_length < 1:
            print("Stack is empty!")
            return False
        # else 가장 위에 있는 item을 반환하며 삭제
        result = self.stack_items[item_length - 1]
        del self.stack_items[item_length - 1]
        return result

    # push
    def push(self, x):
        self.stack_items.append(x)

    # isEmpty
    def isEmpty(self):
        return not self.stack_items

# test
test = stack()
test.push(1)
test.push(3)
test.push(5)
print(test.stack_items)
print(test.pop())
print(test.pop())
print(test.pop())
print(test.isEmpty())