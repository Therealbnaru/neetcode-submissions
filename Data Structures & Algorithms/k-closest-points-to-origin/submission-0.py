import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums = []
        res = []
        for x in range(len(points)): 
            dist = math.sqrt(math.pow((points[x][0]-0),2) + math.pow((points[x][1]-0),2))
            tup = (dist, points[x])
            nums.append(tup)

        heapq.heapify(nums)

        for x in range(k):
            res.append(heapq.heappop(nums)[1])

        return res


        