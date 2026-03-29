class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        check = {} #hash map
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in check:
                return [check[diff], i]

            check[nums[i]] = i
        



        
        