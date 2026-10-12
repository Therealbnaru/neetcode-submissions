class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        index = 0
        final = head

        while current:
            current = current.next
            index += 1

        prev = None
        current = head

        for x in range(0, index):
            if index - x == n:
                if prev is None and current.next is None:
                    final = None

                elif prev is None:
                    final = current.next

                elif current.next is None:
                    prev.next = None

                else:
                    prev.next = current.next

                return final

            prev = current
            current = current.next

        return final