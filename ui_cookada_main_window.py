# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cookada_main_windowXDXVAi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import cookada_app_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1115, 726)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setStyleSheet(u"QFrame{\n"
"	border-bottom: 1px solid #000;\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.main_header.setFrameShape(QFrame.WinPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tittle_bar_container = QFrame(self.main_header)
        self.tittle_bar_container.setObjectName(u"tittle_bar_container")
        self.tittle_bar_container.setFrameShape(QFrame.StyledPanel)
        self.tittle_bar_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.tittle_bar_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle = QFrame(self.tittle_bar_container)
        self.left_menu_toggle.setObjectName(u"left_menu_toggle")
        self.left_menu_toggle.setMinimumSize(QSize(50, 0))
        self.left_menu_toggle.setMaximumSize(QSize(50, 16777215))
        self.left_menu_toggle.setStyleSheet(u"QFrame{\n"
"	background-color: #000;\n"
"}\n"
"QPushButton{\n"
"	padding: 5px 10px;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	background-color: #000;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"}")
        self.left_menu_toggle.setFrameShape(QFrame.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle_btn = QPushButton(self.left_menu_toggle)
        self.left_menu_toggle_btn.setObjectName(u"left_menu_toggle_btn")
        self.left_menu_toggle_btn.setMinimumSize(QSize(0, 50))
        self.left_menu_toggle_btn.setMaximumSize(QSize(50, 16777215))
        self.left_menu_toggle_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.left_menu_toggle_btn.setIcon(icon)
        self.left_menu_toggle_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.left_menu_toggle_btn)


        self.horizontalLayout_5.addWidget(self.left_menu_toggle)

        self.tittle_bar = QFrame(self.tittle_bar_container)
        self.tittle_bar.setObjectName(u"tittle_bar")
        self.tittle_bar.setStyleSheet(u"QLabel{\n"
"	color: #fff;\n"
"}")
        self.tittle_bar.setFrameShape(QFrame.StyledPanel)
        self.tittle_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.tittle_bar)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_6 = QLabel(self.tittle_bar)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamily(u"Open Sans Semibold")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.tittle_bar)


        self.horizontalLayout_2.addWidget(self.tittle_bar_container)

        self.top_right_btns = QFrame(self.main_header)
        self.top_right_btns.setObjectName(u"top_right_btns")
        self.top_right_btns.setMaximumSize(QSize(100, 16777215))
        self.top_right_btns.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"}")
        self.top_right_btns.setFrameShape(QFrame.StyledPanel)
        self.top_right_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.top_right_btns)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon1)
        self.minimizeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.restoreButton = QPushButton(self.top_right_btns)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon2)
        self.restoreButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.restoreButton)

        self.closeButton = QPushButton(self.top_right_btns)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.horizontalLayout_2.addWidget(self.top_right_btns)


        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMaximumSize(QSize(50, 16777215))
        self.left_side_menu.setStyleSheet(u"QFrame{\n"
"	background-color: #000;\n"
"}\n"
"QPushButton{\n"
"	padding: 20px 10px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: #000;\n"
"	color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 92, 157);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:  rgb(0, 92, 157);\n"
"	border-bottom: 2px solid rgb(255, 165, 24);\n"
"}")
        self.left_side_menu.setFrameShape(QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(7, 0, 0, 0)
        self.left_menu_top_buttons = QFrame(self.left_side_menu)
        self.left_menu_top_buttons.setObjectName(u"left_menu_top_buttons")
        self.left_menu_top_buttons.setFrameShape(QFrame.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.accounts_button = QPushButton(self.left_menu_top_buttons)
        self.accounts_button.setObjectName(u"accounts_button")
        self.accounts_button.setMinimumSize(QSize(100, 0))
        self.accounts_button.setStyleSheet(u"background-image: url(:/icons/icons/cil-user.png);\n"
"background-repeat: none;\n"
"padding-left: 50px;\n"
"background-position: center left;")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.accounts_button)

        self.home_button = QPushButton(self.left_menu_top_buttons)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setMinimumSize(QSize(100, 0))
        self.home_button.setStyleSheet(u"background-image: url(:/icons/icons/cil-home.png);\n"
"background-repeat: none;\n"
"padding-left: 50px;\n"
"background-position: center left;")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.home_button)


        self.verticalLayout_3.addWidget(self.left_menu_top_buttons)

        self.settings_button = QPushButton(self.left_side_menu)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setMinimumSize(QSize(100, 0))
        self.settings_button.setStyleSheet(u"background-image: url(:/icons/icons/cil-settings.png);\n"
"background-repeat: none;\n"
"padding-left: 50px;\n"
"background-position: center left;")

        self.verticalLayout_3.addWidget(self.settings_button)


        self.horizontalLayout.addWidget(self.left_side_menu)

        self.center_main_items = QFrame(self.main_body)
        self.center_main_items.setObjectName(u"center_main_items")
        self.center_main_items.setStyleSheet(u"")
        self.center_main_items.setFrameShape(QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.center_main_items)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.center_main_items)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.home_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.search_line = QLineEdit(self.home_page)
        self.search_line.setObjectName(u"search_line")
        self.search_line.setMinimumSize(QSize(0, 50))

        self.verticalLayout_7.addWidget(self.search_line)

        self.recipes_grid = QGridLayout()
        self.recipes_grid.setObjectName(u"recipes_grid")
        self.third_recipe_btn = QPushButton(self.home_page)
        self.third_recipe_btn.setObjectName(u"third_recipe_btn")
        self.third_recipe_btn.setMinimumSize(QSize(0, 200))
        self.third_recipe_btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(0, 69, 116);\n"
"	border-radius: 22px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 69, 116);\n"
"	border: 2px solid rgb(0, 69, 116);\n"
"	border-radius: 22px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 136, 255);\n"
"	border: 2px solid rgb(0, 69, 116);\n"
"	border-radius: 22px;\n"
"}\n"
"")

        self.recipes_grid.addWidget(self.third_recipe_btn, 2, 0, 1, 1)

        self.first_recipe_btn = QPushButton(self.home_page)
        self.first_recipe_btn.setObjectName(u"first_recipe_btn")
        self.first_recipe_btn.setMinimumSize(QSize(0, 200))
        self.first_recipe_btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(0, 69, 116);\n"
"	border-radius: 22px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 69, 116);\n"
"	border: 2px solid rgb(0, 69, 116);\n"
"	border-radius: 22px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 136, 255);\n"
"	border: 2px solid rgb(0, 69, 116);\n"
"	border-radius: 22px;\n"
"}\n"
"")

        self.recipes_grid.addWidget(self.first_recipe_btn, 0, 0, 1, 1)

        self.second_recipe_btn = QPushButton(self.home_page)
        self.second_recipe_btn.setObjectName(u"second_recipe_btn")
        self.second_recipe_btn.setMinimumSize(QSize(0, 200))
        self.second_recipe_btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(0, 69, 116);\n"
"	border-radius: 22px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 69, 116);\n"
"	border: 2px solid rgb(0, 69, 116);\n"
"	border-radius: 22px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 136, 255);\n"
"	border: 2px solid rgb(0, 69, 116);\n"
"	border-radius: 22px;\n"
"}\n"
"")

        self.recipes_grid.addWidget(self.second_recipe_btn, 0, 2, 1, 1)

        self.fourth_recipe_btn = QPushButton(self.home_page)
        self.fourth_recipe_btn.setObjectName(u"fourth_recipe_btn")
        self.fourth_recipe_btn.setMinimumSize(QSize(300, 200))
        self.fourth_recipe_btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(0, 69, 116);\n"
"	border-radius: 22px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 69, 116);\n"
"	border: 2px solid rgb(0, 69, 116);\n"
"	border-radius: 22px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 136, 255);\n"
"	border: 2px solid rgb(0, 69, 116);\n"
"	border-radius: 22px;\n"
"}\n"
"")

        self.recipes_grid.addWidget(self.fourth_recipe_btn, 2, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.recipes_grid)

        self.search_response_layout = QHBoxLayout()
        self.search_response_layout.setObjectName(u"search_response_layout")
        self.search_response_frame = QFrame(self.home_page)
        self.search_response_frame.setObjectName(u"search_response_frame")
        self.search_response_frame.setMinimumSize(QSize(400, 100))
        self.search_response_frame.setMaximumSize(QSize(800, 300))
        self.search_response_frame.setFrameShape(QFrame.StyledPanel)
        self.search_response_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.search_response_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.search_response_frame_2 = QFrame(self.search_response_frame)
        self.search_response_frame_2.setObjectName(u"search_response_frame_2")
        self.search_response_frame_2.setMinimumSize(QSize(400, 100))
        self.search_response_frame_2.setMaximumSize(QSize(800, 300))
        self.search_response_frame_2.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(0, 69, 116);\n"
"	border-radius: 22px;\n"
"}\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 69, 116);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"	padding: 10px;\n"
"	border: none;\n"
"	\n"
"}")
        self.search_response_frame_2.setFrameShape(QFrame.StyledPanel)
        self.search_response_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.search_response_frame_2)
        self.verticalLayout_11.setSpacing(7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.search_response_msg = QLabel(self.search_response_frame_2)
        self.search_response_msg.setObjectName(u"search_response_msg")
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        self.search_response_msg.setFont(font1)
        self.search_response_msg.setLayoutDirection(Qt.LeftToRight)
        self.search_response_msg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.search_response_msg)

        self.search_response_btn = QPushButton(self.search_response_frame_2)
        self.search_response_btn.setObjectName(u"search_response_btn")
        self.search_response_btn.setEnabled(True)
        self.search_response_btn.setMinimumSize(QSize(80, 50))
        self.search_response_btn.setMaximumSize(QSize(80, 50))
        self.search_response_btn.setAutoDefault(False)
        self.search_response_btn.setFlat(False)

        self.verticalLayout_11.addWidget(self.search_response_btn, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.search_response_frame_2)


        self.search_response_layout.addWidget(self.search_response_frame)


        self.verticalLayout_7.addLayout(self.search_response_layout)

        self.stackedWidget.addWidget(self.home_page)
        self.accounts_page = QWidget()
        self.accounts_page.setObjectName(u"accounts_page")
        self.accounts_page.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.accounts_page)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.login_response_frame = QFrame(self.accounts_page)
        self.login_response_frame.setObjectName(u"login_response_frame")
        self.login_response_frame.setMinimumSize(QSize(400, 100))
        self.login_response_frame.setMaximumSize(QSize(800, 300))
        self.login_response_frame.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(0, 69, 116);\n"
"	border-radius: 22px;\n"
"}\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 69, 116);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"	padding: 10px;\n"
"	border: none;\n"
"	\n"
"}")
        self.login_response_frame.setFrameShape(QFrame.StyledPanel)
        self.login_response_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.login_response_frame)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.login_response_msg = QLabel(self.login_response_frame)
        self.login_response_msg.setObjectName(u"login_response_msg")
        self.login_response_msg.setFont(font1)
        self.login_response_msg.setLayoutDirection(Qt.LeftToRight)
        self.login_response_msg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.login_response_msg)

        self.login_res_ok_btn = QPushButton(self.login_response_frame)
        self.login_res_ok_btn.setObjectName(u"login_res_ok_btn")
        self.login_res_ok_btn.setEnabled(True)
        self.login_res_ok_btn.setMinimumSize(QSize(80, 50))
        self.login_res_ok_btn.setMaximumSize(QSize(80, 50))
        self.login_res_ok_btn.setAutoDefault(False)
        self.login_res_ok_btn.setFlat(False)

        self.verticalLayout_4.addWidget(self.login_res_ok_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.login_response_frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.login_form_frame = QFrame(self.accounts_page)
        self.login_form_frame.setObjectName(u"login_form_frame")
        self.login_form_frame.setMinimumSize(QSize(450, 350))
        self.login_form_frame.setMaximumSize(QSize(450, 350))
        self.login_form_frame.setStyleSheet(u"border-radius: 20px;\n"
"")
        self.login_form_frame.setFrameShape(QFrame.StyledPanel)
        self.login_form_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.login_form_frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 10, 0, 10)
        self.input_fileds_frame = QFrame(self.login_form_frame)
        self.input_fileds_frame.setObjectName(u"input_fileds_frame")
        self.input_fileds_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(34, 34, 34);\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(1, 90, 153);\n"
"}\n"
"QLineEdit {\n"
"	border: 2px solid rgb(0, 93, 159);\n"
"	border-radius: 10px;\n"
"	padding: 15px;\n"
"	background-color: rgb(0, 69, 116);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(0, 66, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(206, 206, 206);\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding: 15px;\n"
"	background-color:rgb(14, 13, 24);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0, 66, 124);\n"
"}\n"
"QLabel{\n"
"	border:3px solid  rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	\n"
"	background-color: rgb(6, 63, 104);\n"
"}\n"
"QCheckBox{\n"
"	color: rgb(255, 255, 255);\n"
"	padding: 10px;\n"
"}\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(0, 93, 159);\n"
"	width: 20px;\n"
"	h"
                        "eight: 20px;\n"
"	border-radius: 10px;\n"
"    background:rgb(0, 0, 0);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(34, 34, 34);\n"
"	background-image: url(:/icons/icons/cil-check.png);\n"
"}")
        self.input_fileds_frame.setFrameShape(QFrame.StyledPanel)
        self.input_fileds_frame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.input_fileds_frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.input_fileds_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 50))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.username = QLineEdit(self.input_fileds_frame)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(200, 50))
        self.username.setMaximumSize(QSize(200, 16777215))
        self.username.setStyleSheet(u"border:3px solid  rgb(43, 31, 91);\n"
"border-radius: 10px;")
        self.username.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.username)

        self.label_5 = QLabel(self.input_fileds_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 50))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.password = QLineEdit(self.input_fileds_frame)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(200, 50))
        self.password.setMaximumSize(QSize(200, 16777215))
        self.password.setStyleSheet(u"border:3px solid  rgb(43, 31, 91);\n"
"border-radius: 10px;")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.password)

        self.checkBox = QCheckBox(self.input_fileds_frame)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.checkBox)

        self.login_btn = QPushButton(self.input_fileds_frame)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(0, 50))
        self.login_btn.setMaximumSize(QSize(200, 16777215))

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.login_btn)

        self.profile_icon_frame = QFrame(self.input_fileds_frame)
        self.profile_icon_frame.setObjectName(u"profile_icon_frame")
        self.profile_icon_frame.setMinimumSize(QSize(50, 50))
        self.profile_icon_frame.setMaximumSize(QSize(50, 50))
        self.profile_icon_frame.setStyleSheet(u"image: url(:/icons/icons/cil-user-follow.png);\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 25px;\n"
"border: 3px solid rgb(0, 93, 159);")
        self.profile_icon_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_icon_frame.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.profile_icon_frame)


        self.verticalLayout_8.addWidget(self.input_fileds_frame, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.login_form_frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.accounts_page)
        self.recipe_page = QWidget()
        self.recipe_page.setObjectName(u"recipe_page")
        self.recipe_page.setMinimumSize(QSize(0, 0))
        self.recipe_page.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.recipe_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scroll_area = QScrollArea(self.recipe_page)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setMinimumSize(QSize(1000, 600))
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setAlignment(Qt.AlignCenter)
        self.scroll_contents = QWidget()
        self.scroll_contents.setObjectName(u"scroll_contents")
        self.scroll_contents.setGeometry(QRect(0, 0, 1016, 1000))
        self.scroll_contents.setMinimumSize(QSize(1000, 1000))
        self.scroll_contents.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.scroll_contents)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.recipe_description_frame = QFrame(self.scroll_contents)
        self.recipe_description_frame.setObjectName(u"recipe_description_frame")
        self.recipe_description_frame.setMinimumSize(QSize(0, 0))
        self.recipe_description_frame.setMaximumSize(QSize(16777215, 16777215))
        self.recipe_description_frame.setFrameShape(QFrame.StyledPanel)
        self.recipe_description_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.recipe_description_frame)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.vert_layout = QVBoxLayout()
        self.vert_layout.setObjectName(u"vert_layout")
        self.recipe_name = QLabel(self.recipe_description_frame)
        self.recipe_name.setObjectName(u"recipe_name")
        self.recipe_name.setEnabled(False)
        self.recipe_name.setMaximumSize(QSize(16777215, 100))
        font3 = QFont()
        font3.setPointSize(26)
        self.recipe_name.setFont(font3)
        self.recipe_name.setStyleSheet(u"border:3px solid  rgb(43, 31, 91);\n"
"border-color: rgb(62, 154, 62);\n"
"border-radius: 10px;\n"
"background-color: rgb(0,0,0)")
        self.recipe_name.setAlignment(Qt.AlignCenter)

        self.vert_layout.addWidget(self.recipe_name)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.recipe_image = QLabel(self.recipe_description_frame)
        self.recipe_image.setObjectName(u"recipe_image")
        self.recipe_image.setEnabled(False)
        self.recipe_image.setMinimumSize(QSize(400, 300))
        self.recipe_image.setMaximumSize(QSize(16777215, 16777215))
        self.recipe_image.setFont(font3)
        self.recipe_image.setStyleSheet(u"border:3px solid  rgb(43, 31, 91);\n"
"border-color: rgb(1, 90, 153);\n"
"border-radius: 10px;\n"
"background-color: rgb(0,0,0)\n"
"")
        self.recipe_image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.recipe_image)

        self.recipe_ingredients = QTextEdit(self.recipe_description_frame)
        self.recipe_ingredients.setObjectName(u"recipe_ingredients")
        self.recipe_ingredients.setMinimumSize(QSize(400, 300))
        self.recipe_ingredients.setStyleSheet(u"background-color:rgb(25, 25, 25);\n"
"border:3px solid;\n"
"border-color: rgb(1, 90, 153);\n"
"border-radius: 10px;\n"
"background-color: rgb(0,0,0)")
        self.recipe_ingredients.setLineWidth(5)

        self.horizontalLayout_6.addWidget(self.recipe_ingredients)


        self.vert_layout.addLayout(self.horizontalLayout_6)

        self.recipe_description = QTextEdit(self.recipe_description_frame)
        self.recipe_description.setObjectName(u"recipe_description")
        self.recipe_description.setStyleSheet(u"background-color:rgb(25, 25, 25);\n"
"border:3px solid;\n"
"border-color: rgb(1, 90, 153);\n"
"border-radius: 10px;\n"
"background-color: rgb(0,0,0)")

        self.vert_layout.addWidget(self.recipe_description)


        self.verticalLayout_13.addLayout(self.vert_layout)


        self.gridLayout_2.addWidget(self.recipe_description_frame, 0, 0, 1, 1)

        self.scroll_area.setWidget(self.scroll_contents)

        self.verticalLayout_10.addWidget(self.scroll_area)

        self.stackedWidget.addWidget(self.recipe_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_page.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.settings_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.settings_page)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setPointSize(50)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"background-color: rgb(84, 84, 84);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.center_main_items)


        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMinimumSize(QSize(0, 50))
        self.main_footer.setMaximumSize(QSize(16777215, 30))
        self.main_footer.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-top-color: solid 1px  rgb(0, 0, 0);\n"
"}\n"
"QLabel{\n"
"	color: #fff;\n"
"}")
        self.main_footer.setFrameShape(QFrame.WinPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_footer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.main_footer)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.main_footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.search_response_btn.setDefault(False)
        self.login_res_ok_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.left_menu_toggle_btn.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cookada Desk-Top App", None))
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
        self.closeButton.setText("")
        self.accounts_button.setText(QCoreApplication.translate("MainWindow", u"ACCOUNT", None))
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.third_recipe_btn.setText(QCoreApplication.translate("MainWindow", u"\u043e\u043c\u043b\u0435\u0442", None))
        self.first_recipe_btn.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0430\u0441\u0442\u0430", None))
        self.second_recipe_btn.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043b\u043e\u0432", None))
        self.fourth_recipe_btn.setText(QCoreApplication.translate("MainWindow", u"\u0431\u043b\u0438\u043d\u044b", None))
        self.search_response_msg.setText(QCoreApplication.translate("MainWindow", u"Login response message", None))
        self.search_response_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.login_response_msg.setText(QCoreApplication.translate("MainWindow", u"Login response message", None))
        self.login_res_ok_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Keep me logged in", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.recipe_name.setText(QCoreApplication.translate("MainWindow", u"Recipe name", None))
        self.recipe_image.setText(QCoreApplication.translate("MainWindow", u"Recipe image", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Setttings Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"v 1.0", None))
    # retranslateUi

