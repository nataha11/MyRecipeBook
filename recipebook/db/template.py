from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
import sqlite3


class recipeTemplate(QWidget):
	def __init__(self, recipeName):
		super(recipeTemplate, self).__init__()
		self.setWindowTitle("Add recipe")
		#self.setWindowFlag(QtCore.sheet)
		self.createForm()


		

	def createForm(self):
		pass
		# creating a form layout
		#layout = QFormLayout()

		# adding rows
		# for name and adding input text
		
		# setting layout
		

if __name__ == '__main__':

	# create pyqt5 app
	app = QApplication(sys.argv)

	# create the instance of our Window
	window = recipeTemplate("huy")

	# showing the window
	window.show()

	# start the app
	sys.exit(app.exec())