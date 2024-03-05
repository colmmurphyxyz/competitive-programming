// 1.0 s
// 256 MB
#include <iostream>

int main() {
    int n;
    int x = 0;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::string s;
        std::cin >> s;
        for (int j = 0; j < s.size(); j++) {
            if (s[j] == '+') {
                x++;
                break;
            } else if (s[j] == '-') {
                x--;
                break;
            }
        }
    }
    std::cout << x << std::endl;
    return 0;
}