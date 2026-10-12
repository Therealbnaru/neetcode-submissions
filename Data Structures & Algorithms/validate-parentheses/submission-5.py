class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pop = 0
        for x in s:
            if(x == "{" or x =="[" or x == "("):
                stack.append(x)
            elif(x == "}" or x == ")" or x == "]"):
                if(len(stack) == 0):
                    return False
                elif(stack[len(stack)-1] == "(" and x == ")"):
                    stack.pop()
                elif(stack[len(stack)-1] == "[" and x == "]"):
                    stack.pop()
                elif(stack[len(stack) - 1] == "{" and x == "}"):
                    stack.pop()
                else:
                    return False

        if(len(stack) == 0):
            return True
        return False
        