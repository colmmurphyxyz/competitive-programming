from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # find the 'head' of the filtered LL
        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return None
        def aux(node: Optional[ListNode]) -> Optional[ListNode]:
            n = node.next
            while n is not None and n.val == val:
                n = n.next
            node.next = n
            if n is None:
                return node
            return aux(node.next)
        aux(head)
        return head
    
def printLinkedList(head: ListNode):
    if head is None:
        print()
        return
    print(head.val, end = " ")
    if head.next is not None:
        print("->", end = " ")
        return printLinkedList(head.next)
    else:
        print()
        return
    
def llFromList(elems: list[int]) -> ListNode:
    head = ListNode(elems[0])
    tail = head
    for i in range(1, len(elems)):
        tail.next = ListNode(elems[i])
        tail = tail.next
    return head

print("here")
if __name__ == "__main__":
    s = Solution()
    head = s.removeElements(llFromList([1, 2, 6, 3, 4, 6]), 6)
    printLinkedList(head)
    head = s.removeElements(llFromList([7, 7, 7, 7]), 7)
    printLinkedList(head)
    print("done")
