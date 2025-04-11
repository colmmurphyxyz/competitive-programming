fun isSymmetric(x: Int): Boolean {
    val s = x.toString()
    val n = s.length
    if (n % 2 == 1) return false
    val lhs = s.take(n / 2)
    val rhs = s.drop(n / 2)
    val leftSum = lhs.foldRight(0) { digit, acc -> acc + digit.digitToInt() }
    val rightSum = rhs.foldRight(0) { digit, acc -> acc + digit.digitToInt() }
    return leftSum == rightSum
}

fun countSymmetricIntegers(low: Int, high: Int): Int {
    return (low .. high).filter(::isSymmetric).size
}

fun main() {
    // println(countSymmetricIntegers(1, 25))
    println(countSymmetricIntegers(1, 100))
    println(countSymmetricIntegers(1200, 1230))
}