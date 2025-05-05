class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}


fun postorderTraversal(root: TreeNode?): List<Int> {
    if (root == null) return listOf()
    return postorderTraversal(root.left) + postorderTraversal(root.right) + root.`val`
}