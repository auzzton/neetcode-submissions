class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in dic:
                l=max(l, dic[s[r]]+1)
            dic[s[r]] = r

            res = max(res, r - l + 1)
        return res