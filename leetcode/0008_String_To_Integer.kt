import java.math.BigInteger

fun myAtoi(s: String): Int {
    var a = s.trimStart()
//    var n: Long = 0
    var n: BigInteger = BigInteger.ZERO
    // get sign of ascii number
    val isNegative: Boolean
    if (a.isNotEmpty() && a.first() == '-') {
        isNegative = true
        a = a.removePrefix("-")
    } else if (a.isNotEmpty() && a.first() == '+') {
        isNegative = false
        a = a.removePrefix("+")
    } else {
        isNegative = false
    }

    // ignore leading zeros
    while (a.isNotEmpty() && a.first() == '0') {
        a = a.removePrefix("0")
    }

    while (a.isNotEmpty() && a.first().isDigit()) {
        val c = a.first()
        n *= BigInteger.valueOf(10)
        n += BigInteger.valueOf(c.digitToInt().toLong())
        a = a.removePrefix(c.toString())
    }

    val result = if (isNegative) n.negate() else n

    if (result < BigInteger.valueOf(Int.MIN_VALUE.toLong())) {
        return Int.MIN_VALUE
    } else if (result > BigInteger.valueOf(Int.MAX_VALUE.toLong())) {
        return Int.MAX_VALUE
    }

    return result.intValueExact()
}

fun main() {
    println(myAtoi("42"))
    println(myAtoi("-42"))
    println(myAtoi("-042"))
    println(myAtoi("1337c0d3"))
    println(myAtoi("0-1"))
    println(myAtoi("words and 987"))
    println(myAtoi("-91283472332"))
    println(myAtoi("9223372036854775808"))
}