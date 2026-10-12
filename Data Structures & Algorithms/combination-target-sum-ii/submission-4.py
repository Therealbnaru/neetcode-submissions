class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def perm(index, curr, sumA) -> None:
            if(sumA == target):
                res.append((curr.copy()))
                return
            if(sumA > target):
                return

            if(index >= len(candidates)):
                return
            
            curr.append(candidates[index])
            perm(index + 1, curr, sumA + candidates[index])
            curr.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1

            perm(index + 1, curr, sumA)

        perm(0,[],0)
        return res
            


