class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res=[0]*n
        stack = [] # [ind, temp]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][-1]:
                stackI, stackT = stack.pop()
                res[stackI] = i - stackI
            stack.append([i, t])

        return res        