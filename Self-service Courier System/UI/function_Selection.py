# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function_Selection.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import UI.admin_login
import UI.pick_up


class Ui_Function_Selection_Window(object):
    def setupUi(self, Function_Selection_Window):
        self.window = Function_Selection_Window

        Function_Selection_Window.setObjectName("Function_Selection_Window")
        Function_Selection_Window.resize(800, 600)
        Function_Selection_Window.setMinimumSize(QtCore.QSize(800, 600))
        Function_Selection_Window.setMaximumSize(QtCore.QSize(800, 600))
        self.center()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/Resource/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Function_Selection_Window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Function_Selection_Window)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(40, 40, 40, 40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.welcome_pic = QtWidgets.QLabel(self.centralwidget)
        self.welcome_pic.setMaximumSize(QtCore.QSize(780, 287))
        self.welcome_pic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.welcome_pic.setAutoFillBackground(False)
        self.welcome_pic.setText("")
        self.welcome_pic.setPixmap(QtGui.QPixmap("UI/Resource/welcom.jpg"))
        self.welcome_pic.setScaledContents(True)
        self.welcome_pic.setObjectName("welcome_pic")
        self.verticalLayout.addWidget(self.welcome_pic)
        self.welcome_title = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome_title.sizePolicy().hasHeightForWidth())
        self.welcome_title.setSizePolicy(sizePolicy)
        self.welcome_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.welcome_title.setStyleSheet("font: -75 20pt \"微软雅黑\";")
        self.welcome_title.setTextFormat(QtCore.Qt.AutoText)
        self.welcome_title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.welcome_title.setObjectName("welcome_title")
        self.verticalLayout.addWidget(self.welcome_title)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.storeButton = QtWidgets.QPushButton(self.centralwidget)
        self.storeButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.storeButton.setStyleSheet("font: 20pt \"微软雅黑\"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI/Resource/storage_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.storeButton.setIcon(icon1)
        self.storeButton.setIconSize(QtCore.QSize(200, 200))
        self.storeButton.setObjectName("storeButton")
        self.horizontalLayout.addWidget(self.storeButton)
        self.pickupButton = QtWidgets.QPushButton(self.centralwidget)
        self.pickupButton.setStyleSheet("font: 20pt \"微软雅黑\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("UI/Resource/pickup_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pickupButton.setIcon(icon2)
        self.pickupButton.setIconSize(QtCore.QSize(200, 200))
        self.pickupButton.setObjectName("pickupButton")
        self.horizontalLayout.addWidget(self.pickupButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        Function_Selection_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Function_Selection_Window)
        self.storeButton.clicked.connect(self.jump_to_admin_login)
        self.pickupButton.clicked.connect(self.jump_to_pickup_window)
        QtCore.QMetaObject.connectSlotsByName(Function_Selection_Window)

    def retranslateUi(self, Function_Selection_Window):
        _translate = QtCore.QCoreApplication.translate
        Function_Selection_Window.setWindowTitle(_translate("Function_Selection_Window", "快递自助收取一体机 -欢迎使用"))
        self.welcome_title.setText(_translate("Function_Selection_Window", "欢迎使用科院快递自助收取一体机"))
        self.storeButton.setText(_translate("Function_Selection_Window", "  入库"))
        self.pickupButton.setText(_translate("Function_Selection_Window", "开始取件"))

    def center(self):
         screen = QtWidgets.QDesktopWidget().screenGeometry()
         size = self.window.geometry()
         self.window.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)

    def jump_to_admin_login(self):  # 这一块注意，是重点从主界面跳转到Demo1界面，主界面隐藏，如果关闭Demo界面，主界面进程会触发self.form.show()会再次显示主界面
        self.window.hide()  # 如果没有self.window.show()这一句，关闭Demo1界面后就会关闭程序,window为类的实例属性
        login_dialog = QtWidgets.QDialog()
        ui = UI.admin_login.Ui_Login_Window()
        ui.setupUi(login_dialog)
        login_dialog.show()
        login_dialog.exec_()
        self.window.show()

    def jump_to_pickup_window(self):
        self.window.hide()
        pickuo_dialog = QtWidgets.QDialog()
        ui = UI.pick_up.Ui_PickUp_Dialog()
        ui.setupUi(pickuo_dialog)
        pickuo_dialog.show()
        pickuo_dialog.exec_()
        self.window.show()





