class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ""
        for char in s:
            if char.isalnum():
                cleaned_str += ''.join(char.lower())
        left_point = 0
        right_point = len(cleaned_str)

        while left_point < right_point:
            if cleaned_str[left_point] == cleaned_str[right_point-1]:
                left_point += 1
                right_point -= 1
            else:
                return False
        return True
        

            