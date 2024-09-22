object Solution:
    def productExceptSelf(nums: Array[Int]): Array[Int] =
        val prefixProduct = nums.scan(1)((a, b) => a * b).drop(1)
        val suffixProduct = nums.scanRight(1)((a, b) => a * b).dropRight(1)
        
        Range(0, nums.length).map(idx =>
            val p = if idx <= 0 then 1 else prefixProduct(idx - 1)
            val s = if idx >= nums.length - 1 then 1 else suffixProduct(idx + 1)
            p * s
        ).toArray

println(Solution.productExceptSelf(Array[Int](1, 2, 3, 4)).mkString(" ")) // [24, 12, 8, 6]
println(Solution.productExceptSelf(Array[Int](-1, 1, 0, -3, 3)).mkString(" ")) // [0, 0, 9, 0, 0]