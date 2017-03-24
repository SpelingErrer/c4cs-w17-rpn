#!/usr/bin/env python3
import math
import readline
from termcolor import colored


def add(arg1, arg2):
	return arg1 + arg2

def subtract(arg1, arg2):
	return arg1 - arg2

def powerOf(arg1, arg2):
	return math.pow(arg1, arg2)

def multiply(arg1, arg2):
	return arg1 * arg2

def divide(arg1, arg2):
	return arg1 / arg2

OPERATORS = {
	'+': add,
	'-': subtract,
	'^': powerOf,
}


def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			#print colored(arg1, 'red'), colored(operand, 'green'), colored(arg2, 'red'), colored('=:', 'green')
			result = operator_fn(arg1, arg2)

			stack.append(result)

	return stack.pop()

def main():
	while True:
		result = calculate(input("rpn calc> "))
		print(result)

if __name__ == '__main__':
	main()
