class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # Im storing in pairs as 73, 0 and 74, 1

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stack_index = stack.pop() #temp, index pair in a stack
                res[stack_index] = (i - stack_index) #This gives the diff between the warmer temps i.e the correct no of days
            stack.append([t, i])
        return res

        