import scala.collection.mutable.PriorityQueue

class ListNode(_x: Int = 0, _next: ListNode = null):
    var next: ListNode = _next
    var x: Int         = _x

implicit object ListNodeOrdering extends Ordering[ListNode]:
    def compare(lhs: ListNode, rhs: ListNode): Int =
        rhs.x.compare(lhs.x)

object Solution:
    def mergeKLists(lists: Array[ListNode]): ListNode =
        if lists.length == 0 then return null
        var pq: PriorityQueue[ListNode] = new PriorityQueue[ListNode]()

        def getNextNode(): ListNode =
            val nextNode = pq.dequeue()
            if nextNode.next != null then
                pq.addOne(nextNode.next)
                nextNode.next = null
            nextNode

        // add the head of each list to the pq
        pq.addAll(
            // ignoring lists with no elements
            lists.filter(node => node != null)
        )

        if pq.isEmpty then return null

        // pop the minimum value, this will be the head of our sorted list
        val head = getNextNode()
        if pq.isEmpty then return head
        var tail = getNextNode()
        head.next = tail

        while !pq.isEmpty do
            val nextNode = getNextNode()
            tail.next = nextNode
            tail = nextNode

        head

// LL HELPERS

def makeLinkedList(elems: Array[Int]): ListNode =
    if elems.length == 0 then return null
    else if elems.length == 1 then return ListNode(elems.head)

    @annotation.tailrec
    def builder(nodes: Array[Int], tail: ListNode): ListNode =
        if nodes.isEmpty then return tail
        tail.next = ListNode(nodes.head, null)
        builder(nodes.tail, tail.next)

    val head = ListNode(elems.head, null)
    val tail = builder(elems.tail, head)
    head

def showLinkedList(head: ListNode): String =
    var res  = "[ "
    var curr = head
    while (curr != null) {
        res += curr.x.toString + " "
        curr = curr.next
    }
    res + "]"

// TESTBENCH

val lists = Array[Array[Int]](
  Array[Int](1, 4, 5),
  Array[Int](1, 3, 4),
  Array[Int](2, 6)
).map(makeLinkedList)

val sortedHead = Solution.mergeKLists(lists)

println(showLinkedList(sortedHead))

println(
  showLinkedList(
    Solution.mergeKLists(
      Array[ListNode]()
    )
  )
)

println(
    showLinkedList(
        Solution.mergeKLists(
            Array[ListNode](null)
        )
    )
)
