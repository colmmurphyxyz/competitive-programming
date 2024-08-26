/**
 * Builds and returns a list containing the frequency count of a string consisting of lower-case, english letters
 */
fun frequencyList(s: String): List<Int> {
    val res = MutableList<Int>(26) { 0 }
    s.forEach {
        val idx = it.code - 97
        res[idx]++
    }
    return res
}

fun groupAnagrams(strs: Array<String>): List<List<String>> {
    val map = strs.groupBy { frequencyList(it) }
    return map.values.toList()
}

fun main() {
    println(
        groupAnagrams(arrayOf("eat","tea","tan","ate","nat","bat"))
            .joinToString {
                "[" + it.joinToString() + "]"
            }
    )
}