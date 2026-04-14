class MinStack:

    def __init__(self):
        self.values = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.values.append(val)
        if self.mins:
            curr_min = self.getMin()
            if val <= curr_min:
                self.mins.append(val)
        else:
            #empty mins list
            self.mins.append(val)
        

    def pop(self) -> None:
        curr_min = self.getMin()
        val = self.values[-1]
        if val == curr_min:
            self.mins = self.mins[:-1]
        self.values = self.values[:-1]

    def top(self) -> int:
        return self.values[-1]
 
        
    def getMin(self) -> int:
        return self.mins[-1]
        
