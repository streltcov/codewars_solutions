/*
Your task is to sum the differences between consecutive pairs in the array in descending order;

Example
    [2, 1, 10]  -->  9
    In descending order: [10, 2, 1]
    Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9

If the array is empty or the array has only one element the result should be 0 (Nothing in Haskell, None in Rust;

https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e

*/

#include <iostream>
#include <vector>
#include <algorithm>

int sumOfDifferences(const std::vector<int>& arr){
  if (arr.size() == 0) {
    return 0;
  };

  int sum = 0;
  std::vector<int> sorted = arr;
  std::sort(sorted.begin(), sorted.end(), std::greater<int>());

  for (std::size_t i = 0; i < sorted.size() - 1; ++i) {
    sum += sorted[i] - sorted[i + 1];
  };

  return sum;
}
