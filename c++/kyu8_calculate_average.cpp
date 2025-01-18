/*
Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0;

https://www.codewars.com/kata/57a2013acf1fa5bfc4000921

*/

#include <vector>

double calcAverage(const std::vector<int>& values){
    if (values.empty()) {
        return 0;
    }

    int sum = 0;
    double average = 0.0;

    for (int value : values) {
        sum += value;
    }

    average = static_cast<double>(sum) / values.size();

    return average;
}
