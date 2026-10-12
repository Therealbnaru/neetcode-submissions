class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        index = 0
	
        while(start <= end):
            index = (start + (end-start)//2)
            if(nums[index] < target):
                start = index + 1
            elif(nums[index] > target):
                end = index - 1
            elif(nums[index] == target):
                return index
			

        return -1

        