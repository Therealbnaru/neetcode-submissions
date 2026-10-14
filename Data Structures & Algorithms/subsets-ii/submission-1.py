class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def perm(stage, curr):
            if(stage >= len(nums)):
                res.append(curr.copy())
                return

            eqP = 0
            eqT = 0
            for x in range(0, stage):
                if(nums[x] == nums[stage]):
                    eqP += 1
            for x in range(0, len(curr)):
                if(curr[x] == nums[stage]):
                    eqT += 1
            
            if(eqP == eqT):
                curr.append(nums[stage])
                perm(stage + 1, curr)
                curr.pop()
                perm(stage + 1, curr)

            else:
                perm(stage + 1, curr)

        perm(0, curr)
        return res
        