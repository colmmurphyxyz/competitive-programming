class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
    fun shouldCarry(l1: ListNode?, l2: ListNode?, carry: Boolean): Boolean {
         return (l1?.`val` ?: 0) + (l2?.`val` ?: 0) + (if (carry) 1 else 0) >= 10
    }
    fun sumNodes(l1: ListNode?, l2: ListNode?, carry: Boolean): ListNode {
        var sum = 0
        l1?.`val`?.let {
            sum += it
        }
        l2?.`val`?.let {
            sum += it
        }
        if (carry) {
            sum += 1
        }
        return ListNode(sum % 10)
    }

    val dummyHead = ListNode(-1)
    var tail: ListNode = dummyHead

    var c1 = l1
    var c2 = l2

    var carry = false

    while (c1 != null || c2 != null) {
        tail.next = sumNodes(c1, c2, carry)
        tail = tail.next!!
        carry = shouldCarry(c1, c2, carry)

        if (c1 != null) {
            c1 = c1.next
        }
        if (c2 != null) {
            c2 = c2.next
        }
    }

    if (carry) {
        tail.next = ListNode(1)
    }

    return dummyHead.next
}

fun makeLinkedList(nums: IntArray): ListNode {
    val iter = nums.iterator()
    val root = ListNode(iter.next())
    var tail: ListNode
    if (iter.hasNext()) {
        tail = ListNode(iter.next())
        root.next = tail
    } else {
        return root
    }
    while (iter.hasNext()) {
        tail.next = ListNode(iter.next())
        tail = tail.next!!
    }

    return root
}

fun ListNode.joinToString(separator: CharSequence=", "): String {
    val items = mutableListOf<Int>()
    var curr: ListNode? = this
    while (curr != null) {
        items.add(curr.`val`)
        curr = curr.next
    }
    return items.joinToString(separator)
}

fun main() {
    val l1 = makeLinkedList(intArrayOf(2, 4, 3))
    val l2 = makeLinkedList(intArrayOf(5, 6, 4))
    println(addTwoNumbers(l1, l2)?.joinToString())
    val l12 = makeLinkedList(intArrayOf(0, 0))
    val l22 = makeLinkedList(intArrayOf(0, 0))
    println(addTwoNumbers(l12, l22)?.joinToString())
    val l13 = makeLinkedList(intArrayOf(9, 9, 9, 9, 9, 9, 9))
    val l23 = makeLinkedList(intArrayOf(9, 9, 9, 9))
    println(addTwoNumbers(l13, l23)?.joinToString())
}