class Node(var `val`: Int) {
    var children: List<Node?> = listOf()

    override fun toString(): String {
        return "Node(${`val`})"
    }
}

// O(n) time and memory complexity for a tree with n nodes
fun postorder(root: Node?): List<Int> {
    if (root == null) {
        return listOf()
    }
    val res = mutableListOf<Int>() // res is appended to n times
    fun aux(node: Node) { // called once for every node of the tree (n times)
        node.children.filterNotNull().forEach {
            aux(it)
        }
        res.add(node.`val`)
    }

    aux(root)

    return res
}

fun main() {
    val root = Node(1)
    val three = Node(3)
    root.children = listOf(three, Node(2), Node(4))
    three.children = listOf(Node(5), Node(6))
    print(postorder(root).joinToString())
}