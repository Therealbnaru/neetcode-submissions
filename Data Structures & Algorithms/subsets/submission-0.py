class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        listLists = [[]]
        index = 0
        y = 0
        for x in nums:
            leng = len(listLists)
            while y < leng:
                current = listLists[y].copy()
                current.append(x)
                listLists.append(current)
                y += 1

            y = 0
        return listLists



