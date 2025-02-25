from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"Node({self.val}, {self.next.val if self.next else 'None'})"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def aux(merged: Optional[ListNode], left: Optional[ListNode], right: Optional[ListNode]) -> None:
            print("Iteration")
            if left is None and right is None:
                return
            if left is None:
                merged.next = ListNode(right.val)
                right = right.next
                return aux(merged.next, left, right)
            if right is None:
                merged.next = ListNode(left.val)
                left = left.next
                return aux(merged.next, left, right)
            if left.val <= right.val:
                merged.next = ListNode(left.val)
                left = left.next
                return aux(merged.next, left, right)
            else:
                merged.next = ListNode(right.val)
                right = right.next
                return aux(merged.next, left, right)
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            merged_head = ListNode(list1.val)
            list1 = list1.next
        else:
            merged_head = ListNode(list2.val)
            list2 = list2.next
        print("Using HEAD", merged_head)
        aux(merged_head, list1, list2)
        return merged_head
    
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

if __name__ == "__main__":
    s = Solution()
    left = llFromList([1, 2, 4])
    right = llFromList([1, 3, 4])
    merged = s.mergeTwoLists(left, right)
    printLinkedList(merged)
    merged = s.mergeTwoLists(None, None)
    printLinkedList(merged)
