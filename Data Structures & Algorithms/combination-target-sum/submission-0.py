class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def checks(arr, sumA,stage) -> None:
            if(sumA >= target):
                if(sumA == target):
                    res.append(arr.copy())
                return

            if(stage >= len(nums)):
                return
            arr.append(nums[stage])
            checks(arr, sumA + nums[stage],stage)
            arr.pop()
            checks(arr, sumA, stage + 1)

        checks([],0,0)
        return res


       
        

        
        


    

