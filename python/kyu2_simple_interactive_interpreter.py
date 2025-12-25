# -*- coding: utf-8 -*-

"""Simpler Interactive Interpreter;

https://www.codewars.com/kata/53005a7b26d12be55c000243/train/python

Simpler Interactive interpreter (or REPL)
You will create an interpreter which takes inputs described below and produces outputs, storing state in between each
input. This is a simplified version of the Simple Interactive Interpreter kata with functions removed, so if you have
fun with this kata, check out its big brother to add functions into the mix;

If you're not sure where to start with this kata, check out ankr's Evaluate Mathematical Expression kata;

Note that the eval command has been disabled


Concepts

The interpreter will take inputs in the language described under the language header below. This section will give an
overview of the language constructs


Variables

Any identifier which is not a keyword will be treated as a variable. If the identifier is on the left hand side of an
assignment operator, the result of the right hand side will be stored in the variable. If a variable occurs as part of
an expression, the value held in the variable will be substituted when the expression is evaluated;

Variables are implicitly declared the first time they are assigned to;

Example:
    Initializing a variable to a constant value and using the variable in another expression (Each line starting
    with a '>' indicates a separate call to the input method of the interpreter, other lines represent output)

    >x = 7
        7
    >x + 6
        13

Referencing a non-existent variable will cause the interpreter to throw an error. The interpreter should be able to
continue accepting input even after throwing;

Example:
    Referencing a non-existent variable

    >y + 7
        ERROR: Invalid identifier. No variable with name 'y' was found."


Assignments

An assignment is an expression that has an identifier on left side of an = operator, and any expression on the right
Such expressions should store the value of the right hand side in the specified variable and return the result;

Example:
    Assigning a constant to a variable
    x = 7
    7

In this kata, all tests will contain only a single assignment. You do not need to consider chained or nested
assignments


Operator Precedence

Operator precedence will follow the common order. There is a table in the Language section below that explicitly
states the operators and their relative precedence;


Name conflicts

Because variables are declared implicitly, no naming conflicts are possible. variable assignment will always overwrite
any existing value;


Input

Input will conform to the expression production in the grammar below


Output

Output for a valid expression will be the result of the expression
Output for input consisting entirely of whitespace will be an empty string (null in case of Java)

All other cases will throw an error

"""


import re


# V.2;

def is_number(token):
    return re.fullmatch(r"[0-9]*\.?[0-9]+", token) is not None


class RPNConverter:
    """Converts expression to RPN sequence;

    """

    def convert(self, tokens):
        priority = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "%": 2,
        }

        output, operations = [], []
        
        for token in tokens:
            if is_number(token) or token.isidentifier():
                output.append(token)
            elif token in priority:
                while(
                    operations
                    and operations[-1] in priority
                    and priority[operations[-1]] >= priority[token]
                    ):
                    output.append(operations.pop())
                operations.append(token)
            elif token =='(':
                operations.append(token)
            elif token ==')':
                while operations and operations[-1] != '(':
                    output.append(operations.pop())
                if operations and operations[-1] == '(':
                    operations.pop()  # Remove the opening parenthesis
                else:
                    raise Exception("Mismatched parentheses")
        
        while operations:
            if operations[-1] == '(':
                raise Exception("Mismatched parentheses")
            output.append(operations.pop())
        
        return output


class RPNCalculator:
    """Calculates result for RPN expression;

    """
    
    def __init__(self, vars):
        self.vars = vars

    def calculate(self, rpn_expression):
        stack = []
        operators = ('*', '/', '%', '+', '-',)
        
        for token in rpn_expression:
            if is_number(token):
                stack.append(float(token) if '.' in token else int(token))
            elif token.isidentifier():
                stack.append(self.vars[token])
        
            elif token in operators:
                y = stack.pop()
                x = stack.pop()
                
                if token == "+":
                    stack.append(x + y)
                elif token == "-":
                    stack.append(x - y)
                elif token == "*":
                    stack.append(x * y)
                elif token == "/":
                    if y == 0:
                        raise Exception("Division by zero")
                    stack.append(x / y)
                elif token == "%":
                    stack.append(x % y)
                else:
                    raise Exception
        
        if len(stack) != 1:
            raise Exception
        
        return stack[0]


class Interpreter:
    """Simple interactive interpreter;

    """

    def __init__(self):
        self.vars = {}
        self.converter = RPNConverter()
        self.calculator = RPNCalculator(self.vars)
    
    # ------------------------- #
    
    @staticmethod
    def _tokenize(expression):
        if expression == "":
            return []
        
        regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
        tokens = regex.findall(expression)
        return [s for s in tokens if not s.isspace()]
    
    # ------------------------- #
    
    def _handle_assignment(self, tokens):
        name = tokens[0]
        expression_tokens = tokens[2:]
        
        rpn = self.converter.convert(expression_tokens)
        value = self.calculator.calculate(rpn)
        self.vars[name] = value
        
        return value
    
    # ------------------------- #
    
    def input(self, expression):
        try:
            tokens = self._tokenize(expression)
            if not tokens:
                return ""
        except Exception as e:
            return f"Error: {e}"
        
        return self._handle_assignment(tokens=tokens) if '=' in tokens\
         else self.calculator.calculate(self.converter.convert(tokens))


# ******************************************************************************************************************* #


# V.1;

def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    
    return [s for s in tokens if not s.isspace()]


def is_number(token):
    return re.fullmatch(r"[0-9]*\.?[0-9]+", token) is not None


class Interpreter:
    """Simple interactive interpreter;
    
    """

    def __init__(self):
        self.vars = {}
    
    # ------------------------- #

    def input(self, expression):
        try:
            tokens = tokenize(expression)
            if not tokens:
                return ""
        except Exception as e:
            return f"Error: {e}"
        
        if not tokens:
            return ""
        
        return self._handle_assignment(tokens=tokens) if '=' in tokens\
         else self._eval(self._tokens_to_rpn(tokens))
    
    # ------------------------- #
    
    def _handle_assignment(self, tokens):
        name = tokens[0]
        expression_tokens = tokens[2:]
        
        rpn = self._tokens_to_rpn(expression_tokens)
        value = self._eval(rpn)
        self.vars[name] = value
        
        return value
    
    # ------------------------- #
    
    def _tokens_to_rpn(self, tokens):
        priority = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "%": 2,
        }

        output, operations = [], []
        
        for token in tokens:
            if is_number(token) or token.isidentifier():
                output.append(token)
            elif token in priority:
                while(
                    operations
                    and operations[-1] in priority
                    and priority[operations[-1]] >= priority[token]
                    ):
                    output.append(operations.pop())
                operations.append(token)
            elif token =='(':
                operations.append(token)
            elif token ==')':
                while operations and operations[-1] != '=':
                    output.append(operations.pop())
        
        while operations:
            output.append(operations.pop())
        
        return output
    
    # ------------------------- #
    
    def _eval(self, rpn):
        stack = []
        operators = ('*', '/', '%', '+', '-',)
        
        for token in rpn:
            if is_number(token):
                stack.append(float(token) if '.' in token else int(token))
            elif token.isidentifier():
                stack.append(self.vars[token])
        
            elif token in operators:
                y = stack.pop()
                x = stack.pop()
                
                if token == "+":
                    stack.append(x + y)
                elif token == "-":
                    stack.append(x - y)
                elif token == "*":
                    stack.append(x * y)
                elif token == "/":
                    if y == 0:
                        raise Exception("Division by zero")
                    stack.append(x / y)
                elif token == "%":
                    stack.append(x % y)
                else:
                    raise Exception
        
        if len(stack) != 1:
            raise Exception
        
        return stack[0]
