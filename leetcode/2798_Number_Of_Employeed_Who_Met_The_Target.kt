fun numberOfEmployeesWhoMetTarget(hours: IntArray, target: Int): Int =
    hours.count { it >= target}