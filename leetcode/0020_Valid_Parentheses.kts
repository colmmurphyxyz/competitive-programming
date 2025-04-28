import java.util.*

fun isMatchingPair(open: Char, close: Char): Boolean {
    return (open == '(' && close == ')') ||
           (open == '{' && close == '}') ||
           (open == '[' && close == ']')
}

fun isValid(s: String): Boolean {
    val stack = Stack<Char>()
    for (c in s) {
        when (c) {
            '(', '{', '[' -> stack.push(c)
            ')', '}', ']' -> {
                if (stack.isEmpty()) return false
                val top = stack.pop()
                if (!isMatchingPair(top, c)) return false
            }
        }
    }
    return stack.isEmpty()
}

fun main() {
    println(isValid("()"))
    println(isValid("()[]{}"))
    println(isValid("(]"))
    println(isValid("([])"))
}

main()