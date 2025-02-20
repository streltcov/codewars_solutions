/*
Create a function that gives a personalized greeting. This function takes two parameters: name and owner;

Use conditionals to return the proper message:
case	            return
name equals owner	'Hello boss'
otherwise	        'Hello guest'

https://www.codewars.com/kata/5772da22b89313a4d50012f7

*/

#include <string>

std::string greet(const std::string& name, const std::string& owner) {
  return (name == owner)? "Hello boss" : "Hello guest";
}
