class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for x in nums:
            if x in numsSet:
                return True
            numsSet.add(x)
        return False