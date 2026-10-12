class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        target = nums[right]
        while(left <= right):
            middle = (left+right)//2
            if(nums[middle] > target):	
                left = middle + 1
            elif(nums[middle] < target):
                target = nums[middle]
                right = middle - 1
            else:
                return target

        return target

        