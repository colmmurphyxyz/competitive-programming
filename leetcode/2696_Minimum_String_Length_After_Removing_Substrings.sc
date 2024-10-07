object Solution:
    @annotation.tailrec
    def minLength(s: String): Int =
        val abIdx = s.indexOfSlice("AB", 0)
        val cdIdx = s.indexOfSlice("CD", 0)
        if abIdx >= 0 then
            minLength(s.slice(0, abIdx) ++ s.slice(abIdx + 2, s.length))
        else if cdIdx >= 0 then
            minLength(s.slice(0, cdIdx) ++ s.slice(cdIdx + 2, s.length))
        else
            s.length


println(Solution.minLength("ABFCACDB"))
println(Solution.minLength("CCCCDDDD"))
