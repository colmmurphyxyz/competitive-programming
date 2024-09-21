import scala.collection.mutable.Stack

object Solution:
    private def isVowel(c: Character): Boolean =
        Set[Char]('a', 'e', 'i', 'o', 'u', 'A', 'E' ,'I', 'O', 'U').contains(c)


    def reverseVowels(s: String): String =
        val stack: Stack[Char] = Stack[Char]()
            .pushAll(s.filter(isVowel))
        s.map(c => if isVowel(c) then stack.pop() else c)
        

println(Solution.reverseVowels("IceCreAm")) // AceCreIm
println(Solution.reverseVowels("leetcode")) // leotcede