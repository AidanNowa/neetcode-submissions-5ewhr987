class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ints = []
        for token in tokens:
            
            if token in ['+', '-', '*', '/'] and len(ints) >= 2:
                second = ints.pop()
                first = ints.pop()
                if token == '+':
                    ints.append(first + second)
                elif token == '-':
                    ints.append(first - second)
                elif token == '*':
                    ints.append(first * second)
                elif token == '/':
                    ints.append(int(first / second))
            else:
                ints.append(int(token))

        return ints[0]
        