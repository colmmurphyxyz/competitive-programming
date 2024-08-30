fun convert(s: String, numRows: Int): String {
    if (numRows == 1) return s
    val output = MutableList<String>(numRows) { "" }
    var direction = 1
    var curr = 0
    for (letter in s) {
        output[curr] = output[curr] + letter
        if (curr == output.lastIndex) {
            direction = -1
        } else if (curr == 0) {
            direction = 1
        }
        curr += direction
    }
    return output.joinToString("")
}

fun main() {
    println(convert("PAYPALISHIRING", 3))
}