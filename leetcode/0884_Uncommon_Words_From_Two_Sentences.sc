object Solution:
    def uncommonFromSentences(s1: String, s2: String): Array[String] =
        var counter = Map[String, Int]()
        for word <- s1.split(" ") do
            val curr = counter.getOrElse(word, 0)
            counter = counter.updated(word, curr + 1)
        for word <- s2.split(" ") do
            val curr = counter.getOrElse(word, 0)
            counter = counter.updated(word, curr + 1)
        counter.keys.filter(key => counter(key) == 1).toArray