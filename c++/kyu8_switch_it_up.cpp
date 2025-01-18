/*
When provided with a number between 0-9, return it in words. Note that the input is guaranteed to be within the range of 0-9.

Input: 1

Output: "One";

If your language supports it, try using a switch statement

https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/

*/

#include <string>

std::string switch_it_up(int number){
    std::string number_name;

    switch (number) {
        case 0:
            number_name = "Zero";
            break;
        case 1:
            number_name = "One";
            break;
        case 2:
            number_name = "Two";
            break;
        case 3:
            number_name = "Three";
            break;
        case 4:
            number_name = "Four";
            break;
        case 5:
            number_name = "Five";
            break;
        case 6:
            number_name = "Six";
            break;
        case 7:
            number_name = "Seven";
            break;
        case 8:
            number_name = "Eight";
            break;
        case 9:
            number_name = "Nine";
            break;
    };
