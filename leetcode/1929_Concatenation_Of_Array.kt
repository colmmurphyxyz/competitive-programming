fun getConcatenation(nums: IntArray): IntArray = IntArray(2 * nums.size) { nums[it % nums.size] }

fun main() {
    println(getConcatenation(intArrayOf(1, 2, 1)).joinToString())
    println(getConcatenation(intArrayOf(1, 3, 2, 1)).joinToString())
}