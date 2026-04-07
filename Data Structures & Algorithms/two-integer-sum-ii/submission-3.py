class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = -1, -1 
        for num in numbers:
            if (target - num) in numbers and numbers.index(num) != numbers.index(target-num):
                return [numbers.index(num)+1, numbers.index(target-num)+1]
        