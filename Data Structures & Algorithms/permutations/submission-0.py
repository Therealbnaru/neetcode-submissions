class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append(nums)
        resSet = set()
        resSet.add(tuple(nums))
        def tate(nums: List[int]) -> None:
            curr = nums.copy()
            for x in range(1, len(nums)):
                temp = curr[0]
                curr[0] = curr[x]
                curr[x] = temp
                if(tuple(curr) not in resSet):
                    res.append(curr)
                    resSet.add(tuple(curr))
                    tate(curr)
                curr = nums.copy()
        
        tate(nums)
        return res






#flip exists return
#otherwise continue
