import scala.annotation.tailrec

class ListNode(_x: Int = 0, _next: ListNode = null) {
    var next: ListNode = _next
    var x: Int = _x
}

object Solution:
    @tailrec
    private def gcd(a: Int, b: Int): Int =
        if b == 0 then
            return a
        else
            return gcd(b, a % b)

    def insertGreatestCommonDivisors(head: ListNode): ListNode =
        // handle case where list length is 1
        if head.next == null then
            return head
        var left: ListNode = head
        var right: ListNode = head.next
        while right != null do
            val middle = ListNode(gcd(left.x, right.x), right)
            left.next = middle
            right = right.next
            left = left.next.next
        
        head

def makeLinkedList(elems: Array[Int]): ListNode =
    if elems.length == 0 then
        return null
    else if elems.length == 1 then
        return ListNode(elems.head)

    @tailrec
    def builder(nodes: Array[Int], tail: ListNode): ListNode =
        if nodes.isEmpty then
            return tail
        tail.next = ListNode(nodes.head, null)
        builder(nodes.tail, tail.next)

    val head = ListNode(elems.head, null)
    val tail = builder(elems.tail, head)
    head

def showLinkedList(head: ListNode): String = {
  var res = "[ "
  var curr = head
  while (curr != null) {
    res += curr.x.toString + " "
    curr = curr.next
  }
  res + "]"
}

def printLinkedList(head: ListNode): Unit =
    print("[ ")
    def aux(node: ListNode): Unit =
        print(s"${node.x} ")
        if node.next != null then
            aux(node.next)
    aux(head)
    print("]\n")

val nums = Array[Int](18, 6, 10, 3)

printLinkedList(makeLinkedList(nums))

printLinkedList(Solution.insertGreatestCommonDivisors(
    makeLinkedList(Array[Int](18, 6, 10, 3))
))