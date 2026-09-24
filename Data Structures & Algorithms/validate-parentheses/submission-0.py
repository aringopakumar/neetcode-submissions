class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openClose = {'(' : ')', '{' : '}', '[' : ']'}

        for char in s:
            if char in openClose:
                stack.append(char)
            else:
                if not stack:
                    return False #empty stack
            
                last = stack[-1]
                if openClose[last] != char:
                    return False
                
                stack.pop()
        
        return len(stack) == 0
            




        


        