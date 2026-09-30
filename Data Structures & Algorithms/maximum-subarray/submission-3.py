class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            current = max(num, current + num)
            best = max(best, current)
        
        return best



        
        