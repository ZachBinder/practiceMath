"""
Program: practiceMath
Author: Zach Binder
Date: 9-13-18

A basic math program which has the user enter 2 integers 
and chooses whether or not they would like
to add, subtract, multiply, or divide the 2
"""
#required imports
from breezypythongui import EasyFrame
import math

class PracticeMath(EasyFrame):
	def __init__(self):
		EasyFrame.__init__(self, title = "Learn Math")

		#Creating a label and field for the input
		self.addLabel(text = "First Number :", row = 0, column = 0, columnspan = 2)
		self.inputField = self.addIntegerField(value = 0, row = 0, column = 2, width = 10, columnspan = 2)

		#The addition button
		self.add = self.addButton(text = "     +     \n     Add     ", row = 2, column = 0, command = self.addNums)

		#The subtraction button
		self.sub = self.addButton(text = " - \n Subtract  ", row = 2, column = 1, command = self.subNums)
		
		#The multiplication button
		self.mult = self.addButton(text = " × \n Multiply ", row = 2, column = 2, command = self.multNums)
		
		#The division button
		self.div = self.addButton(text = "  ÷  \n  Divide   ", row = 2, column = 3, command = self.divNums)

		#changes the color for the addition button
		self.add["background"] = "pink"
		self.add["foreground"] = "black"

		#changes the color for the addition button
		self.sub["background"] = "chartreuse"
		self.sub["foreground"] = "black"

		#changes the color for the addition button
		self.mult["background"] = "orange"
		self.mult["foreground"] = "black"

		#changes the color for the addition button
		self.div["background"] = "lightblue"
		self.div["foreground"] = "black"

		#Creating a label and field for the second imput
		self.addLabel(text = "Second Number :", row = 1, column = 0, columnspan = 2)
		self.inputFieldTwo = self.addIntegerField(value = 0, row = 1, column = 2, width = 10, columnspan = 2)

		#Label and field for the input
		self.addLabel(text = "The Result is :", row = 3, column = 0, columnspan = 2)
		self.outputField = self.addIntegerField(value = 0, row = 3, column = 2, width = 10, state = "readonly", columnspan = 2)

	#method for adding the 2 numbers entered by the user
	def addNums(self):
		numOne = self.inputField.getNumber()
		numTwo = self.inputFieldTwo.getNumber()
		some = numOne + numTwo
		self.outputField.setNumber(some)

	#method for subtracting the 2 numbers entered by the user
	def subNums(self):
		numOne = self.inputField.getNumber()
		numTwo = self.inputFieldTwo.getNumber()
		subtract = numOne - numTwo
		self.outputField.setNumber(subtract)

	#method for dividing the 2 numbers entered by the user
	def divNums(self):
		numOne = self.inputField.getNumber()
		numTwo = self.inputFieldTwo.getNumber()
		divide = numOne / numTwo
		self.outputField.setNumber(divide)

	#method for multiplying the 2 numbers entered by the user
	def multNums(self):
		numOne = self.inputField.getNumber()
		numTwo = self.inputFieldTwo.getNumber()
		product = numOne * numTwo
		self.outputField.setNumber(product)

#main method which calls the practice math class and makes it run
def main():
	PracticeMath().mainloop()

#call to the main method
main()

