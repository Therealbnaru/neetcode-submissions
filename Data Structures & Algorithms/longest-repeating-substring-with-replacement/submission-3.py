class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        occuranceCount = {}
        res = 0
        for x in range(len(s)):
            occuranceCount[s[x]] = 1 + occuranceCount.get(s[x],0)

            while(x-start+1) - max(occuranceCount.values()) > k:
                occuranceCount[s[start]] -= 1 
                start += 1

            res = max(res, (x-start)+1)

        return res