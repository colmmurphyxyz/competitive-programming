from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        if self.next:
            return self.val + " " + str(self.next)
        else:
            return self.val

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head = head
        def aux(reversed_head: ListNode, curr: Optional[ListNode]) -> ListNode:
            if not curr:
                return reversed_head
            next = curr.next
            curr.next = reversed_head
            return aux(curr, next)
        return aux(None, head)
