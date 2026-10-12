class Solution:
    def minEatingSpeed(self, piles: List[List[int]], h: int) -> int:
        maxPile = max(piles)
        l, r = 1, maxPile
        hours = 0
        result = []
        while(l <= r):
            m = (l + r)//2
            print(m)
            for x in range(len(piles)):
                hours += piles[x]//m
                if(m > piles[x]):
                    hours += 1 
                elif(piles[x] % m > 0):
                    hours += 1
            print(hours)
            if(hours > h):
                l = m+1
            elif(hours <= h):
                r = m-1
                result.append(m)
            hours = 0
          
        return min(result)

                        