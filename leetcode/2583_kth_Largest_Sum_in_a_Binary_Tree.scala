import scala.math.max

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution:
    private def levelSums(root: TreeNode): Array[Long] =
        Array[Long]()

    def getHeight(root: TreeNode): Int =
        def f(curr: TreeNode, height: Int): Int =
            if curr == null then
                height
            else if curr.left == null && curr.right == null then
                height + 1
            else
                1 + max(getHeight(curr.left), getHeight(curr.right))
        f(root, 0)
        
    def kthLargestLevelSum(root: TreeNode, k: Int): Long =
        val height = getHeight(root)
        if height < k then return -1
        var sums = Array.ofDim[Long](height)
        def calculateSums(curr: TreeNode, currentHeight: Int): Unit =
            if curr == null then return
            sums(currentHeight) += curr.value
            calculateSums(curr.left, currentHeight + 1)
            calculateSums(curr.right, currentHeight + 1)
        calculateSums(root, 0)
        sums.sortWith(_ > _)(k - 1)


@main def main() =
    val root = TreeNode(
        5,
        TreeNode(
            8,
            TreeNode(
                2,
                TreeNode(4),
                TreeNode(6)
            ),
            TreeNode(1)
        ),
        TreeNode(
            9,
            TreeNode(3),
            TreeNode(7)
        )
    )
    println(Solution.kthLargestLevelSum(root, 2))