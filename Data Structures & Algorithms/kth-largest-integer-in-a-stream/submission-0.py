import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums = [-x for x in nums]
        heapq.heapify(nums)
        self.numsHeap = nums
        self.num = k
        
    def add(self, val: int) -> int:
        heapq.heappush(self.numsHeap, -1 * val)
        temp = []
        for x in range(self.num):
            tem = heapq.heappop(self.numsHeap)
            temp.append(tem)

        for x in temp:
            heapq.heappush(self.numsHeap,x)
        return tem * -1


        

        
