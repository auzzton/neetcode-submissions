class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        

        while l<=r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:#Checking left half
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:#Checking right half
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
        