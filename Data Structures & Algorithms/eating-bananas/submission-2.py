class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Two pointers where l being the number of bananas/hr
        l = 1
        r = max(piles)

        while l < r:
            m = l + ((r - l) // 2)
            total_hours = 0 #its the time taken when u eat at m bananas/hr
            for pile in piles:
                total_hours = total_hours + ((pile + m - 1) // m)
            
            if total_hours > h:
                l = m + 1
            else:
                r = m
        return l