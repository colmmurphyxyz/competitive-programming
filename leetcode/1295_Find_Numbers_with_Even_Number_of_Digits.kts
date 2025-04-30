fun digitCount(num: Int): Int =
    when (num) {
        0 -> 0
        else -> 1 + digitCount(num / 10)
    }

fun findNumbers(nums: IntArray): Int {
    return nums
        .map(::digitCount)
        .count { it % 2 == 0 }
}

fun main() {
    println(findNumbers(intArrayOf(12, 345, 2, 6, 7896)))
    println(findNumbers(intArrayOf(555, 901, 482, 1771)))
}

main()