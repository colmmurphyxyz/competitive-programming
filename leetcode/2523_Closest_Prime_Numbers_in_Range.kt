import kotlin.math.abs
import kotlin.math.sqrt

fun getPrimes(limit: Int): BooleanArray {
    val a = BooleanArray(limit + 1) { true }
    a[1] = false
    for (i in 2 .. sqrt(limit.toDouble()).toInt()) {
        if (a[i]) {
            var j = i * i
            while (j <= limit) {
                a[j] = false
                j += i
            }
        }
    }
    return a
}

fun closestPrimes(left: Int, right: Int): IntArray {
    val sieve = getPrimes(right)
    val primes = (left .. right).filter { sieve[it] }

    if (primes.size < 2) {
        return intArrayOf(-1, -1)
    }
//    println("primes ${primes.joinToString()}")
    var closest: Pair<Int, Int> = primes[0] to primes[1]
    var minDiff = primes[1] - primes[0]
    for (i in 1 until primes.lastIndex) {
        if (abs(primes[i + 1] - primes[i]) < minDiff) {
//            println("Updating closest to ${primes[i]}, ${primes[i + 1]}")
            minDiff = primes[i + 1] - primes[i]
            closest = primes[i] to primes[i + 1]
            if (minDiff <= 2) break
        }
    }
    if (closest.second < closest.first) {
        return intArrayOf(closest.second, closest.first)
    }
    return intArrayOf(closest.first, closest.second)
}

fun main() {
    println(getPrimes(100))
    println(closestPrimes(10, 19).joinToString())
    println(closestPrimes(4, 6).joinToString())
    println(closestPrimes(84084, 407043).joinToString())
    println(closestPrimes(628853, 801856).joinToString()) // [628937,628939]
    println(closestPrimes(1000000, 1000000).joinToString())
    println(closestPrimes(1, 1000000).joinToString())
}
