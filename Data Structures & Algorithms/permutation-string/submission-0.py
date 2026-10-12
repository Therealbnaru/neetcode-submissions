class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        stringDict = {}
        for x in range(len(s1)):
            stringDict[s1[x]] = 1 + stringDict.get(s1[x],0)

        start = 0
        lenS = 0

        for x in range(len(s2)): 
            if(s2[x] in stringDict):
                stringDict[s2[x]] -= 1
                lenS += 1

                while(stringDict[s2[x]] < 0 ):
                    stringDict[s2[start]] += 1
                    start += 1
                    lenS -= 1


            else:
                while start < x:
                    if(s2[start] in stringDict):
                        stringDict[s2[start]] += 1
                        start += 1

                start = x + 1
                lenS = 0			


            if(lenS == len(s1)):
                return True

        return False

        