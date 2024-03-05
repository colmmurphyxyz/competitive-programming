#include <iostream>
#include <string>

int main() {
    int N;
    std::cin >> N;
    int right = 0;
    for (int i = 0; i < N; i++) {
        int op1, op2, expectedResult;
        std::string equals;
        std::string operation;
        std::cin >> op1 >> operation >> op2 >> equals >> expectedResult;
        int actualResult;
        switch (operation[0]) {
            case '+':
                actualResult = op1 + op2;
                break;
            case '-':
                actualResult = op1 - op2;
                break;
            case '*':  
                actualResult = op1 * op2;
                break;
            case '/':
                actualResult = op1 / op2;
                break;
        }
        if (actualResult == expectedResult) {
            right++;
        }
    }
    int percentage = (right * 100) / N;
    char grade = 'F';
    if (percentage > 70) {
        grade = 'A';
    } else if (percentage > 60) {
        grade = 'B';
    } else if (percentage > 50) {
        grade = 'C';
    } else if (percentage > 40) {
        grade = 'D';
    } else if (percentage > 30) {
        grade = 'E';
    }
    std::cout << grade << std::endl;
    return 0;
}