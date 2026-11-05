class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in nums]
        suffix = [1 for _ in nums]
        result = [1 for _ in nums]

        for i in range(len(nums)):
            if i == 0:
                continue

            prefix[i] = prefix[i - 1] * nums[i - 1]

        for j in reversed(range(len(nums))):
            if j == len(nums) - 1:
                continue

            suffix[j] = suffix[j + 1] * nums[j + 1]

        for k in range(len(result)):
            result[k] = prefix[k] * suffix[k]

        return result

        