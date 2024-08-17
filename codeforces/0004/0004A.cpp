#include <iostream>
#include <string>

int main() {
    std::string input;
    std::getline(std::cin, input);    
    int n = std::stoi(input);
    bool b = n % 2 == 0 && n > 2;
    std::cout << (b ? "YES" : "NO") << std::endl;
    return 0;
}