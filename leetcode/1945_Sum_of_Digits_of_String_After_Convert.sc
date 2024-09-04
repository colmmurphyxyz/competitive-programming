import scala.math.{floor, log10}

object Solution {

  private def toDigitArray(num: Int): Array[Int] = {
    val numDigits: Int = floor(log10(num)).toInt + 1
    val digits = new Array[Int](numDigits)
    var idx = numDigits - 1
    var curr: Int = num
    while (idx >= 0) {
      digits(idx) = curr % 10
      curr /= 10
      idx -= 1
    }
    digits
  }

  def getLucky(s: String, k: Int): Int = {
    val digits = s.map(a => a.toInt - 96).toArray.map(toDigitArray)
    var res = digits.flatten.sum
    for (_ <- 0 until (k - 1)) {
      res = toDigitArray(res).sum
    }
    res
  }
}

println(Solution.getLucky("zbax", 2)) // 8
println(Solution.getLucky("iiii", 1)) // 36
println(Solution.getLucky("leetcode", 2)) // 6
println(Solution.getLucky("dbvmfhnttvr", 5)) // 5