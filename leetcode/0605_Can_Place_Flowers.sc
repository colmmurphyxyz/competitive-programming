object Solution:
    def canPlaceFlowers(flowerbed: Array[Int], n: Int): Boolean =
        // handle flowerbed.length <= 2
        if flowerbed.length == 1 then
            return flowerbed.count(_ == 0) >= n
        else if flowerbed.length == 2 then
            return flowerbed.count(_ == 0) match {
                case 0 => n <= 0
                case 1 => n <= 0
                case 2 => n <= 1
            }

        var flowersPlaced = 0
        // try to place a flowerbed in the first position
        if flowerbed(0) + flowerbed(1) == 0 then
            flowersPlaced += 1
            flowerbed(0) = 1
        for i <- 0 until flowerbed.length - 3 do
            if flowerbed(i) + flowerbed(i + 1) + flowerbed(i + 2) == 0 then
                flowerbed(i + 1) = 1
                flowersPlaced += 1
        // try to place a flower in the last position
        if flowerbed(flowerbed.length - 2) + flowerbed(flowerbed.length - 1) == 0 then
            flowersPlaced += 1
        flowersPlaced >= n

println(Solution.canPlaceFlowers(Array[Int](1, 0, 0, 0, 1), 1)) // true
println(Solution.canPlaceFlowers(Array[Int](1, 0, 0, 0, 1), 2)) // false
println(Solution.canPlaceFlowers(Array[Int](1), 1)) // false
println(Solution.canPlaceFlowers(Array[Int](0), 1)) // true
println(Solution.canPlaceFlowers(Array[Int](0, 0), 1)) // true
println(Solution.canPlaceFlowers(Array[Int](1, 0), 1)) // false
println(Solution.canPlaceFlowers(Array[Int](1,0,1,0,0,1,0), 1)) // false
