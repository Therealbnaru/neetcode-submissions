class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.replace(" ", "")
        right = len(string) - 1
        left = 0
        print(string)
        while left <= right:
            if(string[left].isalnum() and string[right].isalnum()):
                if(string[left].lower() != string[right].lower()):
                    return False  
                left += 1
                right -= 1
            elif(string[left].isalnum() == False):
                left += 1
            elif(string[right].isalnum() == False):
                right -= 1
       
              

        return True

        