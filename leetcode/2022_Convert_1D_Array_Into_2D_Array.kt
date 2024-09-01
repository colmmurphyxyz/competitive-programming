fun construct2DArray(original: IntArray, m: Int, n: Int): Array<IntArray> {
    if (original.size != m * n) {
        return arrayOf()
    }
    val res = ArrayList<IntArray>()
    var r = 0
    while (r < original.size) {
        res.add(
            original.sliceArray(r until (r+n))
        )
        r += n
    }
    return res.toTypedArray()
}

fun main() {
    println(
        construct2DArray(intArrayOf(1, 2, 3, 4), 2, 2)
            .joinToString {
                "[" + it.joinToString() + "]"
            }
    )
    println(
        construct2DArray(intArrayOf(1, 2, 3), 1, 3)
            .joinToString {
                "[" + it.joinToString() + "]"
            }
    )
    println(
        construct2DArray(intArrayOf(1, 2), 1, 1)
            .joinToString {
                "[" + it.joinToString() + "]"
            }
    )
}