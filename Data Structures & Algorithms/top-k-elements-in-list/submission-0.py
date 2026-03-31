class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        #counting the frequency of each digit
        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1

        arr = []
        for element, count in dict1.items():
            arr.append([count, element])
        arr.sort()

        res = []
        for i in range(k):
            temp = arr.pop(-1)
            res.append(temp[1])

        return res
