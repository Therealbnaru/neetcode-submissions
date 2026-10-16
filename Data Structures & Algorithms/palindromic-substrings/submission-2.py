class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dromeCount = 0
        dp = [[False] * n for x in range(len(s))]

        for x in range(n-1,-1,-1):
            for y in range(x, n):
                if(s[x] == s[y] and (y - x <= 2 or dp[x+1][y-1] == True)):
                    dromeCount += 1
                    dp[x][y] = True
                

        return dromeCount

                    


        