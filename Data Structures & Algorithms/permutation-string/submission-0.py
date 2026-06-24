class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer, it can't be a substring permutation
        if len(s1) > len(s2):
            return False

        # Frequency arrays for s1 and current window in s2
        s1Count = [0] * 26
        s2Count = [0] * 26

        # Fill counts for s1 and first window of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Count how many character frequencies match
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        left = 0

        # Slide the window
        for right in range(len(s1), len(s2)):

            # If all 26 frequencies match, permutation found
            if matches == 26:
                return True

            # Add new character on the right
            index = ord(s2[right]) - ord('a')
            s2Count[index] += 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Remove left character
            index = ord(s2[left]) - ord('a')
            s2Count[index] -= 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            left += 1

        # Check the final window
        return matches == 26
        