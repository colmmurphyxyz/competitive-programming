import kotlin.math.abs

/**
 * Time: O(n)
 * Space: O(1)
 * @param s String consisting of lowercase English characters. guaranteed to be between 2 and 100 chars in length
 */
fun scoreOfString(s: String): Int {
    val absDiff: (Char, Char) -> Int = { s1, s2 ->
        abs(s1.code - s2.code)
    }
    var sum = 0
    for (i in 0 until s.lastIndex) {
        val left = s[i]
        val right = s[i + 1]
        sum += absDiff(left, right)
    }

    return sum
}

fun main() {
    println(scoreOfString("hello")) // 13
    println(scoreOfString("zaz")) // 50
}