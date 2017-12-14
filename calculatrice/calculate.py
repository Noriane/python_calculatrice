#!/usr/bin/env python3
import sys
from math import *

class Calculate():
	result = []
	tab = []
	result2 = []
	count = 0;
	_param = ""

	def __init__(self):
		pass

	def execute(self, operation)->float:
		start_str = False

		for char in operation:
			if char == " ":
				continue
			if char.isdigit() or (char == '.'):
				self._param += char

			else:
				if self._param != "":
					self.result.append(self.convertToNumber(self._param))
					self._param = ""
				if start_str and not char.isalpha():
					last = self.tab.pop();
					last.append(''.join(self.result))
					start_str = False
					self.result = last

				if char != ')' and char != '(' and char.isalpha() == False:
					self.result.append(char)

				if char.isalpha() and start_str == False:
					if not start_str:
						self.tab.append(self.result)
						start_str = True
						self.result = []
						self.result.append(char)

				elif char.isalpha() and start_str == True:
					self.result.append(char)

				if char == '(':
					self.tab.append(self.result)
					self.result = []

				elif char == ')':
					parent_tab = self.tab.pop()
					parent_tab.append(self.result)
					self.result = parent_tab

		if self._param != "":
			self.result.append(self.convertToNumber(self._param))
			self._param = ""

		calcul = self.calcule(self.result)
		return calcul[0]


	def convertToNumber(self, _param):
		if _param.count('.') == 1:
			return float(_param)
		else:
			return int(_param)

	def calcule(self, array):

		i = 0
		while i < len(array):
			val = array[i]
			if isinstance(val, list):
				new_arr = self.calcule(val)
				array[i] = new_arr[0]
			i += 1

		i = 0
		while i < len(array):
			val = array[i]
			if str(val) == "sqrt":
				test = array[i+1]
				array[i] = sqrt(test)
				del array[i+1]
			elif str(val) == "cos":
				test = array[i+1]
				array[i] = cos(test)
				del array[i+1]
			elif str(val) == "tan":
				test = array[i+1]
				array[i] = tan(test)
				del array[i+1]
			elif str(val) == "sin":
				test = array[i+1]
				array[i] = sin(test)
				del array[i+1]
			i += 1

		i = 0
		while i < len(array):
			val = array[i]
			if val == '%':
				array[i-1] = array[i-1] % array[i+1]
				del array[i]
				del array[i]
				i -=1
			elif val == '*':
				array[i-1] = array[i-1] * array[i+1]
				del array[i]
				del array[i]
				i -=1
			elif val == '/':
				array[i-1] = array[i-1] / array[i+1]
				del array[i]
				del array[i]
				i -=1
			i += 1

		i = 0
		while i < len(array):
			val = array[i]
			if val == '+':
				array[i-1] = array[i-1] + array[i+1]
				del array[i]
				del array[i]
				i -=1
			elif val == '-':
				array[i-1] = array[i-1] - array[i+1]
				del array[i]
				del array[i]
				i -=1
			i += 1

		return array
