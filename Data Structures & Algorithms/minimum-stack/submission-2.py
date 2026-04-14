class MinStack:

    def __init__(self):
        self.values = []
        self.curr_min = float('inf')
        

    def push(self, val: int) -> None:
        self.values.append(val)
        if val < self.curr_min:
            self.curr_min = val
        

    def pop(self) -> None:
        print(f"curr stack: {self.values}")
        if self.values[-1] == self.curr_min:
            if len(self.values[:-1]) == 0:
                self.curr_min = float('inf')
            else:
                self.curr_min = min(self.values[:-1])
        self.values = self.values[:-1]

    def top(self) -> int:
        return self.values[-1]
 
        
    def getMin(self) -> int:
        return self.curr_min
        
