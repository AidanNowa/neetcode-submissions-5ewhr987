class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            if area > curr_max:
                curr_max = area
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return curr_max

        