class ListNode(_x: Int = 0, _next: ListNode = null):
    var next: ListNode = _next
    var x: Int         = _x

implicit class TupleAdd(t: (Int, Int)):
    def +(p: (Int, Int)) = (p._1 + t._1, p._2 + t._2)

object Solution:
    private def build2DMatrix(
        rows: Int,
        cols: Int,
        initialValue: Int
    ): Array[Array[Int]] =
        Array.fill(rows)(Array.fill(cols)(initialValue))

    private def rotateClockwise(vector: (Int, Int)): (Int, Int) =
        vector match {
            case (0, 1) => (1, 0)
            case (1, 0) => (0, -1)
            case (0, -1) => (-1, 0)
            case (-1, 0) => (0, 1)
        }

    private def fillSpiral(
        spiral: Array[Array[Int]],
        node: ListNode,
        direction: (Int, Int),
        curr: (Int, Int)
    ): Array[Array[Int]] =
        if node == null then return spiral
        var candidatePoint: (Int, Int) = curr + direction
        var newDirection = direction
        if (
            candidatePoint._2 >= spiral.head.length
            || candidatePoint._2 < 0
            || candidatePoint._1 >= spiral.length
            || candidatePoint._1 < 0
            || spiral(candidatePoint._1)(candidatePoint._2) != -1
        ) then
            println("Rotating")
            newDirection = rotateClockwise(direction)
            candidatePoint = curr + newDirection
        println(s"Filling $candidatePoint")
        spiral(candidatePoint._1)(candidatePoint._2) = node.x
        fillSpiral(spiral, node.next, newDirection, candidatePoint)


    def spiralMatrix(m: Int, n: Int, head: ListNode): Array[Array[Int]] =
        var direction: (Int, Int) = (0, 1)
        var spiral: Array[Array[Int]] = build2DMatrix(m, n, -1)
        fillSpiral(spiral, head, direction, (0, -1))

def printMatrix[T](matrix: Array[Array[T]]): Unit =
    matrix.foreach(row =>
        print("[ ")
        row.foreach(value => print(value.toString + " \t"))
        print("]\n")
    )

def makeLinkedList(elems: Array[Int]): ListNode = {
    if (elems.isEmpty) {
        return null
    }
    val head           = ListNode(elems(0), null)
    var curr: ListNode = head
    for (i <- 1 until elems.length) {
        curr.next = ListNode(_x = elems(i), _next = null)
        curr = curr.next
    }
    head
}

printMatrix(
  Solution.spiralMatrix(
    3,
    5,
    makeLinkedList(Array[Int](3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0))
  )
)
