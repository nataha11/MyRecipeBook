#!/usr/bin/python3
# APP MAIN SCREEN

# APP Imports
import sys
import os
import platform
import sqlite3
from functools import partial
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_cookada_main_window import *

# Global value for the windows status for understanding min/max 
WINDOW_SIZE = 0;

# Функции поиска:
def search_branch(root, word, search_mistake, word_copy, dishes):
    iteration_number = 0

    if len(word) == 0:
        DFS(root, word_copy, root, dishes)
    else:
        for child in root.children:
            iteration_number += 1
            if child.letter == word[0]:
                search_branch(child, word[1:], search_mistake, word_copy, dishes)
                break

        # Если не нашли подходящего префикса
        if iteration_number == len(root.children) and len(word) != 0:
            search_mistake = 1

    return dishes


def DFS(current_root, word, root, dishes):
    # Добавляем в конец текущего слова новую полученную букву
    if current_root != root:
        word = word + current_root.letter

    # Проверка на то, подходит ли нам данное слово
    if current_root.accepting_state == 1:
        dishes.append(word)

    # Продолжение поиска
    for elem in current_root.children:
        DFS(elem, word, root, dishes)

    # Удаляем полученную на данном шаге букву
    word = word[:-1]

    return 0

class Node:
    def __init__(self, value):
        self.children = []
        self.letter = value
        self.accepting_state = 0

# Основная функция поиска, которая выдаёт список блюд по префиксу
def search(root, word):
    search_mistake = 0
    # Это массив блюд, которые удовлетворяют данному префиксу
    dishes = []
    word_copy = word
    dishes = search_branch(root, word, search_mistake, word_copy, dishes)

    return dishes

def CreateTree():
    path = "recipebook/db/recipebook.db"
    names = get_recipe_name(path)

    root = Node("")
    for name in names:
        insert(root, name)

    return root, names

def insert(root, word):
    if (len(word) == 0):
        root.accepting_state = 1
    else:
        for child in root.children:
            if word[0] == child.letter:
                insert(child, word[1:])
                return 0
        else:
            root.children.append(Node(word[0]))
            insert(root.children[-1], word[1:])
            return 0
    return 0

def get_recipe_name(db_path):
    conn = conn = sqlite3.connect('recipebook/db/recipebook.db')
    cur = conn.cursor()
    cur.execute('''
     SELECT DISTINCT name
     FROM recipes
     ''')
    rows = cur.fetchall()
    conn.close()
    names = []
    for elem in rows:
        names.append(elem[0].lower())

    return names

# The only class - MainClass
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.root, self.dishes = CreateTree()

        # Remove window tlttle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
      
        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Appy shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)


        #################################################
        # Button click events to our top bar buttons
        #################################################
        # Minimize window
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        # Close window
        self.ui.closeButton.clicked.connect(lambda: self.close())
        # Restore/Maximize window
        self.ui.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())


        # ###############################################
        # Move window on mouse drag event on the tittle bar
        # ###############################################
        def moveWindow(e):
            # Detect if the window is  normal size
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  
                # if left mouse button is clicked (Only accept left mouse button clicks (Not enter using Shift and Tab))
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        
        # ###############################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        # ###############################################
        self.ui.main_header.mouseMoveEvent = moveWindow


        # ###############################################
        # SLIDABLE LEFT MENU (the most gorgeous thing I've ever done)
        # ###############################################
        self.ui.left_menu_toggle_btn.clicked.connect(lambda: self.slideLeftMenu())


        # STACKED PAGES 
        # Main page (what you see opening the GUI)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        # ###############################################
        

        # ###############################################
        # STACKED PAGES NAVIGATION (using side menu buttons)
        # ###############################################

        #navigate to Home page
        self.ui.home_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
        #navigate to Accounts page
        self.ui.accounts_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.accounts_page))
        #navigate to Settings page
        self.ui.settings_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))
        #Тут необходимо добавить вызов recipe_page для обработки кнопок на home_page
        self.ui.first_recipe_btn.clicked.connect(partial(self.createRecipePage, self.ui.first_recipe_btn.text()))
        self.ui.second_recipe_btn.clicked.connect(partial(self.createRecipePage, self.ui.second_recipe_btn.text()))
        self.ui.third_recipe_btn.clicked.connect(partial(self.createRecipePage, self.ui.third_recipe_btn.text()))
        self.ui.fourth_recipe_btn.clicked.connect(partial(self.createRecipePage, self.ui.fourth_recipe_btn.text()))


        # ###############################################
        # LOGIN PAGE
        # ###############################################
        #When login btn is clicked:
        self.ui.login_btn.clicked.connect(self.validateLoginFields)
        #Hiding login response container:
        self.ui.login_response_frame.hide()
        self.ui.search_response_frame.hide()
        #Hiding login response container after OK button is pressed:
        self.ui.login_res_ok_btn.clicked.connect(lambda:self.ui.login_response_frame.hide())
        




        # ###############################################
        # CLICK EVENT LISTENER FOR STYLING PRESSED BUTTONS
        # ###############################################
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)

        ###################################################
        # Здесь будет реализована реакция на изменение текста в поисковике
        ###################################################
        self.ui.search_line.textChanged.connect(self.changeText)
        self.ui.search_line.returnPressed.connect(self.turnToPage)
        #подсказки в поиске
        

        # ###############################################
        # SHOW THE WINDOW
        # ###############################################
        self.show()

################################################################################################
##############################------CLASS METHODS-------########################################
################################################################################################
    ###################################################
    # Здесь будет реализована реакция на изменение текста в поисковике
    ###################################################

    def turnToPage(self):
        query = self.ui.search_line.text().lower()
        if(query in self.dishes): self.createRecipePage(query)
        else: print("wrong query")
        
    def changeText(self):
        widget_names = search(self.root, self.ui.search_line.text().lower())
        self.completer = QCompleter(widget_names)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.search_line.setCompleter(self.completer)
        
        


    #################################################
    # NICE THING. HIGHLIGHTS BTN if PRESSED
    #################################################
    def applyButtonStyle(self):
        #Resetting style for other buttons
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            if w.objectName() != self.sender().objectName(): #sender is equal to clicked button
                defaultStyle = w.styleSheet().replace("border-left: 2px solid rgb(0, 136, 255);", "")
                w.setStyleSheet(defaultStyle)

        newStyle = self.sender().styleSheet() + ("border-left: 2px solid rgb(0, 136, 255);")
        self.sender().setStyleSheet(newStyle)
        return


    #################################################
    # MOUSE EVENT (Onclick to move window)
    #################################################
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()


    #################################################
    # WINDOW MAIN BUTTONS
    #################################################
    # Restore or maximize your window
    def restore_or_maximize_window(self):
        # Global windows state
        global WINDOW_SIZE #The default value is zero to show that the size is not maximized
        win_status = WINDOW_SIZE

        if win_status == 0:
        	# If the window is not maximized
        	WINDOW_SIZE = 1 #Update value to show that the window has been maxmized
        	self.showMaximized()
        	# Update button icon  when window is maximized
        	self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-restore.png"))#Show minized icon
        else:
        	# If the window is on its default size
            WINDOW_SIZE = 0 #Update value to show that the window has been minimized/set to normal size (which is 800 by 400)
            self.showNormal()
            # Update button icon when window is minimized
            self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-maximize.png"))#Show maximize icon

    ################################################
    # Обработка поискового запроса. Сначала попытемся сделать простейший поиск по названию блюда
    ################################################

    def createRecipePage(self, recipeName):
        db_catalog = "recipebook/db"
        conn = sqlite3.connect(db_catalog + "/recipebook.db", timeout=10)
        cur = conn.cursor()
        cur.execute('''
    			SELECT recipes.id, description, instruction, ingredients, images.image
    			FROM recipes 
    			JOIN images_in_recipes ON recipes.id = images_in_recipes.recipe_id
    			JOIN images ON images_in_recipes.image_id = images.id
    			WHERE recipes.name = (?) ''', (recipeName,))
        data = cur.fetchall()
        conn.close()

        images_path = []
        for elem in data: images_path.append(db_catalog + "/" + elem[-1])

        def get_info(path) -> str:
            f = open(path, "r")
            info = f.read()
            f.close()
            return info

        description = get_info(db_catalog + "/" + data[0][1])
        instruction = get_info(db_catalog + "/" + data[0][2])
        ingredients = get_info(db_catalog + "/" + data[0][3])


        if(len(images_path) != 0):
            self.ui.recipe_image.setScaledContents(True)
            img = QPixmap(images_path[0])
            self.ui.recipe_image.setPixmap(img)
            self.ui.recipe_image.repaint()
            QApplication.processEvents()


        self.ui.stackedWidget.setCurrentWidget(self.ui.recipe_page)

        self.ui.recipe_description.setReadOnly(True)
        self.ui.recipe_description.setTextColor(QColor(255, 255, 255))
        self.ui.recipe_description.setWordWrapMode(QTextOption.WordWrap)
        self.ui.recipe_description.setFont(QFont("Times", 20))
        self.ui.recipe_description.setFontUnderline(20)
        self.ui.recipe_description.setText("Инструкция по приготовлению: \n" + QCoreApplication.translate("MainWindow", instruction, None))

        self.ui.recipe_ingredients.setReadOnly(True)
        self.ui.recipe_ingredients.setTextColor(QColor(255, 255, 255))
        self.ui.recipe_ingredients.setWordWrapMode(QTextOption.WordWrap)
        self.ui.recipe_ingredients.setFont(QFont("Times", 20))
        self.ui.recipe_ingredients.setPlainText("Необходимые ингридиенты: \n" + QCoreApplication.translate("MainWindow", ingredients, None))
        
        self.ui.recipe_name.setFont(QFont("Times", 25))
        self.ui.recipe_name.setStyleSheet('color:white')
        self.ui.recipe_name.setText(QCoreApplication.translate("MainWindow", recipeName, None).upper())
        self.ui.recipe_description.setReadOnly(True)


    #################################################
    # LOGIN VALIDATION SECTION
    #################################################
    def validateLoginFields(self):
        #Styles to be used to highlight input fields in succes/error
        succesStyle = "border:3px solid rgb(0, 255, 255); border-radius: 10px;"
        errorStyle = "border:3px solid rgb(255, 0, 0); border-radius: 10px;"

        #Check username
        if (not self.ui.username.text()):
            usernameResponse = " User login cannot be empty. "
            self.ui.username.setStyleSheet(errorStyle)
        else:
            usernameResponse = ""

        #Check password
        if (not self.ui.password.text()):
            passwordResponse = " User password cannot be empty. "
            self.ui.username.setStyleSheet(errorStyle)
        else:
            passwordResponse = ""

        #Check
        if passwordResponse != "" or usernameResponse != "":
            loginResponse = usernameResponse + passwordResponse
            self.showLoginResponse(loginResponse)
        else:
            #Check if the field values are correct (Database usage)
            correct_username = "FUCK"
            correct_password = "FUCK"

        #Set styles depending on login and password given
        if self.ui.username.text() == correct_username:
            usernameResponse = ""
            self.ui.username.setStyleSheet(succesStyle)
        else:
            usernameResponse = " Incorrect username. "
            self.ui.username.setStyleSheet(errorStyle)

        if self.ui.password.text() == correct_password:
            passwordResponse = ""
            self.ui.password.setStyleSheet(succesStyle)
        else:
            passwordResponse = " Incorrect password. "
            self.ui.password.setStyleSheet(errorStyle)

        #Create a response message
        if (usernameResponse == "" and passwordResponse == ""):
            loginResponse = " Login Successful. "
            self.showLoginResponse(loginResponse)
        elif (usernameResponse != "" and passwordResponse != ""):
            loginResponse = usernameResponse + "Also," + passwordResponse
            self.showLoginResponse(loginResponse)
        else:
            loginResponse = usernameResponse +  passwordResponse
            self.showLoginResponse(loginResponse)

    def showLoginResponse(self, responseMessage):
        #Show the login response container
        self.ui.login_response_frame.show()
        #Update the login response text
        self.ui.login_response_msg.setText(responseMessage)


    #################################################
    # SLIDE MENU
    #################################################
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.left_side_menu.width()
        # If minimized
        if width == 50:
            # Expand menu
            newWidth = 150
        # If maximized
        else:
            # Restore menu
            newWidth = 50

        # I struggled to determine how this magic happens, but I didn't succeed in it, therefore I copied it 
        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.left_side_menu, b"minimumWidth")#Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


#################################################
# LAUNCHING THE PROGRAMM
#################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
else:
	print(__name__, "hh")

