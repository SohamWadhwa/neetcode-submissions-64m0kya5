class MinStack:

    def __init__(self):
        self.st =[]

    def push(self, val: int) -> None:
        minVal = self.getMin()
        if minVal == None or minVal > val:
            minVal = val
        
        self.st.append([val, minVal])

    def pop(self) -> None:
        if self.st:
            self.st.pop()

    def top(self) -> int:
        return self.st[-1][0] if self.st else None

    def getMin(self) -> int:
        return self.st[-1][1] if self.st else None
