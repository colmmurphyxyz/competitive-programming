object Solution:
    def countConsistentStrings(allowed: String, words: Array[String]): Int =
        val allowedCharacters: Set[Char] = allowed.toSet
        words.count(word =>
            word.forall(letter =>
                allowed.contains(letter)    
            )    
        )

println(Solution.countConsistentStrings("ab", Array[String]("ad", "bd", "aab", "baa", "badab"))) // 2
println(Solution.countConsistentStrings("abc", Array[String]("a","b","c","ab","ac","bc","abc"))) // 7