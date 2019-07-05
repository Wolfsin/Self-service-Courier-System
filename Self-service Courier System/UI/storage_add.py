# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storage_add.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Connect import DBController
from entity.Goods import Goods


class Ui_Manual_add_Dialog(object):
    def setupUi(self, Manual_add_Dialog):
        Manual_add_Dialog.setObjectName("Manual_add_Dialog")
        Manual_add_Dialog.resize(300, 140)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/Resource/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Manual_add_Dialog.setWindowIcon(icon)
        self.formLayout = QtWidgets.QFormLayout(Manual_add_Dialog)
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Manual_add_Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.trackingNumber_horizontalLayout = QtWidgets.QHBoxLayout()
        self.trackingNumber_horizontalLayout.setObjectName("trackingNumber_horizontalLayout")
        self.trackingNumber_label = QtWidgets.QLabel(Manual_add_Dialog)
        self.trackingNumber_label.setObjectName("trackingNumber_label")
        self.trackingNumber_horizontalLayout.addWidget(self.trackingNumber_label)
        self.trackingNumber_lineEdit = QtWidgets.QLineEdit(Manual_add_Dialog)
        self.trackingNumber_lineEdit.setObjectName("trackingNumber_lineEdit")
        self.trackingNumber_horizontalLayout.addWidget(self.trackingNumber_lineEdit)
        self.verticalLayout.addLayout(self.trackingNumber_horizontalLayout)
        self.phone_horizontalLayout = QtWidgets.QHBoxLayout()
        self.phone_horizontalLayout.setObjectName("phone_horizontalLayout")
        self.phone_label = QtWidgets.QLabel(Manual_add_Dialog)
        self.phone_label.setObjectName("phone_label")
        self.phone_horizontalLayout.addWidget(self.phone_label)
        self.phone_lineEdit = QtWidgets.QLineEdit(Manual_add_Dialog)
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.phone_horizontalLayout.addWidget(self.phone_lineEdit)
        self.verticalLayout.addLayout(self.phone_horizontalLayout)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Manual_add_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(Manual_add_Dialog)
        self.buttonBox.accepted.connect(Manual_add_Dialog.accept)
        self.buttonBox.rejected.connect(Manual_add_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Manual_add_Dialog)

    def retranslateUi(self, Manual_add_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Manual_add_Dialog.setWindowTitle(_translate("Manual_add_Dialog", "手动添加信息"))
        self.label.setText(_translate("Manual_add_Dialog", "手动添加"))
        self.trackingNumber_label.setText(_translate("Manual_add_Dialog", "快递单号："))
        self.phone_label.setText(_translate("Manual_add_Dialog", "收货手机："))

    def done(self):
        goods = Goods(self.trackingNumber_lineEdit.text())
        goods.phone = self.phone_lineEdit.text()
        goods.container_number = DBController().find_max_container_number()
        goods.pick_up_code = None
        return goods





