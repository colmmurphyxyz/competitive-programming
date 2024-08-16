fun maximumWealth(accounts: Array<IntArray>): Int =
    accounts
        .map(IntArray::sum)
        .max()

fun main() {
    println(maximumWealth(
        arrayOf<IntArray>(
            intArrayOf(1, 2, 3),
            intArrayOf(3, 2, 1)
        )
    )) // 6
    println(maximumWealth(
        arrayOf<IntArray>(
            intArrayOf(1, 5),
            intArrayOf(7, 3),
            intArrayOf(3, 5)
        )
    )) // 10
    println(maximumWealth(
        arrayOf<IntArray>(
            intArrayOf(2, 8, 7),
            intArrayOf(7, 1, 3),
            intArrayOf(3, 5)
        )
    )) // 17
}