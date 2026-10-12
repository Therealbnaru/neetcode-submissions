# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        listNodes = []  # stores every node in order
        current = head  # starts at the head

        while current is not None:  # go through the linked list
            listNodes.append(current)  # save the current node
            current = current.next  # move to the next node

        x = 0  # starts from the front
        y = len(listNodes) - 1  # starts from the back
        changes = 0  # keeps track of whether we use front or back

        while x < y:
            if changes % 2 == 0:
                listNodes[x].next = listNodes[y]  # front node points to back node
                x += 1  # move front forward

            else:
                listNodes[y].next = listNodes[x]  # back node points to front node
                y -= 1  # move back backward

            changes += 1

        if len(listNodes) > 0:
            listNodes[x].next = None  # make sure the reordered list ends

        