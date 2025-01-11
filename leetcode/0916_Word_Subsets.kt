fun alphIdx(c: Char): Int =
    c.code - 97

infix fun <T: Comparable<T>> Array<T>.isSubsetOf(rhs: Array<T>): Boolean {
    return this.zip(rhs).all { it.first <= it.second }
}

fun makeHashTable(s: String): Array<Int> {
    val result = Array<Int>(26) {0}
    for (char in s) {
        result[alphIdx(char)]++
    }
    return result
}

fun merge(arr: Array<Array<Int>>): Array<Int> =
    Array<Int>(arr[0].size) { idx -> arr.map { it[idx] }.max() }

fun wordSubsets(words1: Array<String>, words2: Array<String>): List<String> {
     val w1 = Array<Array<Int>>(words1.size) { idx -> makeHashTable(words1[idx]) }
     val w2 = Array<Array<Int>>(words2.size) { idx -> makeHashTable(words2[idx]) }

     val merged = merge(w2)
     val ret = mutableListOf<String>()
     for (i in w1.indices) {
        val word = w1[i]
        if (merged isSubsetOf word) {
            ret.add(words1[i])
        }
     }

     return ret
}

fun main() {
    println(wordSubsets(
        arrayOf("amazon", "apple", "facebook", "google", "leetcode"),
        arrayOf("e", "o")))
    println(wordSubsets(
        arrayOf("amazon", "apple", "facebook", "google", "leetcode"),
        arrayOf("l", "e")))
}