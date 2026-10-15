class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * n
        arr[0] = 1
        prev = 1

        for x in range(len(arr) - 1):
            arr[x+1] = arr[x] + prev
            prev = arr[x]

        return arr[n-1]
        

       

