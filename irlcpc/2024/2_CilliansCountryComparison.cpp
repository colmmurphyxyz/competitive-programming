#include <iostream>
#include <map>
#include <string>
#include <vector>

void bubbleSort(std::vector<std::pair<int, int>> &arr) {
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr.size() - i - 1; j++) {
            if (arr[j].second < arr[j + 1].second) {
                std::pair<int, int> temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    std::map<int, std::string> countries;
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::string country;
        int number;
        std::cin >> country >> number;
        countries[number] = country;
    }
    std::map<int, int> occurences;
    int h, w;
    std::cin >> h >> w;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            int num;
            std::cin >> num;
            occurences[num]++;
        }
    }
    // get a list of all key-value pairs in occurences
    std::vector<std::pair<int, int>> pairs;
    for (auto it = occurences.begin(); it != occurences.end(); it++) {
        pairs.push_back(*it);
    }

    bubbleSort(pairs);

    for (int i = 0; i < 3; i++) {
        std::cout << countries[pairs[i].first] << std::endl;
    }

    return 0;
}