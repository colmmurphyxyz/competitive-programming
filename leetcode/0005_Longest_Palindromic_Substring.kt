import kotlin.math.sign

/**
 * Iterates through all substrings starting with the largest.
 * @return the first palindrome found, guaranteed to be the largest.
 * If no palindromes are found, returns the original string
 */
fun longestPalindrome_naive(s: String): String {
    fun <T> isPalindrome(l: List<T>): Boolean = l == l.reversed()
    var k = s.length
    while (k >= 1) {
        // iterate through all substrings of length k
        // starting with the largest substrings
        // if we find a palindrome, return it
        for (substring in s.asSequence().windowed(k)) {
            if (isPalindrome(substring)) {
                return substring.joinToString("")
            }
        }
        k -= 1
    }

    // s.length == 1 case: return the original string
    return s
}

/** Iterate through each character in the string, and assume it is the center of a palindrome.
 * Expand around the center to find the longest palindrome centered at that position
 * @return The longest palindrome in the string
 */
fun longestPalindrome(s: String): String {
    var start = 0
    var maxPalindrome = s.first().toString()
    for (i in 0 until s.lastIndex) {
        // continuously expand around the center character to find the longest palindrome
        // centered at s[i]
        val longest1 = expandRecursively(s, i, i)
        // expand around center for even-length starting strings
        val longest2 = expandRecursively(s, i, i + 1)
        val longest = arrayOf(longest1, longest2).maxBy(String::length)
        if (longest.length > maxPalindrome.length) {
            maxPalindrome = longest
        }
    }

    return maxPalindrome
}

fun expandAroundCenter(s: String, left: Int, right: Int): Int {
    var l = left
    var r = right
    while (l >= 0 && r < s.length && s[l] == s[r]) {
        l--
        r++
    }

    return r - l - 1
}

fun expandRecursively(s: String, left: Int, right: Int): String {
    if (left <= 0 || right >= s.lastIndex) {
        return s.substring(left..right)
    }
    if (s[left - 1] == s[right + 1]) {
        return expandRecursively(s, left - 1, right + 1)
    }
    return s.substring(left..right)
}

fun main() {
    println(longestPalindrome("babad")) // bab
    println(longestPalindrome("cbbd")) // bb
    println(longestPalindrome("zz")) // zz
    println(longestPalindrome("z")) // z
    println(longestPalindrome("ac")) // a
    println(longestPalindrome("gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv"))
}