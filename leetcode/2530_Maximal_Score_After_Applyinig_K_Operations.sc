import scala.collection.mutable.PriorityQueue
import scala.math.ceil

object Solution:
    def maxKelements(nums: Array[Int], k: Int): Long =
        val pq = PriorityQueue(nums*)

        @annotation.tailrec
        def f(currScore: Long, remainingOps: Int): Long =
            if remainingOps <= 0 || pq.isEmpty then
                currScore
            else
                val popped = pq.dequeue
                val newElem = ceil(popped / 3.0).toInt
                pq.addOne(newElem)
                f(currScore + popped, remainingOps - 1)

        f(0L, k)
            


println(Solution.maxKelements(Array[Int](1, 10, 3, 3, 3), 3)) // 17
println(Solution.maxKelements(Array[Int](10, 10, 10, 10, 10), 5)) // 50
println(Solution.maxKelements(Array[Int](10, 10, 10, 10), 5)) // 40