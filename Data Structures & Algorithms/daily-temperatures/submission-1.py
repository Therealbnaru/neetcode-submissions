class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*(len(temperatures))
        for x in range(len(temperatures)-1,-1,-1):
            while(len(stack) > 0 and temperatures[x] >= stack[-1][0]):
                stack.pop()
            
            if(len(stack) == 0):
                result[x] = 0
            else:
                result[x] = stack[-1][1]-x
            
            stack.append((temperatures[x],x))
          
  
        
        return result

            
        