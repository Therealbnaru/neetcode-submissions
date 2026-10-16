class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        nums.append(0)
        maxRobbed = 0
        for x in range(len(nums)-3,-1,-1):
            prev = nums[x+2]
            maxRobbed = max(prev, maxRobbed)
            nums[x] += maxRobbed
            
        return max(nums[0],nums[1])
            
        