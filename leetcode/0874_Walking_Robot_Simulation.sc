import scala.annotation.tailrec
import scala.math.{abs, max}
import scala.collection.immutable.Set

implicit class TupleAdd(t: (Int, Int)) {
  def +(p: (Int, Int)) = (p._1 + t._1, p._2 + t._2)
}

object Solution {

  private def square(a: Int): Int = a * a

  private def distanceSquaredFromOrigin(a: (Int, Int)): Int = {
    square(a._1) + square(a._2)
  }

  private def turnLeft(currentDirection: (Int, Int)): (Int, Int) = currentDirection match {
    case (0, 1) => (-1, 0)
    case (1, 0) => (0, 1)
    case (0, -1) => (1, 0)
    case (-1, 0) => (0, -1)
  }

  private def turnRight(currentDirection: (Int, Int)): (Int, Int) = currentDirection match {
    case (0, 1) => (1, 0)
    case (1, 0) => (0, -1)
    case (0, -1) => (-1, 0)
    case (-1, 0) => (0, 1)
  }

  @tailrec
  private def move(curr: (Int, Int), direction: (Int, Int), obstacles: Set[(Int, Int)], distance: Int): (Int, Int) = {
    if (distance == 0) {
      return curr
    }
    val nextSquare = curr + direction
    if (obstacles.contains(nextSquare)) {
      return curr
    }
    move(nextSquare, direction, obstacles, distance - 1)
  }

  def robotSim(commands: Array[Int], obstacles: Array[Array[Int]]): Int = {
    val obst: Set[(Int, Int)] = obstacles.map(arr => (arr(0), arr(1))).toSet
    var robotLocation: (Int, Int) = (0, 0)
    var maxDistance: Int = 0
    var direction = (0, 1)
    // cache turn commands to perform lazily when we receive a move command
    // this allows command sequences such as [turnLeft, turnLeft, turnRight, move 4]
    // to be reduced to [turnLeft, move 4]
    // directionCache = -n implies we should turn left n times
    // positive values indicate we should turn right
    var turnCache: Int = 0
    for (command <- commands) {
      command match {
        case -1 => turnCache += 1
        case -2 => turnCache -= 1
        case n if n > 0 => {
          if (turnCache < 0) {
            for (_ <- 1 to abs(turnCache) % 4) {
              direction = turnLeft(direction)
            }
          } else if (turnCache > 0) {
            for (_ <- 1 to turnCache % 4) {
              direction = turnRight(direction)
            }
          }
          turnCache = 0
          robotLocation = move(robotLocation, direction, obst, n)
          maxDistance = max(maxDistance, distanceSquaredFromOrigin(robotLocation))
        }
      }
    }
    maxDistance
  }
}

println( // 25
  Solution.robotSim(
    Array[Int](4, -1, 3),
    Array[Array[Int]]()
  )
)
println( // 65
  Solution.robotSim(
    Array[Int](4,-1,4,-2,4),
    Array[Array[Int]](
      Array[Int](2, 4)
    )
  )
) // 65
println( // 36
  Solution.robotSim(
    Array[Int](6, -1, -1, 6),
    Array[Array[Int]]()
  )
)
