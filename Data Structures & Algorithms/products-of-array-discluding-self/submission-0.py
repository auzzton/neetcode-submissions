class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l_mul, r_mul = 1, 1

        n = len(nums)

        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n): #Traversing from left to right
            j = -i-1 #Traversing from right from left
            l_arr[i] = l_mul
            r_arr[j] = r_mul
            l_mul = l_mul * nums[i]
            r_mul = r_mul * nums[j]

        res = []
        for i in range(len(l_arr)): #finding result by multiplying left and right array
            res.append(l_arr[i] * r_arr[i])

        return res


        