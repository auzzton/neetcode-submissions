class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 1
        if len(nums) == 0:
            return 0

        for num in nums:
            if num - 1 not in seen:
                nextnum = num + 1
                count = 1

                while nextnum in seen:
                    count = count + 1
                    nextnum  = nextnum + 1
                    longest = max(longest, count)
        
        return longest