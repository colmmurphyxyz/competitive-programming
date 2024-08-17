import java.util.*
import kotlin.math.abs
import kotlin.math.max

// m == arrays.size
// 2 <= m <= 10^5
// 1 <= arrays[i].size <= 500
// -10^4 <= arrays[i][j] <= 10^4
// arrays[i] sorted in ascending order

fun maxDistance(arrays: List<List<Int>>): Int {
    val indexMin = arrays.indices.minBy { arrays[it].first() }
    val indexMax = arrays.indices.maxBy { arrays[it].last() }
    if (indexMin != indexMax) {
        return arrays[indexMax].last() - arrays[indexMin].first()
    }

    val indexMin2 = arrays
        .indices
        .asSequence()
        .filter { it != indexMin }
        .minBy { arrays[it].first() }
    val indexMax2 = arrays
        .indices
        .asSequence()
        .filter { it != indexMax }
        .maxBy { arrays[it].last() }

    return max(
        arrays[indexMax].last() - arrays[indexMin2].first(),
        arrays[indexMax2].last() - arrays[indexMin].first()
    )
}

fun main() {
    println(maxDistance(listOf(
        listOf(1, 2, 3),
        listOf(4, 5),
        listOf(1, 2, 3)
    ))) // 4

    println(maxDistance(listOf(
        listOf(1),
        listOf(1)
    ))) // 0
}