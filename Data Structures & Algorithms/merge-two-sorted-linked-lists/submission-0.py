# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = list1
        current2  = list2
        startingNode = None

        if current is None and current2 is None:
            return None
        if current is None:
            top = current2
            current2 = current2.next
        elif current2 is None:
            top = current
            current = current.next
        elif current.val < current2.val:
            top = current
            current = current.next
        else:
            top = current2
            current2 = current2.next

        startingNode = top
            
        while current is not None and current2 is not None:
            if(current.val < current2.val):
                top.next = current
                current = current.next
            elif(current.val > current2.val):
                top.next = current2
                current2 = current2.next
            else:
                top.next = current
                current = current.next

            top = top.next

        
        while(current is not None):
            top.next = current
            top = top.next
            current = current.next

        while(current2 is not None):
            top.next = current2 
            top = top.next
            current2 = current2.next

        return startingNode
        

        
        