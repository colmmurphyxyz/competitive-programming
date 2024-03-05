#include <iostream>

int getTotalSetBits(int b) {
    int count = 0;
    while (b) {
        count += b & 1;
        b >>= 1;
    }
    return count;

}

int main() {
    int n;
    std::cin >> n;
    int output = 0;
    for (int i = 0; i < n; i++) {
        int p, q, r;
        std::cin >> p >> q >> r;
        int subtotal = (p << 2) + (q << 1) + (r);
        if (getTotalSetBits(subtotal) >= 2) {
            output++;
        }
    }
    std::cout << output << std::endl;
}