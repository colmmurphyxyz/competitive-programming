class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

fun minDepth(root: TreeNode?): Int {
    if (root == null) return 0
    if (root.left == null && root.right == null) return 1

    val leftDepth = minDepth(root.left)
    val rightDepth = minDepth(root.right)

    return if (leftDepth == 0 || rightDepth == 0) {
        leftDepth + rightDepth + 1
    } else {
        minOf(leftDepth, rightDepth) + 1
    }
}