class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        length = 0
        longest = 0
        for x in nums:
            if((x - 1) not in setNums):
                length = 1
                while(x + length in setNums):
                    length += 1
                longest = max(length,longest)
        
        return longest
