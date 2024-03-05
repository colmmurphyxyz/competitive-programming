# 1.0 s
# 16 MB

N = int(input())
right = 0
for i in range(N):
    op1, operator, op2, _, expected_result = input().split(" ")
    op1 = int(op1); op2 = int(op2); expected_result = int(expected_result)
    actual_result = 0
    match operator:
        case "+":
            actual_result = op1 + op2
        case "-":
            actual_result = op1 - op2
        case "*":
            actual_result = op1 * op2
        case "//":
            actual_result = op1 // op2
    if actual_result == expected_result:
        right += 1

grade = "F"
percentage = right / N
if percentage > 0.7:
    grade = "A"
elif percentage > 0.6:
    grade = "B"
elif percentage > 0.5:
    grade = "C"
elif percentage > 0.4:
    grade = "D"
elif percentage > 0.3:
    grade = "E"

print(grade)