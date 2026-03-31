from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in dict1:
                dict1[key] = []

            dict1[key].append(word)

        return list(dict1.values())