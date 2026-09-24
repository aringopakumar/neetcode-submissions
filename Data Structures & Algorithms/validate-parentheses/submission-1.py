class Solution:
    def isValid(self, s: str) -> bool:
        matching = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in matching:  # Closing bracket
                if not stack or stack.pop() != matching[char]:
                    return False
            else:                 # Opening bracket
                stack.append(char)

        return not stack