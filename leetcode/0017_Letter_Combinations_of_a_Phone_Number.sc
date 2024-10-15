import scala.collection.immutable.Map

object Solution:
    def letterCombinations(digits: String): List[String] =
        if digits.isEmpty then return List[String]()

        val digitToChars: Map[Char, List[Char]] = Map(
            ('2', List[Char]('a', 'b', 'c')),
            ('3', List[Char]('d', 'e', 'f')),
            ('4', List[Char]('g', 'h', 'i')),
            ('5', List[Char]('j', 'k', 'l')),
            ('6', List[Char]('m', 'n', 'o')),
            ('7', List[Char]('p', 'q', 'r', 's')),
            ('8', List[Char]('t', 'u', 'v')),
            ('9', List[Char]('w', 'x', 'y', 'z')),
        )

        def permutations(currentPerms: List[String], remainingDigits: String): List[String] =
            if remainingDigits.isEmpty then
                currentPerms
            else
                val possibilities = digitToChars(remainingDigits.head)
                val newPerms = currentPerms.flatMap( x =>
                    possibilities.map(y => x + y)    
                )
                permutations(newPerms, remainingDigits.tail)
        val initial = digitToChars(digits.head).map(_.toString)
        permutations(initial, digits.tail)

println(Solution.letterCombinations("23"))
println(Solution.letterCombinations("2"))
println(Solution.letterCombinations(""))