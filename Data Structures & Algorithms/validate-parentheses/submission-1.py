class Solution:
    def isValid(self, s: str) -> bool:
        open_chars = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                open_chars.append(char)
            elif len(open_chars) > 0:
                if char == ')':
                    if open_chars[-1] == '(':
                        open_chars.pop()
                    else:
                        return False
                elif char == ']':
                    if open_chars[-1] == '[':
                        open_chars.pop()
                    else:
                        return False
                elif char == '}':
                    if open_chars[-1] == '{':
                        open_chars.pop()
                    else:
                        return False
            else:
                #unknown char or unmatched close
                return False
            
        if len(open_chars) == 0:
            return True
        return False
        