import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''the formula is ceil(pile/hour) to calculate how many hrs are required'''

        def k_check(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                return True
            else:
                return False
        
        l = 1
        r = max(piles) #4 in the example
        while l < r:
            m = l + ((r - l) // 2)
            if k_check(m):
                r = m
            else:
                l = m + 1
        return l
