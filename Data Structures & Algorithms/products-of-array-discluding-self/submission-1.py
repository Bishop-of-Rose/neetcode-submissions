class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        output = [1] * len(nums)

        for i in range(len(nums)):
            if i != 0:
                prefix[i] = prefix[i - 1] * nums[i - 1]

        for j in range(len(nums) - 1, -1, -1):
            if j != len(nums) - 1:
                suffix[j] = suffix[j + 1] * nums[j + 1]
        
        for k in range(len(output)):
            output[k] = prefix[k] * suffix[k]

        return output