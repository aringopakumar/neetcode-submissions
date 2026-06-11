class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for num in nums:
            if num not in myDict:
                myDict[num] = 1
            else:
                temp = myDict[num]
                myDict[num] = temp+1
        finalReturn = []
        for i in range(k):
            maxVal = -1
            maxKey = 0
            for key, val in myDict.items():
                if val > maxVal:
                    maxVal = val
                    maxKey = key
            finalReturn.append(maxKey)
            del myDict[maxKey]
        
        return finalReturn
