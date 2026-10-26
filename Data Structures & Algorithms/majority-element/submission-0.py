class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1

        max = (0, 0)
        for key, value in nums_dict.items():
            if value >= max[1]:
                max = (key, value)
        
        return max[0]