fun applyOperations(nums: IntArray): IntArray {
    for (i in 0 until nums.size - 1) {
        if (nums[i] == nums[i + 1]) {
            nums[i] *= 2
            nums[i + 1] = 0
        }
    }
    val ret = IntArray(nums.size) { 0 }
    var i = 0
    for (j in nums) {
        if (j != 0) {
            ret[i] = j
            i += 1
        }
    }
    return ret
}

println(applyOperations(intArrayOf(1, 2, 2, 1, 1, 0)).joinToString())
println(applyOperations(intArrayOf(0, 1)).joinToString())