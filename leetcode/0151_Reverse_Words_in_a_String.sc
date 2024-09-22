object Solution:
    private def isBlank(s: String): Boolean = 
        s.trim.isEmpty

    def reverseWords(s: String): String =
        s
            .split(" ")
            .filterNot(isBlank(_))
            .reverse
            .mkString(" ")

println(Solution.reverseWords("the sky is blue"))
println(Solution.reverseWords("  hello world     "))
println(Solution.reverseWords("a good    example"))