class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maximum = [0, i, j]
        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            if area > maximum[0]:
                maximum = [area, i, j]

            if heights[i] < heights[j]:
                i += 1

            else:
                j -= 1

        return maximum[0] 



        