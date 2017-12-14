#!/usr/bin/env python3
import sys
import calculate
from math import *

operation = input("Operation: ")

calc = calculate.Calculate();
result = calc.execute(operation)
print(result)