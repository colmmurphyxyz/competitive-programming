fun uniqueOccurrences(arr: IntArray): Boolean {
    val occurences = buildMap<Int, Int> {
        arr.forEach { it ->
            put(it, getOrDefault(it, 0) + 1)
        }
    }.values

    val seen = mutableSetOf<Int>()
    for (n in occurences) {
        if (n in seen) return false
        seen.add(n)
    }

    return true
}

fun main() {
    println(uniqueOccurrences(intArrayOf(1, 2, 2, 1, 1, 3)))
    println(uniqueOccurrences(intArrayOf(1, 2)))
    println(uniqueOccurrences(intArrayOf(-3, 0, 1, -3, 1, 1, 1, -3, 10, 0)))
}