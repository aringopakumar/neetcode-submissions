class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pt1 = 0
        pt2 = len(numbers)-1
        finalArray = []

        while pt1 < pt2:
            if numbers[pt1] + numbers[pt2] == target:
                finalArray.append(pt1+1)
                finalArray.append(pt2+1)
                return finalArray
            elif numbers[pt1] + numbers[pt2] > target:
                pt2 -= 1
            else:
                pt1 += 1

        pt1 = pt1 + 1


        #returning 1-indexed version


        
        