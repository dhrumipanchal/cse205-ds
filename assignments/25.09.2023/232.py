class MyQueue:

    def __init__(self):
        self.in_st1=[]
        self.out_st2=[]

    def push(self, x: int) -> None:
        self.in_st1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_st2.pop()

    def peek(self) -> int:
        if not self.out_st2:
            while self.in_st1:
                self.out_st2.append(self.in_st1.pop())
        return self.out_st2[-1]
                

    def empty(self) -> bool:
        return not self.in_st1 and not self.out_st2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()