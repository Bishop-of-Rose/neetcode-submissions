class Solution:
    def trap(self, height: List[int]) -> int:
        height = [0] + height + [0]
        amount = [0 for _ in range(len(height))] 
        prefix = [0 for _ in range(len(height))]
        suffix = [0 for _ in range(len(height))]
        for k in range(1, len(height) - 1, 1):
            prefix[k] = max(prefix[k - 1], height[k - 1])

        for k in range(len(height) - 2, 0, -1):
            suffix[k] = max(suffix[k + 1], height[k + 1])

        for k in range(len(amount)):
            amount[k] = min(prefix[k], suffix[k]) - height[k]
            if amount[k] < 0:
                amount[k] = 0

        amount = amount[1:len(amount) - 1]

        return sum(amount)


        