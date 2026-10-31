class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        dictn = {}
        for i in nums:
            dictn[i] = dictn.get(i, 0) + 1

        listn = sorted(dictn.keys(), key=lambda x: dictn[x])
        j = len(listn) - k
        return listn[j:]