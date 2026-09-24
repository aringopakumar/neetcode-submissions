class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val not in ["+", "-", "*", "/"]:
                stack.append(int(val))
            else:
                recent = stack.pop()
                old = stack.pop()

                if val == "+":
                    temp = old + recent
                elif val == "-":
                    temp = old - recent
                elif val == "*":
                    temp = old * recent
                else:
                    temp = int(old / recent)

                stack.append(temp)

        return stack[0]
                
