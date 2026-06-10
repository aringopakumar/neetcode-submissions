class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sNums = set(nums)
        if len(sNums) == len(nums):
            return False
        return True 
                



