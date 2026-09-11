class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numdict = {}
        for i in nums:
            if numdict.get(str(i)) is not None:
                return True

            numdict[str(i)] = ''

        return False