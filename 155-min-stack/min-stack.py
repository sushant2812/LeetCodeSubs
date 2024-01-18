class MinStack:

    def __init__(self):
        self.Min_Stack=[]
        self.Stack=[]

    def push(self, val: int) -> None:
        self.Stack.append(val)
        if self.Min_Stack==[]:
            self.Min_Stack.append(val)
        elif(val<self.Min_Stack[-1]):
            self.Min_Stack.append(val)
        else:
            self.Min_Stack.append(self.Min_Stack[-1])

    def pop(self) -> None:
        self.Stack.pop()
        self.Min_Stack.pop()

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return self.Min_Stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()