class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxi=0
        mini=float('inf')
        if maxi == prices[0]:
            return 0
        
        for num in prices:
            
            mini=min(mini, num)
            maxi=max(maxi, num - mini)
        return maxi

            
        
        

        