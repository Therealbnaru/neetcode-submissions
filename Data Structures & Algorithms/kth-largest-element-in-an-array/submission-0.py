import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for x in range(k):
            num = heapq.heappop(nums)
        return -1 * num
        