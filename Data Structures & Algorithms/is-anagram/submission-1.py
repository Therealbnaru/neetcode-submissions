class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dictChar = {}
        for x in t:
            if x in dictChar:
                dictChar[x] += 1
            else:
                dictChar[x] = 1

        for x in s:
            if x in dictChar:
                if(dictChar[x] > 0):
                    dictChar[x] -= 1
                else:
                    return False
            else:
                return False
                
        if(len(s) != len(t)): 
            return False
        return True