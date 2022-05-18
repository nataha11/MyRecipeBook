# importing libraries
from PyQt5.QtWidgets import *
import sys
import os
import sqlite3
from PyQt5.QtGui import QPixmap

# creating a class
# that inherits the QDialog class
class Window(QDialog):

	# constructor
	def __init__(self):
		super(Window, self).__init__()

		# setting window title
		self.setWindowTitle("Add recipe")

		# creating a group box
		self.formGroupBox = QGroupBox("Form")

		# creating a fields
		self.name = QLineEdit()
		self.description = QPlainTextEdit()
		self.ingredients = QPlainTextEdit()
		self.instruction = QPlainTextEdit()

		self.labelImage = QLabel()
		self.image_button = QPushButton('Upload image')
		self.image_button.clicked.connect(self.get_image_file)
		#костыль
		self.images = []
		# calling the method that create the form
		self.createForm()

		# creating a dialog button for ok and cancel
		self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

		# adding action when form is accepted
		self.buttonBox.accepted.connect(self.getInfo)

		# adding action when form is rejected
		self.buttonBox.rejected.connect(self.reject)

		# creating a vertical layout
		mainLayout = QVBoxLayout()

		# adding form group box to the layout
		mainLayout.addWidget(self.formGroupBox)

		# adding button box to the layout
		mainLayout.addWidget(self.buttonBox)

		# setting lay out
		self.setLayout(mainLayout)

	# get info method called when form is accepted
	#в идеале переименовать и сделать проверку корректности + добавить картинки
	#можно отправить в другой поток
	def getInfo(self):
		try:
			created = []
			if os.path.exists('recipes/{0}'.format(self.name.text())) == False: 
				os.mkdir('recipes/{0}'.format(self.name.text()))
				created.append('recipes/{0}'.format(self.name.text()))
				dir_name = self.name.text()
			else: 
				os.mkdir('recipes/{0}_1'.format(self.name.text()))
				dir_name = self.name.text()+'_1'
				created.append(dir_name)
			f_instruction = open('recipes/{0}/instruction.txt'.format(self.name.text()), 'w')
			f_instruction.write(self.instruction.toPlainText())

			f_descreption = open('recipes/{0}/descreption.txt'.format(self.name.text()), 'w')
			f_descreption.write(self.description.toPlainText())

			f_ingredients = open('recipes/{0}/ingredients.txt'.format(self.name.text()), 'w')
			f_ingredients.write(self.ingredients.toPlainText())

			os.mkdir('recipes/{0}/images'.format(self.name.text()))

			kostil = dict()
			kostil['name'] = self.name.text()
			kostil['description'] = f_descreption.name
			kostil['ingredients'] = f_ingredients.name
			kostil['instruction'] = f_instruction.name


			for i in range(len(self.images)):
				img_i = open('recipes/{0}/images/img_{1}.jpeg'.format(self.name.text(), i), 'wb')
				img_i.write(self.images[i])
				kostil['img_{0}'.format(i)] = img_i.name
				img_i.close()
			f_ingredients.close()
			f_descreption.close()
			f_ingredients.close()

			insert_recipe(kostil)
		except Exception as error:
			print(error)
			if os.path.exists(created[0]): os.rmdir(created[0])

		# closing the window
		self.close()

	def get_image_file(self):
		file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif)")
		self.images.append(open(file_name, 'rb').read())

		
		#self.labelImage.setPixmap(QPixmap(file_name))

	# creat form method,m
	def createForm(self):

		# creating a form layout
		layout = QFormLayout()

		# adding rows
		# for name and adding input text
		layout.addRow(QLabel("Name"), self.name)
		layout.addRow(QLabel("Description"), self.description)
		layout.addRow(QLabel("Ingredients"), self.ingredients)
		layout.addRow(QLabel("Instruction"), self.instruction)
		layout.addWidget(self.image_button)
		# setting layout
		self.formGroupBox.setLayout(layout)

#Здесь происходит жеская вставка в бд, не стоит это читать, оно работает, но на костылях
def insert_recipe(kostil):
	conn = sqlite3.connect('recipebook.db', timeout = 10)#не ебу зачем он нужен timeout без него не работает
	cur = conn.cursor()
	try:
		cur.execute('''
			INSERT INTO recipes (name, description, ingredeints, instruction) 
			VALUES (?, ?, ?, ?)
		''', (kostil['name'], kostil['description'], kostil['ingredients'], kostil['instruction']))
		
		cur.execute('''SELECT last_insert_rowid()''')
		recipe_id = cur.fetchall()[0][0]
		for elem in kostil:
			if elem not in ['name', 'description', 'instruction', 'ingredients']:
				cur.execute('''INSERT INTO images (image) VALUES (?)''', (kostil[elem],))
				cur.execute('''SELECT last_insert_rowid()''')
				img_id = cur.fetchall()[0][0]
				cur.execute('''INSERT INTO images_in_recipes (recipe_id, image_id) VALUES (?, ?)''', (recipe_id, img_id))
		conn.commit()
	except Exception as error:
		print(error)
		conn.rollback()
	conn.close()


# main method
if __name__ == '__main__':

	# create pyqt5 app
	app = QApplication(sys.argv)

	# create the instance of our Window
	window = Window()

	# showing the window
	window.show()

	# start the app
	sys.exit(app.exec())
