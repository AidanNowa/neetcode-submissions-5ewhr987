class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            first_num = True
            product = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                if first_num:
                    product += nums[j]
                    first_num = False
                else:
                    product *= nums[j]
            output.append(product)
        return output
        