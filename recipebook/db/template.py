import sys
import os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class recipeTemplate(QMainWindow):
	def __init__(self, recipeName):
		super(recipeTemplate, self).__init__()
		self.edit = QLineEdit(self)
		self.edit.textChanged.connect(self.func)
		self.show()
	def func(self):
		print("based")

		

		
if __name__ == '__main__':

	# create pyqt5 app
	app = QApplication(sys.argv)

	# create the instance of our Window
	window = recipeTemplate("window")

	# showing the window
	window.show()

	# start the app
	sys.exit(app.exec_())