class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max = maxSize
        self.size = 0


    def push(self, x: int) -> None:
        if self.size==self.max:
            return
        self.stack.append(x)
        self.size+=1

    def pop(self) -> int:
        if self.stack==[]:
            return -1
        self.size-=1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        if self.size<k:
            for i in range(self.size):
                self.stack[i]+=val
        else:
            for i in range(k):
                self.stack[i]+=val
        return


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)