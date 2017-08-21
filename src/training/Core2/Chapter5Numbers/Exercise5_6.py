def parseExpression(expression):
    operators = ['**', '+', '-', '*', '/', '%']
    operator = '+'
    for currOperator in operators:
        if expression.__contains__(currOperator):
            operator = currOperator
            break
    if bool(operator):
        operands = expression.split(operator)
    return {'firstOperand': int(operands[0]), 'operator': operator, 'secondOperand': int(operands[1])}


def add(firstOperand, secondOperand):
    return firstOperand + secondOperand


def subtract(firstOperand, secondOperand):
    return firstOperand - secondOperand


def multiply(firstOperand, secondOperand):
    return firstOperand * secondOperand


def divide(firstOperand, secondOperand):
    return firstOperand / secondOperand


def mod(firstOperand, secondOperand):
    return firstOperand % secondOperand


def pow(firstOperand, secondOperand):
    return firstOperand ** secondOperand


def calculate(firstOperand, operator, secondOperand):
    operatorMappingFunc = {'+': add, '-': subtract, '*': multiply, '/': divide, '%': mod, '**': pow}
    return operatorMappingFunc[operator](firstOperand, secondOperand)
