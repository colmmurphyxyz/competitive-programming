import kotlin.math.abs
import kotlin.math.max

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

fun height(node: TreeNode?): Int {
    if (node == null) return 0
    return 1 + max(height(node.left), height(node.right))
}

fun isBalanced(root: TreeNode?): Boolean {
    if (root == null) {
        return true
    }

    val leftHeight = height(root.left)
    var rightHeight = height(root.right)

    if (abs(leftHeight - rightHeight) > 1) {
        return false
    }

    return isBalanced(root.left) && isBalanced(root.right)
}