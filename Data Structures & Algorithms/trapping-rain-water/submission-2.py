class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length == 0:
            return 0
        
        leftMax = [0] * length
        rightMax = [0] * length

        leftMax[0] = height[0]
        for i in range(1, length):
            leftMax[i] = max(leftMax[i-1], height[i])

        rightMax[-1] = height[-1]
        for i in range(length - 2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        
        total = 0
        for i in range(length):
            total += min(leftMax[i], rightMax[i]) - height[i]
        
        return total
        