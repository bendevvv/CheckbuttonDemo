"""
Program: GUI_template.py
Chapter 8 (page 251)
8/7/2024

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

GUI-based app for demonstrating the use of the checkbox/checkbutton grahpic component.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font

class CheckbuttonDemo(EasyFrame):
	def __init__(self):
		EasyFrame.__init__(self, "Menu Options", 320, 200, "#513", False)
		self.addLabel("Today's Menu", 0, 0, 2, 1, "NSEW", Font(family="Elephant", size=28), "#513", "#8BF")

		self.chickenCB = self.addCheckbutton("Chicken", 1, 0)
		self.friesCB = self.addCheckbutton("French Fries", 1, 1)
		self.beansCB = self.addCheckbutton("Green Beans", 2, 0)
		self.applesauceCB = self.addCheckbutton("Applesauce", 2, 1)

		for i in [self.chickenCB, self.friesCB, self.beansCB, self.applesauceCB]:
			i["background"] = "#624"
			i["foreground"] = "#8BF"

		self.order = self.addButton("Place Order", 3, 0, 2, command=self.PlaceOrder)
		self.order["background"] = "#624"
		self.order["foreground"] = "#6FB"
		self.order["width"] = 22
		self.order["height"] = 2

	def PlaceOrder(self):
		message = ""
		total = self.chickenCB.isChecked() + self.beansCB.isChecked() + self.friesCB.isChecked() + self.applesauceCB.isChecked()
		match(total):
			case 0: #none, prewritten
				message = "No food was ordered."
			case 1: #one was ordered - just find it
				message = "Chicken was ordered" if self.chickenCB.isChecked() else "French Fries were ordered" if self.friesCB.isChecked() else "Green Beans were ordered" if self.beansCB.isChecked() else "Applesauce was ordered"
			case 2: #two were ordered - find the two, and add "and" before the 2nd
				if self.chickenCB.isChecked(): #is the first one, never has "and" before it if present, don't bother testing
					total -= 1
					message += "Chicken "
				if self.friesCB.isChecked():
					total -= 1
					if total == 0:
						message += "and "
					message += "French Fries "
				if self.beansCB.isChecked():
					total -= 1
					if total == 0:
						message += "and "
					message += "Green Beans "
				if self.applesauceCB.isChecked(): #is the last one, always has "and" before it if present, don't bother testing
					#total -= 1
					message += "and Applesauce "
				message += "were ordered"
			case 3: #all but one were ordered - find it but opposite
				message = "French Fries, Green Beans, and Applesauce were ordered" if not self.chickenCB.isChecked() else "Chicken, Green Beans, and Applesauce were ordered" if not self.friesCB.isChecked() else "Chicken, French Fries, and Applesauce were ordered" if not self.beansCB.isChecked() else "Chicken, French Fries, and Green Beans were ordered"
			case 4: #all, prewritten
				message = "Chicken, French Fries, Green Beans, and Applesauce were ordered"

		self.messageBox("Customer Order", message)

def main():
	CheckbuttonDemo().mainloop()

if __name__ == '__main__':
	main()