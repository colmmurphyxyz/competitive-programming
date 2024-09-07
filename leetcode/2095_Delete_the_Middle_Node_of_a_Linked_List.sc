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

    var fast: ListNode = head
    var slow: ListNode = head

    while (true) {
      fast = fast.next.next
      if (fast == null) {
        slow.next = slow.next.next
        return head
      }
      if (fast.next == null) {
        slow.next = slow.next.next
        return head
      }
      slow = slow.next
    }
    slow.next = slow.next.next
    head
  }
}
