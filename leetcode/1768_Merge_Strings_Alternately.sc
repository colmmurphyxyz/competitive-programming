object Solution:
    def mergeAlternately(word1: String, word2: String): String =
        @annotation.tailrec
        def merge(w1: String, w2: String, merged: String = "", useLeft: Boolean = true): String =
            (w1, w2) match {
                case ("", "") => merged
                case (s, "") => merge(s.tail, w2, merged + s.head, useLeft = !useLeft)
                case ("", s) => merge(w1, s.tail, merged + s.head, useLeft = !useLeft)
                case (left, right) => {
                    if useLeft then 
                        merge(w1.tail, w2, merged + w1.head, false)
                    else
                        merge(w1, w2.tail, merged + w2.head, true)
                }
            }
        merge(word1, word2, "", true)

println(Solution.mergeAlternately("abc", "pqr")) // apbqcr
println(Solution.mergeAlternately("ab", "pqrs")) // apbqrs
println(Solution.mergeAlternately("abcd", "pq")) // apb qcd