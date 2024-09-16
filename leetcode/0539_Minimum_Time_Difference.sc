import scala.math.min

object Solution:
    def findMinDifference(timePoints: List[String]): Int =
        val times = timePoints.map(timeStr =>
            val components = timeStr.split(":")
            val hours = components(0).toInt
            val minutes = components(1).toInt
            hours * 60 + minutes    
        ).sorted
        val circularDifference = (60 * 24) - times.last + times.head
        val differences = new Array[Int](times.length - 1)
        var i = 0
        while i <= times.length - 2 do
            differences(i) = times(i + 1) - times(i)
            i += 1
        min(circularDifference, differences.min)


println(Solution.findMinDifference(List[String]("23:59","00:00"))) // 1
println(Solution.findMinDifference(List[String]("00:00","23:59","00:00"))) // 0
println(Solution.findMinDifference(List[String]("00:12", "14:14", "15:15", "23:48"))) // 24
println(Solution.findMinDifference(List[String]("00:00", "14:14", "14:24", "23:00"))) // 10