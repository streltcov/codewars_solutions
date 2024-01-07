"""

Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form;
For example:
    expanded_form(12) # Should return '10 + 2'
    expanded_form(42) # Should return '40 + 2'
    expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0;

https://www.codewars.com/kata/5842df8ccbd22792a4000245

"""


def expanded_form(num):
    expanded, snum = [], str(num)
    register = len(snum) - 1
    
    for item in snum:
        if item != '0':
            expanded.append(item + "0" * register)
        register -= 1
    
    return " + ".join(expanded)
