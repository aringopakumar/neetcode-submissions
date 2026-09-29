class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        incr = 0 
        
        while incr < len(prices):
            i = len(prices)-1
            while incr < i:
                val = prices[i] - prices[incr]
                if val > maxProf:
                    maxProf = val
                i -= 1
            incr += 1
        return maxProf

            