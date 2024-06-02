/**
Write a function that reverses a string. The input string is given as an array of characters `s`.
You must do this by modifying the input array in-place with O(1) extra memory.
 */
class Solution {
    fun reverseString(s: CharArray): Unit {
        var left: Int = 0
        var right: Int = s.size - 1

        
        while (left <= right) {
            val temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left++
            right--
        }
        println(s)
    }
}

fun main() {
    val sol = Solution()
    sol.reverseString(charArrayOf('h', 'e', 'l', 'l', 'o'))
    sol.reverseString(charArrayOf('H', 'a', 'n', 'n', 'a', 'h'))
}