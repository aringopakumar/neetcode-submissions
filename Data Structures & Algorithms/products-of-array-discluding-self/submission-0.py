class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        target = 0
        while len(final) != len(nums):
            result = 1
            for i in range(len(nums)):
                if target != i:
                    result = result*nums[i]
            final.append(result)
            target += 1
        return final