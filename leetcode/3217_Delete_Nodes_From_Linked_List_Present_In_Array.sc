import scala.collection.immutable.Set

class ListNode(_x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var x: Int = _x
}

object Solution {

  private def firstNodeWhere(head: ListNode)(predicate: (ListNode) => Boolean): Option[ListNode] = {
    if (head == null) {
      return Option.empty
    }
    var curr: Option[ListNode] = Option(head)
    while (curr.isDefined) {
      if (predicate(curr.get)) {
        return curr
      }
      curr = Option(curr.get.next)
    }
    Option.empty
  }

  private def nextNodeWhere(head: ListNode)(predicate: (ListNode) => Boolean): Option[ListNode] = {
    firstNodeWhere(head.next)(predicate)
  }

  def modifiedList(nums: Array[Int], head: ListNode): ListNode = {
    val toRemove: Set[Int] = nums.toSet
    // Increment HEAD until its value is not in `toRemove`
    // input list is guaranteed to contain at least one element not in `toRemove`
    // No need to handle case where the while loop iterates through the entire list
    val resultHead: ListNode = firstNodeWhere(head)(node =>
      !toRemove.contains(node.x)
    ).get

    var curr: Option[ListNode] = Option(resultHead)
    while (curr.isDefined) {
      val nextNode = nextNodeWhere(curr.get)(node =>
        !toRemove.contains(node.x)
      )
      curr.get.next = nextNode.orNull
      curr = Option(curr.get.next)
    }
    
    resultHead
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

println( // 3 - 8
  showLinkedList(
    Solution.modifiedList(
      Array[Int](1, 7, 6, 2, 4),
      makeLinkedList(Array[Int](3, 7, 1, 8, 1))
    )
  )
)

println( // 4 - 5
  showLinkedList(
    Solution.modifiedList(
      Array[Int](1, 2, 3),
      makeLinkedList(Array[Int](1, 2, 3, 4, 5))
    )
  )
)

println( // 2 - 2 - 2
  showLinkedList(
    Solution.modifiedList(
      Array[Int](1),
      makeLinkedList(Array[Int](1, 2, 1, 2, 1, 2))
    )
  )
)

println( // 1 - 2 - 3 - 4
  showLinkedList(
    Solution.modifiedList(
      Array[Int](5),
      makeLinkedList(Array[Int](1, 2, 3, 4))
    )
  )
)
