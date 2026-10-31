class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def maxheapify(i, heapsize):
            l = 2 * i + 1
            r = 2 * i + 2
            largest = i
            if l < heapsize and nums[l] > nums[largest]:
                largest = l
            if r < heapsize and nums[r] > nums[largest]:
                largest = r
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                maxheapify(largest, heapsize)

        for i in reversed(range(len(nums)//2)):
            maxheapify(i, len(nums))

        mark = len(nums)
        while mark != 0:
            mark -= 1
            nums[0], nums[mark] = nums[mark], nums[0]
            maxheapify(0, mark)

        return nums