#include <iostream>

int Sum(int first, int second) {
    return first + second;
}

int main() {
    int first = 0;
    int second = 0;
    std::cin >> first >> second;
    std::cout << Sum(first, second) << std::endl;
}