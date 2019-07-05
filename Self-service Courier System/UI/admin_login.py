# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_login.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Connect import DBController
import UI.storage


class Ui_Login_Window(object):
    def setupUi(self, Login_Window):
        self.window = Login_Window
        Login_Window.setObjectName("Login_Window")
        Login_Window.setWindowModality(QtCore.Qt.NonModal)
        Login_Window.setEnabled(True)
        Login_Window.resize(255, 143)
        Login_Window.setMinimumSize(QtCore.QSize(255, 143))
        Login_Window.setMaximumSize(QtCore.QSize(255, 143))
        Login_Window.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Login_Window.setModal(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/Resource/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login_Window.setWindowIcon(icon)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Login_Window)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.userLayout = QtWidgets.QHBoxLayout()
        self.userLayout.setObjectName("userLayout")
        self.userlabel = QtWidgets.QLabel(Login_Window)
        self.userlabel.setObjectName("userlabel")
        self.userLayout.addWidget(self.userlabel)
        self.userlineEdit = QtWidgets.QLineEdit(Login_Window)
        self.userlineEdit.setObjectName("userlineEdit")
        self.userLayout.addWidget(self.userlineEdit)
        self.verticalLayout.addLayout(self.userLayout)
        self.pswlLayout = QtWidgets.QHBoxLayout()
        self.pswlLayout.setObjectName("pswlLayout")
        self.pswlabel = QtWidgets.QLabel(Login_Window)
        self.pswlabel.setObjectName("pswlabel")
        self.pswlLayout.addWidget(self.pswlabel)
        spacerItem = QtWidgets.QSpacerItem(12, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.pswlLayout.addItem(spacerItem)
        self.pswlineEdit = QtWidgets.QLineEdit(Login_Window)
        self.pswlineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pswlineEdit.setObjectName("pswlineEdit")
        self.pswlLayout.addWidget(self.pswlineEdit)
        self.verticalLayout.addLayout(self.pswlLayout)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.loginButton = QtWidgets.QPushButton(Login_Window)
        self.loginButton.setObjectName("loginButton")
        self.buttonLayout.addWidget(self.loginButton)
        self.cancelButton = QtWidgets.QPushButton(Login_Window)
        self.cancelButton.setObjectName("cancelButton")
        self.buttonLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.buttonLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        # 去掉标题栏的代码
        self.window.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.retranslateUi(Login_Window)
        QtCore.QMetaObject.connectSlotsByName(Login_Window)

    def retranslateUi(self, Login_Window):
        _translate = QtCore.QCoreApplication.translate
        Login_Window.setWindowTitle(_translate("Login_Window", "管理员登录"))
        self.userlabel.setText(_translate("Login_Window", "用户名："))
        self.pswlabel.setText(_translate("Login_Window", "密码："))
        self.loginButton.setText(_translate("Login_Window", "确认"))
        self.cancelButton.setText(_translate("Login_Window", "取消"))
        self.loginButton.clicked.connect(self.login)
        self.cancelButton.clicked.connect(self.window.close)

    def login(self):
        username = self.userlineEdit.text()
        psd = self.pswlineEdit.text()
        controller = DBController()
        success_flag = controller.find_user(username, psd)
        if success_flag is True:
            self.login_success()
        elif "had_error" is success_flag:
            pass
        else:
            message = QtWidgets.QMessageBox(self.window)
            message.setWindowTitle('出错了！')
            message.setIcon(QtWidgets.QMessageBox.Critical)
            message.setText("请输入正确的用户名和密码")
            message.setStandardButtons(QtWidgets.QMessageBox.Close)
            message.setDetailedText('如果您没有可用的用户名，请前往WEB端进行注册！')
            message.exec()

    def login_success(self):
        self.window.close()
        storage_dialog = QtWidgets.QDialog()
        ui = UI.storage.Ui_Storage_Dialog()
        ui.setupUi(storage_dialog)
        storage_dialog.show()
        storage_dialog.exec_()




