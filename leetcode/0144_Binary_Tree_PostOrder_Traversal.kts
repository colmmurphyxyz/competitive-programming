class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

fun preorderTraversal(root: TreeNode?): List<Int> {
    if (root == null) return listOf()
    return listOf(root.`val`) + preorderTraversal(root.left) + preorderTraversal(root.right)
}