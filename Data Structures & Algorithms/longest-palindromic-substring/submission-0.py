class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resIndex,resLen = 0,0
        dp = [[False] * n for x in range(n)]

        for x in range(n-1,-1,-1):
            for y in range(x,n):
                if(s[x] == s[y] and (y - x <= 2 or dp[x+1][y-1] == True)):
                    dp[x][y] = True
                    if(resLen < (y-x+1)):
                        resIndex = x
                        resLen = y-x+1
        
        return s[resIndex: resIndex + resLen ]



     








        