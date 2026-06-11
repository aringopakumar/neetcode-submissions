class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        myList = [[] for i in range(len(nums)+1)]

        for num in nums:
            myDict[num] = 1 + myDict.get(num, 0)
        for key, val in myDict.items():
            myList[val].append(key)
        
        result = []
        for i in range(len(myList)-1, 0, -1):
            for x in myList[i]:
                result.append(x)
                if len(result) == k:
                    return result