# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import movableLabel


class Ui_LoginUi(object):
    def setupUi(self, LoginUi):
        LoginUi.setObjectName("LoginUi")
        LoginUi.resize(1007, 772)
        self.horizontalLayout = QtWidgets.QHBoxLayout(LoginUi)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(LoginUi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color : black;\n"
"border-radius : 15px;\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LoginSide = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginSide.sizePolicy().hasHeightForWidth())
        self.LoginSide.setSizePolicy(sizePolicy)
        self.LoginSide.setMinimumSize(QtCore.QSize(0, 0))
        self.LoginSide.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LoginSide.setStyleSheet("\n"
"QWidget#LoginSide{\n"
"background-color : #111b21;\n"
"border-top-right-radius: 30px;\n"
"border-bottom-right-radius: 30px;\n"
"}\n"
"\n"
"QPushButton#loginButton , #registerButton{\n"
"    color : white;\n"
"    border: 2px solid ;\n"
"    border-radius: 20px;\n"
"    border-color: #00a884;\n"
"    background-color:#161219;\n"
"    fixed-width: 80px;\n"
"    margin-left: 20px;\n"
"    margin-right:20px;\n"
"    margin-bottom:10px;\n"
"    margin-top : 10px;\n"
"}\n"
"\n"
"QPushButton#loginButton:hover , #registerButton:hover{\n"
"    background-color: #00a884;\n"
"}\n"
"\n"
"\n"
"QPushButton#loginButton:pressed , #registerButton:pressed{\n"
"    background-color: #005c4b;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid #00a884;\n"
"color:rgba(255, 255, 255, 170);\n"
"border-radius: 0px;\n"
"margin-left : 20px;\n"
"margin-right : 20px;\n"
"margin-bottom : 20px;\n"
"}")
        self.LoginSide.setObjectName("LoginSide")
        self.gridLayout = QtWidgets.QGridLayout(self.LoginSide)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.loginButton = QtWidgets.QPushButton(self.LoginSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("")
        self.loginButton.setObjectName("loginButton")
        self.gridLayout.addWidget(self.loginButton, 4, 1, 1, 1)
        self.registerButton = QtWidgets.QPushButton(self.LoginSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerButton.sizePolicy().hasHeightForWidth())
        self.registerButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("")
        self.registerButton.setObjectName("registerButton")
        self.gridLayout.addWidget(self.registerButton, 5, 1, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.LoginSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout.addWidget(self.widget_5, 6, 1, 1, 1)
        self.passwLine = QtWidgets.QLineEdit(self.LoginSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwLine.sizePolicy().hasHeightForWidth())
        self.passwLine.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.passwLine.setFont(font)
        self.passwLine.setStyleSheet("")
        self.passwLine.setText("")
        self.passwLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwLine.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passwLine.setObjectName("passwLine")
        self.gridLayout.addWidget(self.passwLine, 2, 1, 1, 1)
        self.phoneLine = QtWidgets.QLineEdit(self.LoginSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phoneLine.sizePolicy().hasHeightForWidth())
        self.phoneLine.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.phoneLine.setFont(font)
        self.phoneLine.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.phoneLine.setStyleSheet("")
        self.phoneLine.setText("")
        self.phoneLine.setFrame(True)
        self.phoneLine.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.phoneLine.setObjectName("phoneLine")
        self.gridLayout.addWidget(self.phoneLine, 1, 1, 1, 1)
        self.errorLabel = QtWidgets.QLabel(self.LoginSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorLabel.sizePolicy().hasHeightForWidth())
        self.errorLabel.setSizePolicy(sizePolicy)
        self.errorLabel.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("background-color : rgba(0,0,0,0);\n"
"color : red;")
        self.errorLabel.setText("")
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        self.gridLayout.addWidget(self.errorLabel, 3, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.LoginSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.widget_3.setFont(font)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(28)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("image: url(:/newPrefix/Icons/RegisterPhoto.png);")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.LoginSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout.addWidget(self.widget_6, 0, 2, 7, 1)
        self.widget_4 = QtWidgets.QWidget(self.LoginSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_4, 0, 0, 7, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 2)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 2)
        self.gridLayout.setRowStretch(5, 2)
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout_2.addWidget(self.LoginSide, 1, 0, 2, 1)
        self.titleBar = QtWidgets.QWidget(self.widget)
        self.titleBar.setMinimumSize(QtCore.QSize(0, 40))
        self.titleBar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.titleBar.setStyleSheet("QWidget#titleBar{\n"
"border-radius : 15px;\n"
"}\n"
"QPushButton{\n"
"border-radius : 10px;\n"
"}\n"
"")
        self.titleBar.setObjectName("titleBar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.titleBar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 5, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = movableLabel.MovableLabel(self.titleBar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color : rgba(255,255,255,150);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.min = QtWidgets.QPushButton(self.titleBar)
        self.min.setMinimumSize(QtCore.QSize(20, 20))
        self.min.setMaximumSize(QtCore.QSize(20, 20))
        self.min.setStyleSheet("QPushButton{\n"
"background-color : rgba(0,170,0,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color : rgba(0,170,0,200);\n"
"}")
        self.min.setText("")
        self.min.setObjectName("min")
        self.horizontalLayout_2.addWidget(self.min)
        self.max = QtWidgets.QPushButton(self.titleBar)
        self.max.setMinimumSize(QtCore.QSize(20, 20))
        self.max.setMaximumSize(QtCore.QSize(20, 20))
        self.max.setStyleSheet("QPushButton{\n"
"background-color :rgba(240, 136, 0 ,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color : rgba(240 ,136, 0, 200);\n"
"}")
        self.max.setText("")
        self.max.setObjectName("max")
        self.horizontalLayout_2.addWidget(self.max)
        self.close = QtWidgets.QPushButton(self.titleBar)
        self.close.setMinimumSize(QtCore.QSize(20, 20))
        self.close.setMaximumSize(QtCore.QSize(20, 20))
        self.close.setStyleSheet("QPushButton{\n"
"background-color : rgba(240,0,0,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color : rgb(200, 0, 0);\n"
"}")
        self.close.setText("")
        self.close.setObjectName("close")
        self.horizontalLayout_2.addWidget(self.close)
        self.gridLayout_2.addWidget(self.titleBar, 0, 0, 1, 3)
        self.ImageSide = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageSide.sizePolicy().hasHeightForWidth())
        self.ImageSide.setSizePolicy(sizePolicy)
        self.ImageSide.setMinimumSize(QtCore.QSize(300, 0))
        self.ImageSide.setStyleSheet("QWidget#ImageSide\n"
"{\n"
"image: url(:/newPrefix/Icons/799053.png);\n"
"}")
        self.ImageSide.setObjectName("ImageSide")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ImageSide)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.ImageSide)
        self.frame.setMinimumSize(QtCore.QSize(20, 20))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.gridLayout_2.addWidget(self.ImageSide, 1, 1, 1, 1)
        self.RegisterSide = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RegisterSide.sizePolicy().hasHeightForWidth())
        self.RegisterSide.setSizePolicy(sizePolicy)
        self.RegisterSide.setMaximumSize(QtCore.QSize(0, 16777215))
        self.RegisterSide.setStyleSheet("\n"
"QWidget#RegisterSide{\n"
"background-color : #111b21;\n"
"border-top-left-radius: 30px;\n"
"border-bottom-left-radius: 30px;\n"
"}\n"
"\n"
"QPushButton#SubmitButton , #BrowseImage\n"
"{\n"
"    color : white;\n"
"    border: 2px solid ;\n"
"    border-radius: 20px;\n"
"    border-color: #00a884;\n"
"    background-color:#161219;\n"
"    fixed-width: 80px;\n"
"    margin-left: 20px;\n"
"    margin-right:20px;\n"
"    margin-bottom:10px;\n"
"    margin-top : 10px;\n"
"}\n"
"\n"
"QPushButton#SubmitButton:hover , #BrowseImage:hover{\n"
"    background-color: #00a884;\n"
"}\n"
"\n"
"\n"
"QPushButton#SubmitButton:pressed , #BrowseImage:pressed{\n"
"    background-color: #005c4b;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid #00a884;\n"
"color:rgba(255, 255, 255, 170);\n"
"border-radius: 0px;\n"
"margin-left : 20px;\n"
"margin-right : 20px;\n"
"margin-bottom : 20px;\n"
"}")
        self.RegisterSide.setObjectName("RegisterSide")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.RegisterSide)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.SubmitPass = QtWidgets.QLineEdit(self.RegisterSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubmitPass.sizePolicy().hasHeightForWidth())
        self.SubmitPass.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.SubmitPass.setFont(font)
        self.SubmitPass.setStyleSheet("")
        self.SubmitPass.setText("")
        self.SubmitPass.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SubmitPass.setObjectName("SubmitPass")
        self.gridLayout_4.addWidget(self.SubmitPass, 6, 0, 1, 2)
        self.SubmitPhone = QtWidgets.QLineEdit(self.RegisterSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubmitPhone.sizePolicy().hasHeightForWidth())
        self.SubmitPhone.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.SubmitPhone.setFont(font)
        self.SubmitPhone.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.SubmitPhone.setStyleSheet("")
        self.SubmitPhone.setText("")
        self.SubmitPhone.setFrame(True)
        self.SubmitPhone.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SubmitPhone.setObjectName("SubmitPhone")
        self.gridLayout_4.addWidget(self.SubmitPhone, 5, 0, 1, 2)
        self.widget_7 = QtWidgets.QWidget(self.RegisterSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"\n"
"color:rgba(255, 255, 255, 170);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.backToLogin = QtWidgets.QPushButton(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backToLogin.sizePolicy().hasHeightForWidth())
        self.backToLogin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.backToLogin.setFont(font)
        self.backToLogin.setStyleSheet("    color : #00a884;\n"
"    background-color:rgba(0,0,0,0);\n"
"    fixed-width: 80px;")
        self.backToLogin.setIconSize(QtCore.QSize(16, 16))
        self.backToLogin.setObjectName("backToLogin")
        self.horizontalLayout_5.addWidget(self.backToLogin)
        self.widget_10 = QtWidgets.QWidget(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_5.addWidget(self.widget_10)
        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 2)
        self.gridLayout_4.addWidget(self.widget_7, 9, 0, 1, 2)
        self.widget_8 = QtWidgets.QWidget(self.RegisterSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setContentsMargins(40, 20, 40, 20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SubmitButton = QtWidgets.QPushButton(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubmitButton.sizePolicy().hasHeightForWidth())
        self.SubmitButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setObjectName("SubmitButton")
        self.horizontalLayout_3.addWidget(self.SubmitButton)
        self.gridLayout_4.addWidget(self.widget_8, 8, 0, 1, 1)
        self.FirstName = QtWidgets.QLineEdit(self.RegisterSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FirstName.sizePolicy().hasHeightForWidth())
        self.FirstName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.FirstName.setFont(font)
        self.FirstName.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.FirstName.setStyleSheet("")
        self.FirstName.setText("")
        self.FirstName.setFrame(True)
        self.FirstName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FirstName.setObjectName("FirstName")
        self.gridLayout_4.addWidget(self.FirstName, 3, 0, 1, 1)
        self.widget_9 = QtWidgets.QWidget(self.RegisterSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setContentsMargins(40, 20, 40, 20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.BrowseImage = QtWidgets.QPushButton(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BrowseImage.sizePolicy().hasHeightForWidth())
        self.BrowseImage.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.BrowseImage.setFont(font)
        self.BrowseImage.setObjectName("BrowseImage")
        self.horizontalLayout_4.addWidget(self.BrowseImage)
        self.gridLayout_4.addWidget(self.widget_9, 8, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.RegisterSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.registerProfileImage = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerProfileImage.sizePolicy().hasHeightForWidth())
        self.registerProfileImage.setSizePolicy(sizePolicy)
        self.registerProfileImage.setMinimumSize(QtCore.QSize(140, 140))
        self.registerProfileImage.setMaximumSize(QtCore.QSize(140, 140))
        self.registerProfileImage.setStyleSheet("QLabel#registerProfileImage{\n"
"    border-image: url(:/newPrefix/Icons/RegisterPhoto.png);\n"
"    border-radius : 70px;\n"
"}")
        self.registerProfileImage.setText("")
        self.registerProfileImage.setObjectName("registerProfileImage")
        self.horizontalLayout_6.addWidget(self.registerProfileImage)
        self.aboutRegister = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.aboutRegister.setFont(font)
        self.aboutRegister.setObjectName("aboutRegister")
        self.horizontalLayout_6.addWidget(self.aboutRegister)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout_4.addWidget(self.widget_2, 0, 0, 1, 2)
        self.LastName = QtWidgets.QLineEdit(self.RegisterSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LastName.sizePolicy().hasHeightForWidth())
        self.LastName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LastName.setFont(font)
        self.LastName.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.LastName.setStyleSheet("")
        self.LastName.setText("")
        self.LastName.setFrame(True)
        self.LastName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LastName.setObjectName("LastName")
        self.gridLayout_4.addWidget(self.LastName, 3, 1, 1, 1)
        self.registerErrorLabel = QtWidgets.QLabel(self.RegisterSide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerErrorLabel.sizePolicy().hasHeightForWidth())
        self.registerErrorLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.registerErrorLabel.setFont(font)
        self.registerErrorLabel.setStyleSheet("color : rgba(200 , 0 , 0 ,     255);\n"
"margin-bottom : 30px;\n"
"margin-top : 30px;")
        self.registerErrorLabel.setText("")
        self.registerErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.registerErrorLabel.setObjectName("registerErrorLabel")
        self.gridLayout_4.addWidget(self.registerErrorLabel, 7, 0, 1, 2)
        self.gridLayout_2.addWidget(self.RegisterSide, 1, 2, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setColumnStretch(2, 3)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(LoginUi)
        QtCore.QMetaObject.connectSlotsByName(LoginUi)

    def retranslateUi(self, LoginUi):
        _translate = QtCore.QCoreApplication.translate
        LoginUi.setWindowTitle(_translate("LoginUi", "Form"))
        self.loginButton.setStatusTip(_translate("LoginUi", "login to the system"))
        self.loginButton.setText(_translate("LoginUi", "Login"))
        self.loginButton.setShortcut(_translate("LoginUi", "Return"))
        self.registerButton.setText(_translate("LoginUi", "Register"))
        self.passwLine.setPlaceholderText(_translate("LoginUi", "password"))
        self.phoneLine.setPlaceholderText(_translate("LoginUi", "Phone"))
        self.label.setText(_translate("LoginUi", "  Login - WhatsApp"))
        self.SubmitPass.setPlaceholderText(_translate("LoginUi", "password"))
        self.SubmitPhone.setPlaceholderText(_translate("LoginUi", "Phone"))
        self.label_2.setText(_translate("LoginUi", "have email already ?"))
        self.backToLogin.setText(_translate("LoginUi", "Login"))
        self.SubmitButton.setText(_translate("LoginUi", "Submit"))
        self.FirstName.setPlaceholderText(_translate("LoginUi", "First Name"))
        self.BrowseImage.setText(_translate("LoginUi", "Profile Image"))
        self.aboutRegister.setPlaceholderText(_translate("LoginUi", "about...."))
        self.LastName.setPlaceholderText(_translate("LoginUi", "Last Name"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginUi = QtWidgets.QWidget()
    ui = Ui_LoginUi()
    ui.setupUi(LoginUi)
    LoginUi.show()
    sys.exit(app.exec_())
