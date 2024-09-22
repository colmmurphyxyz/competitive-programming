import scala.collection.immutable.Set

object Solution:
    type Board = Array[Array[Char]]

    private def getRow(board: Board, rowIdx: Int): Array[Char] = 
        board(rowIdx)


    private def getCol(board: Board, colIdx: Int): Array[Char] =
        board.map(row => row(colIdx))


    private def getSubBox(board: Board, rowIdx: Int, colIdx: Int): Array[Array[Char]] =
        val r = 3 * (rowIdx / 3)
        val c = 3 * (colIdx / 3)
        Array[Array[Char]](
            Array[Char](board(r)(c),     board(r)(c + 1),     board(r)(c + 2)),
            Array[Char](board(r + 1)(c), board(r + 1)(c + 1), board(r + 1)(c + 2)),
            Array[Char](board(r + 2)(c), board(r + 2)(c + 1), board(r + 2)(c + 2))
        )

    private def containsDuplicate[T](arr: Iterable[T]): Boolean =
        @annotation.tailrec
        def f[T](visited: Set[T], xs: Iterable[T]): Boolean =
            if xs.isEmpty then
                false
            else if visited.contains(xs.head) then
                true
            else
                f(visited.incl(xs.head), xs.tail)
        f(Set[T](), arr)


    def isValidSudoku(board: Array[Array[Char]]): Boolean =

        if !Range(0, 9).map(getRow(board, _).filter(_ != '.')).forall(!containsDuplicate(_)) then
            return false

        if !Range(0, 9).map(getCol(board, _).filter(_ != '.')).forall(!containsDuplicate(_)) then
            return false

        var subBoxesValid = true
        for rowIdx <- Range(0, 9, 3) do
            for colIdx <- Range(0, 9, 3) do
                val subBox = getSubBox(board, rowIdx, colIdx).flatten.filter(_ != '.')
                if containsDuplicate(subBox) then
                    subBoxesValid = false

        return subBoxesValid

val validBoardString = """
    5 3 . . 7 . . . .
    6 . . 1 9 5 . . .
    . 9 8 . . . . 6 .
    8 . . . 6 . . . 3
    4 . . 8 . 3 . . 1
    7 . . . 2 . . . 6
    . 6 . . . . 2 8 .
    . . . 4 1 9 . . 5
    . . . . 8 . . 7 9
""".trim()

val invalidBoardString = """
    8 3 . . 7 . . . .
    6 . . 1 9 5 . . .
    . 9 8 . . . . 6 .
    8 . . . 6 . . . 3
    4 . . 8 . 3 . . 1
    7 . . . 2 . . . 6
    . 6 . . . . 2 8 .
    . . . 4 1 9 . . 5
    . . . . 8 . . 7 9
""".trim()

val boardString = """
    . . . . 5 . . 1 .
    . 4 . 3 . . . . .
    . . . . . 3 . . 1
    8 . . . . . . 2 .
    . . 2 . 7 . . . .
    . 1 5 . . . . . .
    . . . . . 2 . . .
    . 2 . 9 . . . . .
    . . 4 . . . . . .
""".trim()

def boardFromString(s: String): Array[Array[Char]] =
    s
        .filter(c => c != ' ')
        .split("\n")
        .map(_.toCharArray())

def printMatrix[T](matrix: Array[Array[T]]): Unit =
    matrix.foreach(row =>
        print("[ ")
        row.foreach(value => print(value.toString + " "))
        print("]\n")
    )

println(Solution.isValidSudoku(boardFromString(validBoardString))) // true
println(Solution.isValidSudoku(boardFromString(invalidBoardString))) // false
println(Solution.isValidSudoku(boardFromString(boardString))) // false