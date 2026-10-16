class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        maxRob1 = 0
        maxRob2 = 0

        nums1 = nums.copy()
        nums2 = nums.copy()
    
        nums1.pop(0)
        nums2.pop()

        nums1.append(0)
        nums1.append(0)

        nums2.append(0)
        nums2.append(0)
        
        for x in range(len(nums)-3, -1, -1):
            maxRob1 = max(maxRob1, nums1[x+2])
            maxRob2 = max(maxRob2, nums2[x+2])
            nums1[x] += maxRob1
            nums2[x] += maxRob2
        
        return         max(max(nums1[0],nums1[1]),max(nums2[0],nums2[1]))

       
#[14,13,14,5,6,2,0,0]
#