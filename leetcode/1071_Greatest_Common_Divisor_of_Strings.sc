implicit class StringMult(s: String):
    def *(n: Int): String =
        @annotation.tailrec
        def aux(acc: String, k: Int): String =
            k match {
                case _ if k <= 0 => acc
                case x if k > 0 => aux(acc + s, x - 1)
            }
        aux("", n)

object Solution:
    private def divides(s: String, t: String): Boolean =
        if t == "" then return true
        val factor: Int = s.length / t.length
        t * factor == s

    private def longestCommonPrefix(strs: Array[String]): String =
        @annotation.tailrec
        def aux(strings: Array[String], prefixLength: Int, maxPrefixLength: Int): String =
            if prefixLength >= maxPrefixLength then return strings(0).slice(0, prefixLength)
            val prefixes = strings.map(_.slice(0, prefixLength + 1))

            if prefixes.forall(_ == prefixes(0)) then
                aux(strings, prefixLength + 1, maxPrefixLength)
            else
                strings(0).slice(0, prefixLength)
        aux(strs, 0, strs.minBy(_.length).length)

        
    def gcdOfStrings(str1: String, str2: String): String =
        val longestPrefix = longestCommonPrefix(Array[String](str1, str2))
        @annotation.tailrec
        def getLongestCommonDivisor(str1: String, str2: String, prefix: String): String =
            if divides(str1, prefix) && divides(str2, prefix) then
                return prefix
            getLongestCommonDivisor(str1, str2, prefix.slice(0, prefix.length - 1))
        getLongestCommonDivisor(str1, str2, longestPrefix)

