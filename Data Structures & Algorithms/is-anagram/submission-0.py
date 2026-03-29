class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        if len(s) != len(t):
            return False
        
        for character in range(len(s)):
            countS[s[character]] = 1 + countS.get(s[character], 0)
            countT[t[character]] = 1 + countT.get(t[character], 0)

        if countS == countT:
            return True
        else:
            return False
