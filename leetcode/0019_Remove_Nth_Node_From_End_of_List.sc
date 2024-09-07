class ListNode(var _x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var x: Int = _x
}

object Solution {
  def removeNthFromEnd(head: ListNode, n: Int): ListNode = {
    var fast: ListNode = head
    var slow: ListNode = head
    // check edge case where list has length 1
    if (head.next == null) {
      return null
    }
    // move fast forward by n nodes
    for (_ <- 0 until n) {
      fast = fast.next
    }
    // edge case where we need to remove the nth last node of a list with n elements
    // to handle this, remove the head and return the following node
    if (fast == null) {
      return head.next
    }
    // move `fast` and `slow` at the same pace until `fast` reaches the end of the list
    // `slow` will be at the node before the node to be removed
    while (fast.next != null) {
      fast = fast.next
      slow = slow.next
    }
    // remove the node after `slow`
    slow.next = slow.next.next
    head
  }
}

def makeLinkedList(elems: Array[Int]): ListNode = {
  if (elems.isEmpty) {
    return null
  }
  val head = ListNode(elems(0), null)
  var curr: ListNode = head
  for (i <- 1 until elems.length) {
    curr.next = ListNode(_x = elems(i), _next = null)
    curr = curr.next
  }
  head
}

def showLinkedList(head: ListNode): String = {
  var res = "[ "
  var curr = head
  while (curr != null) {
    res += curr.x.toString + " "
    curr = curr.next
  }
  res + "]"
}

println( // 1 - 2 - 3 - 5
  showLinkedList(
    Solution.removeNthFromEnd(
      makeLinkedList(Array[Int](1, 2, 3, 4, 5)),
      2
    )
  )
)

println( // *empty*
  showLinkedList(
    Solution.removeNthFromEnd(
      makeLinkedList(Array[Int](1)),
      1
    )
  )
)

println( // 1
  showLinkedList(
    Solution.removeNthFromEnd(
      makeLinkedList(Array[Int](1, 2)),
      1
    )
  )
)

println( // 2
  showLinkedList(
    Solution.removeNthFromEnd(
      makeLinkedList(Array[Int](1, 2)),
      2
    )
  )
)
