/*
If you can't sleep, just count sheeps!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input
will always be valid, i.e. no negative integers;

https://www.codewars.com/kata/5b077ebdaf15be5c7f000077

*/

#include <string>

std::string countSheep(int number) {
    std::string murmur = "";
    if (number == 0) {
        return murmur;
    }
    for (int i = 1; i <= number; ++i) {
        murmur += std::to_string(i) + " sheep...";
    }

    return murmur;
}
