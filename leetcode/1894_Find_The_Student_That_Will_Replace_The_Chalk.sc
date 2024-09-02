import scala.annotation.tailrec

object Solution {
  def chalkReplacer(chalk: Array[Int], k: Int): Int = {
    @tailrec
    def loop(idx: Int, piecesChalk: Int): Int =
      if (chalk(idx) > piecesChalk) idx
      else loop((idx + 1) % chalk.length, piecesChalk - chalk(idx))

    loop(0, k)
  }
}

println(Solution.chalkReplacer(Array(5, 1, 5), 22))
println(Solution.chalkReplacer(Array(3, 4, 1, 2), 25))
