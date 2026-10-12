class MinStack:
    def __init__(self):
        self.stack = []
        self.stack1 = []
        self.minNum = float('inf')
    def push(self, val: int) -> None:
        self.minNum = min(self.minNum,val)
        (self.stack).append(val)
        if(len(self.stack1) == 0 or val <= self.stack1[len(self.stack1)-1]):
            (self.stack1).append(val)
    def pop(self) -> None:
        if(self.stack[len(self.stack)-1] == self.minNum):
            if(len(self.stack1) > 1):            
                (self.stack1).pop()
                self.minNum = (self.stack1)[len(self.stack1)-1]
            else:
                (self.stack1).pop()
                self.minNum = float("inf")
        (self.stack).pop()
    def top(self) -> int:
        return (self.stack)[len(self.stack) - 1]
    def getMin(self) -> int:
        return self.minNum

