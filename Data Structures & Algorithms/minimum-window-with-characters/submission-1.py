class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        left = 0
        need = {}
        window = {}
        # the below code checks and updates values and keys in need as A : 1 etc
        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1
        
        have = 0 #number of unique characters whose required frequency has been satisfied in the current window
        need_count = len(need) # Total number of unique characters like  A B C
        minlength = float('inf') # Stores the length of the smallest valid window found
        result = ""

        # Expand the window by moving the right pointer
        for right in range(len(s)):
            char = s[right]

            #sliding window update
            if char in window:
                window[char] += 1
            else:
                window[char] = 1
            
            #If the current character is required and If the current character is required and its frequency now matches exactly what is needed, we have satisfied one required character.
            if char in need and window[char] == need[char]:
                have+=1
            
            while have == need_count:
                if right - left + 1 < minlength:
                    minlength = right - left + 1
                    result = s[left:right + 1]
                
                leftmost_char = s[left]
                window[leftmost_char] -= 1

                if leftmost_char in need and window[leftmost_char] < need[leftmost_char]:
                    have -= 1
                
                left+=1
        return result
            

            

