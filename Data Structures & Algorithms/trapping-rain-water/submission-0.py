class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left, max_right, min_both, output = [0]*n, [0]*n, [0]*n, [0]*n
        min_val = 0

        for i in range(len(height)):
            if i == 0:
                max_left[i] = 0
            else:
                max_left[i] = max(height[i-1], max_left[i-1])

        for j in range(len(height)-1, -1, -1):
            if j == len(height)-1:
                max_right[j] = 0
            else:
                max_right[j] = max(height[j+1], max_right[j+1])

        for k in range(len(height)):
            min_both[k] = min(max_left[k], max_right[k])
            output[k] = max(min_both[k] - height[k], 0)

        return sum(output)