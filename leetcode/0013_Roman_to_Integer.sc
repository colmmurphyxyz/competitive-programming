import scala.collection.immutable.Map
import scala.math.{log10, pow, floor}

object Solution:
    private def orderOfMagnitude(n: Int): Int =
        val exp = floor(log10(n.toDouble))
        pow(10.0, exp).toInt

    def romanToInt(s: String): Int =
        val values: Map[Char, Int] = Map(
          'I' -> 1,
          'V' -> 5,
          'X' -> 10,
          'L' -> 50,
          'C' -> 100,
          'D' -> 500,
          'M' -> 1000
        )
        def f(subtotal: Int, prev: Option[Char] = None, tail: String): Int =
            if tail.isEmpty() then return subtotal
            val currValue = values(tail.head)
            val prevValue =
                if prev.isDefined then values(prev.get) else Int.MaxValue
            val newSubtotal =
                if prevValue >= currValue
                then subtotal + currValue
                else subtotal + currValue - (2 * orderOfMagnitude(prevValue))
            f(newSubtotal, Option(tail.head), tail.tail)
        f(0, None, s)

println(Solution.romanToInt("III"))     // 3
println(Solution.romanToInt("LVIII"))   // 58
println(Solution.romanToInt("MDCLXVI")) // 1666
println(Solution.romanToInt("MCMXCIV")) //1994
println(Solution.romanToInt("IX")) // 4
