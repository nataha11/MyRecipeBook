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

# The only class - MainClass
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        self.ui.first_recipe_but.clicked.connect(partial(self.createRecipePage, self.ui.first_recipe_but.text()))
        self.ui.second_recipe_but.clicked.connect(partial(self.createRecipePage, self.ui.second_recipe_but.text()))
        self.ui.third_recipe_but.clicked.connect(partial(self.createRecipePage, self.ui.third_recipe_but.text()))
        self.ui.fourth_recipe_but.clicked.connect(partial(self.createRecipePage, self.ui.fourth_recipe_but.text()))


        # ###############################################
        # LOGIN PAGE
        # ###############################################
        #When login btn is clicked:
        self.ui.login_btn.clicked.connect(self.validateLoginFields)
        #Hiding login response container:
        self.ui.login_response_frame.hide()
        #Hiding login response container after OK button is pressed:
        self.ui.login_res_ok_btn.clicked.connect(lambda:self.ui.login_response_frame.hide())
        #


        # ###############################################
        # CLICK EVENT LISTENER FOR STYLING PRESSED BUTTONS
        # ###############################################
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)




        # ###############################################
        # SHOW THE WINDOW
        # ###############################################
        self.show()

################################################################################################
##############################------CLASS METHODS-------########################################
################################################################################################

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
        print("HUY")
        db_catalog = "recipebook/db"
        conn = sqlite3.connect(db_catalog + "/recipebook.db", timeout=10)
        cur = conn.cursor()
        cur.execute('''
    			SELECT recipes.id, description, instruction, ingredeints, images.id
    			FROM recipes 
    			JOIN images_in_recipes ON recipes.id = images_in_recipes.recipe_id
    			JOIN images ON images_in_recipes.image_id = images.id
    			WHERE recipes.name = (?) ''', (recipeName,))
        data = cur.fetchall()
        conn.close()
        print(data)


        # decriptionPath = db_catalog + "/" + data[0][1]
        # instructionPath = db_catalog + "/" + data[0][2]
        # ingredientsPath = db_catalog + "/" + data[0][3]

        images_path = []
        for elem in data: images_path.append(elem[-1])

        def get_info(path) -> str:
            f = open(path, "r")
            info = f.read()
            f.close()
            return info

        description = get_info(db_catalog + "/" + data[0][1])
        instruction = get_info(db_catalog + "/" + data[0][2])
        ingridients = get_info(db_catalog + "/" + data[0][3])

        # дальше нужно высрать текст на label и картинки(до них хранятся пути)
        self.ui.stackedWidget.setCurrentWidget(self.ui.recipe_page)
        #self.ui.recipe_description.setText(QCoreApplication.translate("MainWindow", description, None))
        self.ui.recipe_description.setText(QCoreApplication.translate("MainWindow", instruction, None))
        self.ui.recipe_ingridients.setText(QCoreApplication.translate("MainWindow", ingridients, None))
        self.ui.recipe_name.setText(QCoreApplication.translate("MainWindow", recipeName, None))


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

