// 1.0 S
// 256 MB
#include <iostream>
#include <string>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::string outputs[n];
    for (int i = 0; i < n; i++) {
        std::string s;
        std::cin >> s;
        if (s.length() > 10) {
            std::string output = s[0] + std::to_string(s.length() - 2) + s[s.length() - 1];
            outputs[i] = output;
        } else {
            outputs[i] = s;
        }
    }
    for (int i = 0; i < n; i++) {
        std::cout << outputs[i] << std::endl;
    }
    return 0;
}