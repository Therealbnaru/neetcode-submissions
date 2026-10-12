class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counterDict = Counter(nums)
        retList = []
        fin = []

        sortedLict = sorted(counterDict.items(), key=lambda item: item[1], reverse=True)
        
        for x in range(k):
            retList.append(sortedLict[x][0])
        return retList

        