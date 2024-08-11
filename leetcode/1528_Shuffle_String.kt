/**
 * Time: O(n)
 * Space: O(n)
 */
fun restoreString(s: String, indices: IntArray): String {
    val n = s.length
    val output = CharArray(n)
    for (i in s.indices) {
        output[indices[i]] = s[i]
    }
    return output.concatToString()
}

fun main() {
    println(restoreString("codeleet", intArrayOf(4, 5, 6, 7, 0, 2, 1, 3)))
    println(restoreString("abc", intArrayOf(0, 1, 2)))
}