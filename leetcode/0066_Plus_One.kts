fun plusOne(digits: IntArray): IntArray {
    var sum = digits.last() + 1

    var carry = sum >= 10

    digits[digits.lastIndex] = sum % 10

    var i = digits.lastIndex - 1
    while (i >= 0 && carry) {
        sum = digits[i] + 1 // `carry` is always true in loop body
        digits[i] = sum % 10
        carry = sum >= 10
        i -= 1
    }

    return when(carry) {
        false -> digits
        true -> intArrayOf(1, *digits)
    }
}

fun main() {
    println(plusOne(intArrayOf(1, 2, 3)).joinToString())
    println(plusOne(intArrayOf(4, 3, 2, 1)).joinToString())
    println(plusOne(intArrayOf(9)).joinToString())
    println(plusOne(intArrayOf(9, 9, 9)).joinToString())
}

main()