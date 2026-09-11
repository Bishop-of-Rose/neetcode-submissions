class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        for i in numset:
            nums.remove(i)
            if i in nums:
                return True
        
        return False
        