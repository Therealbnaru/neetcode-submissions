class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(step) -> int:
            if step in memo:
                return memo[step]
            if(step == n):
                return 1
            if(step < n):
                x = climb(step + 1)
                y = climb(step + 2)
                memo[step] = x + y
                return x+y
            
            return 0

        return climb(0)
