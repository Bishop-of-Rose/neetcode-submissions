class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            if nums[i] == val:
                nums.pop(i)
                j -= 1
                continue
            i += 1

        print(nums)
        return len(nums)