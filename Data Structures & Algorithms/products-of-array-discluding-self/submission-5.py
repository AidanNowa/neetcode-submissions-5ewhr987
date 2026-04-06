class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1
        output = [0] * len(nums)
        for i in range(len(nums)):
            if zero_count == 1:
                if nums[i] == 0:
                    output[i] = product
                else:
                    output[i] = 0
            if zero_count == 0:
                output[i] = product // nums[i]
        return output
        