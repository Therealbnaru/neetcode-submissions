class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fullProd = 1
        nonZeroProd = 1
        productList = []
        zeroCount = 0
        for x in nums:
            if(x != 0):
                nonZeroProd *= x
            else:
                zeroCount += 1
            
            fullProd *= x
            

        if(zeroCount > 1):
            return [0]*(len(nums))

        for x in range(len(nums)):
            if(nums[x] != 0):
                productList.append(int((fullProd/nums[x])))
            else:
                productList.append(int(nonZeroProd))

        return productList

        