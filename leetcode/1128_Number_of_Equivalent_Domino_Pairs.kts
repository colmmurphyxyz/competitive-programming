//fun hash(domino: IntArray): Int {
//    // only need the first 9 primes, as 1 <= domino[i] <= 9
//    val primes = listOf(2, 3, 5, 7, 11, 13, 17, 19, 23)
//    val (a, b) = domino
//    return primes[a - 1] * primes[b - 1]
//}

fun hash(domino: IntArray): Int {
    val (a, b) = domino
    if (a <= b) {
        return 10 * a + b - 11
    }
    return 10 * b + a - 11
}

fun numEquivDominoPairs(dominoes: Array<IntArray>): Int {
    var ans = 0
    val buckets = IntArray(89) { 0 }
    for (domino in dominoes) {
        val h = hash(domino)
        ans += buckets[h]
        buckets[h]++
    }

    return ans
}

//fun equiv(lhs: IntArray, rhs: IntArray): Boolean {
//    val (a, b) = lhs
//    val (c, d) = rhs
//    return (a == c && b == d) or (a == d && b == c)
//}

//fun numEquivDominoPairs(dominoes: Array<IntArray>): Int {
//    var ans = 0
//    for (i in 0 until dominoes.lastIndex) {
//        for (j in (i + 1) ..dominoes.lastIndex) {
//            if (equiv(dominoes[i], dominoes[j])) {
//                ans++
//            }
//        }
//    }
//
//    return ans
//}

fun main() {
    println(numEquivDominoPairs(arrayOf(intArrayOf(1, 2), intArrayOf(2, 1), intArrayOf(3, 4), intArrayOf(5, 6))))
    println(numEquivDominoPairs(arrayOf(intArrayOf(1, 2), intArrayOf(1, 2), intArrayOf(1, 1), intArrayOf(1, 2), intArrayOf(2, 2))))
}

main()