from codes.python.modules import ListNode


class LinkedListStack:
    """implement stack with linked list"""

    def __init__(self):
        """constructor"""
        self._peek: ListNode | None = None
        self._size: int = 0

    def size(self) -> int:
        """get the size of the stack"""
        return self._size

    def is_empty(self) -> bool:
        return not self._peek

    def push(self, val: int):
        """push an element into the stack"""
        node = ListNode(val)
        node.next = self._peek
        self._peek = node
        self._size += 1

    def pop(self) -> int:
        """pop and element out of the stack"""
        num = self.peek()
        self._peek = self._peek.next
        self._size -= 1
        return num

    def peek(self) -> int:
        """ge the top element of the stack"""
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._peek.val

    def to_list(self) -> list[int]:
        """convert the stack to a list for printing"""
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr


"""Drive Code"""
if __name__ == "__main__":
    # 初始化栈
    stack = LinkedListStack()

    # 元素入栈
    stack.push(1)
    stack.push(3)
    stack.push(2)
    stack.push(5)
    stack.push(4)
    print("栈 stack =", stack.to_list())

    # 访问栈顶元素
    peek: int = stack.peek()
    print("栈顶元素 peek =", peek)

    # 元素出栈
    pop: int = stack.pop()
    print("出栈元素 pop =", pop)
    print("出栈后 stack =", stack.to_list())

    # 获取栈的长度
    size: int = stack.size()
    print("栈的长度 size =", size)

    # 判断是否为空
    is_empty: bool = stack.is_empty()
    print("栈是否为空 =", is_empty)
