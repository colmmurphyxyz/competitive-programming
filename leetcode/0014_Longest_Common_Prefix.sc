object Solution:
    def longestCommonPrefix(strs: Array[String]): String =
        @annotation.tailrec
        def longestCommonPrefixLength(words: Array[String], prefixLength: Int): Int =
            if words.count(word => prefixLength >= word.length) > 0 then
                return prefixLength
            val chars = words.map(word => word(prefixLength))
            if chars.forall(c => c == chars.head) then
                longestCommonPrefixLength(words, prefixLength + 1)
            else 
                prefixLength
        strs.head.slice(0, longestCommonPrefixLength(strs, 0))

println(Solution.longestCommonPrefix(Array[String]("flower","flow","flight"))) // "fl"
println(Solution.longestCommonPrefix(Array[String]("dog","racecar","car"))) // ""