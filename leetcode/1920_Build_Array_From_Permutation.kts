fun buildArray(nums: IntArray): IntArray {
    return IntArray(nums.size) { it -> nums[nums[it]] }
}

// Constant time implementation
fun buildArrayOptimised(nums: IntArray): IntArray {
    // All values in nums are <= 1000 -> can be represented in 10 bits or less
    // the idea is to store the 'updated' value of each index in the upper bits of the 32-bit value
    for (i in nums.indices) {
        val nextIdx = nums[i]
        if (nextIdx < i) {
            nums[i] = nums[i] or ((nums[nextIdx] and 0b1111111111) shl 10)
        } else {
            nums[i] = nums[i] or (nums[nextIdx] shl 10)
        }
    }
    // before returning, right-shift all entries to remove original values
    for (i in nums.indices) {
        nums[i] = nums[i] shr 10
    }

    return nums
}

fun main() {
    println(buildArray(intArrayOf(0, 2, 1, 5, 3, 4)).joinToString())
    println(buildArray(intArrayOf(5, 0, 1, 2, 3, 4)).joinToString())
    println(buildArrayOptimised(intArrayOf(0, 2, 1, 5, 3, 4)).joinToString())
    println(buildArrayOptimised(intArrayOf(5, 0, 1, 2, 3, 4)).joinToString())
}

main()