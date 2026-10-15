import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = [-x for x in stones]
        heapq.heapify(nums)
        
        print(nums)
        while(len(nums) > 1):
            stone1 = heapq.heappop(nums)
            stone2 = heapq.heappop(nums)
            print(stone1)
            print(stone2)
            if(stone1 == stone2):
                continue
            heapq.heappush(nums, stone1-stone2)


        if(len(nums) == 0):
            return 0
        else:
            return -1 * heapq.heappop(nums)
                
        