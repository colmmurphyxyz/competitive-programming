object Solution {
  def chalkReplacer(chalk: Array[Int], k: Int): Int = {
    var piecesChalk: Int = k
    var idx: Int = 0
    while(true) {
      if (chalk(idx) > piecesChalk) {
        return idx
      }
      piecesChalk -= chalk(idx)
      idx = (idx + 1) % chalk.length
    }
    return 0 // unreachable
  }
}

println(Solution.chalkReplacer(Array(5, 1, 5), 22))
println(Solution.chalkReplacer(Array(3, 4, 1, 2), 25))
