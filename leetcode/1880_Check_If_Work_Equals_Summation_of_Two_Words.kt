private fun letterValue(c: Char): Int
    = c.code - 97


private fun numericValue(s: String): Int
    = s.fold(0) { acc, c ->
        (acc * 10) + letterValue(c)
    }

/**
 * let F, S, T be the length of `firstWord`, `secondWord`, `targetWord` respectively
 * Time complexity is O(max(F, S, T)) (linear time)
 * Space complexity is O(max(F, S, T)) (linear space)
 */
fun isSumEqual(firstWord: String, secondWord: String, targetWord: String): Boolean
    = numericValue(firstWord) + numericValue(secondWord) == numericValue(targetWord)


fun main() {
    println(isSumEqual("acb", "cba", "cdb"))
    println(isSumEqual("aaa", "a", "aab"))
}