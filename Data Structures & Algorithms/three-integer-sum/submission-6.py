class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        solutions = []
        for i in range(len(nums)-1):
            if nums[i] > 0:
                break
            target = 0 - nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[j] + nums[k]
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
                else:
                    solutions.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return solutions
        
        