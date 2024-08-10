fun twoSum(nums: IntArray, target: Int): IntArray {
    val map = mutableMapOf<Int, Int>()
    for (i in nums.indices) {
        val num = nums[i]
        // find the value we need to sum to `target`
        val remaining = target - num
        // check if this value exists in the map
        val possibleCompanion = map.getOrDefault(remaining, -1)
        if (possibleCompanion >= 0) {
            return intArrayOf(i, possibleCompanion)
        }
        // add the current value to the map and move on
        map[num] = i
    }
    return intArrayOf() // solution is guaranteed to exist, this statement is unreachable
}

fun main() {
    println(twoSum(intArrayOf(2, 7, 11, 15), 9).joinToString())
    println(twoSum(intArrayOf(3, 2, 4), 6).joinToString())
    println(twoSum(intArrayOf(3, 3), 6).joinToString())
}