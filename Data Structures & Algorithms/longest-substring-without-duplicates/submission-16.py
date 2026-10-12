class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxHeight = 0
        startIndex = 0
        dictionaryIndicies = {}

        if(len(s) == 1):
            return 1

        for x in range(len(s)):
            if(s[x] in dictionaryIndicies):
                if(startIndex > dictionaryIndicies[s[x]]+1):
                    maxHeight = max(maxHeight, (x-startIndex)+1)
                startIndex = max(startIndex,dictionaryIndicies[s[x]] + 1)
                
                
            else:
                maxHeight = max(maxHeight, (x-startIndex)+1)

            dictionaryIndicies[s[x]] = x

        return maxHeight 

        