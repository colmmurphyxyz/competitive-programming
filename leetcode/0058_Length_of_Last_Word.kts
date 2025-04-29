fun lengthOfLastWord(s: String): Int = s.split("\\s+".toRegex()).dropLastWhile(String::isEmpty).last().length

fun main() {
    println(lengthOfLastWord("Hello World"))
    println(lengthOfLastWord("   fly me   to   the moon  "))
    println(lengthOfLastWord("luffy is still joyboy"))
}

main()