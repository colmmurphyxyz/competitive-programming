import java.util.HashSet

fun findDifference(nums1: IntArray, nums2: IntArray): List<List<Int>> {
    val set1 = nums1.toSet()
    val set2 = nums2.toSet()

    return listOf(
        (set1 subtract set2).toList(),
        (set2 subtract set1).toList()
    )
}

fun main() {
    println(findDifference(intArrayOf(1, 2, 3), intArrayOf(2, 4, 6)))
    println(findDifference(intArrayOf(1, 2, 3, 3), intArrayOf(1, 1, 2, 2)))
}