object Solution:

    def largestNumber(nums: Array[Int]): String =
        def lt(a: String, b: String): Boolean =
            a + b > b + a
        val sorted = nums.map(_.toString).sortWith(lt)
        val answer = sorted
            .fold("")((a, b) => a + b)
            .dropWhile((c => c == '0'))
        if answer == "" then "0" else answer

println(Solution.largestNumber(Array[Int](10, 2)))
println(Solution.largestNumber(Array[Int](3, 30, 34, 5, 9)))
