class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            i = numbers[l] + numbers[r]
            if i == target:
                return [l + 1, r + 1]
            
            if i > target:
                r = r - 1

            if i < target:
                l = l + 1