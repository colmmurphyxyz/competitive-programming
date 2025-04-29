fun strStr(haystack: String, needle: String): Int {
    for (i in 0 .. haystack.length - needle.length) {
        if (haystack.substring(i until i+(needle.length)) == needle) {
            return i
        }
    }

    return -1
}

fun main() {
    println(strStr("sadbutsad", "sad"))
    println(strStr("leetcode", "leeto"))
    println(strStr("leetcode", "cod"))
}

main()