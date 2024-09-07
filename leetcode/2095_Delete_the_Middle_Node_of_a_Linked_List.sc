class ListNode(_x: Int = 0, _next: ListNode = null) {
  var x: Int = _x
  var next: ListNode = _next
}

object Solution {
  def deleteMiddle(head: ListNode): ListNode = {
    // handle lists of size 1 or 2
    if (head.next == null) { // n = 1
      return null
    }
    if (head.next.next == null) { // n = 2
      head.next = null
      return head  
    }

    @scala.annotation.tailrec
    def helper(head: ListNode, fast: ListNode, slow: ListNode): ListNode = {
      val fastNew: ListNode = fast.next.next
      if (fastNew == null || fastNew.next == null) {
        slow.next = slow.next.next
        return head
      }
      return helper(head, fastNew, slow.next)
    }

    return helper(head, head, head)
  }
}

