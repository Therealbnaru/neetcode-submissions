class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        
        nums1 = sorted(nums)
        print(nums1)
        
        while(nums1[i] + nums1[j] != target):
            if(i != j):
                if(nums1[i] + nums1[j] > target):
                    j -= 1
                elif(nums1[i] + nums1[j] < target):
                    i += 1
                    
      
        print(nums)
        for x in range(0, len(nums)):
            if(nums[x] == nums1[i]):
                i = x
                break
        print(i)
        
        for x in range(len(nums) - 1, -1, -1):
            if(nums[x] == nums1[j]):
                j = x
                break
    

        return [min(i,j), max(i,j)]	

#[3,4,5,6] target 7