fun main() {
    val k = readLine()!!.split(" ")[1].toInt()
    val scores = readLine()!!.split(" ").map { it.toInt() }
    val requiredScore = scores[k - 1]
    val output = scores.count { it >= requiredScore && it > 0 }
    println(output)
}
