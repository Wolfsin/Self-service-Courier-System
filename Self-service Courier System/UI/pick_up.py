# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pick_up.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Connect import DBController
import cv2
import imutils
from imutils.video import VideoStream
import numpy as np
import multiprocessing as mp
from pyzbar import pyzbar
import time


class Ui_PickUp_Dialog(object):
    def setupUi(self, PickUp_Dialog):
        self.window = PickUp_Dialog
        PickUp_Dialog.setObjectName("PickUp_Dialog")
        PickUp_Dialog.resize(975, 793)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/Resource/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PickUp_Dialog.setWindowIcon(icon)
        self.formLayout = QtWidgets.QFormLayout(PickUp_Dialog)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setObjectName("formLayout")
        self.note_Frame = QtWidgets.QFrame(PickUp_Dialog)
        self.note_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.note_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.note_Frame.setObjectName("note_Frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.note_Frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.instruction_img_label = QtWidgets.QLabel(self.note_Frame)
        self.instruction_img_label.setEnabled(True)
        self.instruction_img_label.setMinimumSize(QtCore.QSize(640, 640))
        self.instruction_img_label.setMaximumSize(QtCore.QSize(640, 640))
        self.instruction_img_label.setText("")
        self.instruction_img_label.setPixmap(QtGui.QPixmap("UI/Resource/instruction.png"))
        self.instruction_img_label.setScaledContents(True)
        self.instruction_img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.instruction_img_label.setObjectName("instruction_img_label")
        self.verticalLayout.addWidget(self.instruction_img_label)
        self.start_scan_button = QtWidgets.QPushButton(self.note_Frame)
        self.start_scan_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_scan_button.sizePolicy().hasHeightForWidth())
        self.start_scan_button.setSizePolicy(sizePolicy)
        self.start_scan_button.setMinimumSize(QtCore.QSize(0, 79))
        self.start_scan_button.setMaximumSize(QtCore.QSize(500000, 500000))
        self.start_scan_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.start_scan_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.start_scan_button.setObjectName("start_scan_button")
        self.verticalLayout.addWidget(self.start_scan_button)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.note_Frame)
        self.function_Layout = QtWidgets.QVBoxLayout()
        self.function_Layout.setObjectName("function_Layout")
        self.pick_up_Zone = QtWidgets.QFrame(PickUp_Dialog)
        self.pick_up_Zone.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pick_up_Zone.setObjectName("pick_up_Zone")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pick_up_Zone)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.trackingNumber_Layout = QtWidgets.QHBoxLayout()
        self.trackingNumber_Layout.setObjectName("trackingNumber_Layout")
        self.trackingNumber_label = QtWidgets.QLabel(self.pick_up_Zone)
        self.trackingNumber_label.setObjectName("trackingNumber_label")
        self.trackingNumber_Layout.addWidget(self.trackingNumber_label)
        self.trackingNumber_lineEdit = QtWidgets.QLineEdit(self.pick_up_Zone)
        self.trackingNumber_lineEdit.setObjectName("trackingNumber_lineEdit")
        self.trackingNumber_Layout.addWidget(self.trackingNumber_lineEdit)
        self.verticalLayout_2.addLayout(self.trackingNumber_Layout)
        self.pickUpCode_Layout = QtWidgets.QHBoxLayout()
        self.pickUpCode_Layout.setObjectName("pickUpCode_Layout")
        self.pickUpCode_label = QtWidgets.QLabel(self.pick_up_Zone)
        self.pickUpCode_label.setObjectName("pickUpCode_label")
        self.pickUpCode_Layout.addWidget(self.pickUpCode_label)
        self.pickUpCode_lineEdit = QtWidgets.QLineEdit(self.pick_up_Zone)
        self.pickUpCode_lineEdit.setObjectName("pickUpCode_lineEdit")
        self.pickUpCode_Layout.addWidget(self.pickUpCode_lineEdit)
        self.verticalLayout_2.addLayout(self.pickUpCode_Layout)
        self.done_pushButton = QtWidgets.QPushButton(self.pick_up_Zone)
        self.done_pushButton.setMinimumSize(QtCore.QSize(0, 79))
        self.done_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.done_pushButton.setObjectName("done_pushButton")
        self.verticalLayout_2.addWidget(self.done_pushButton)
        self.function_Layout.addWidget(self.pick_up_Zone)
        self.Keypad_Layout = QtWidgets.QFrame(PickUp_Dialog)
        self.Keypad_Layout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Keypad_Layout.setObjectName("Keypad_Layout")
        self.gridLayout = QtWidgets.QGridLayout(self.Keypad_Layout)
        self.gridLayout.setObjectName("gridLayout")
        self.number4_pushButton = QtWidgets.QPushButton(self.Keypad_Layout)
        self.number4_pushButton.setMinimumSize(QtCore.QSize(79, 79))
        self.number4_pushButton.setMaximumSize(QtCore.QSize(79, 79))
        self.number4_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.number4_pushButton.setObjectName("number4_pushButton")
        self.gridLayout.addWidget(self.number4_pushButton, 1, 0, 1, 1)
        self.number9_pushButton = QtWidgets.QPushButton(self.Keypad_Layout)
        self.number9_pushButton.setMinimumSize(QtCore.QSize(79, 79))
        self.number9_pushButton.setMaximumSize(QtCore.QSize(79, 79))
        self.number9_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.number9_pushButton.setObjectName("number9_pushButton")
        self.gridLayout.addWidget(self.number9_pushButton, 0, 2, 1, 1)
        self.number3_pushButton = QtWidgets.QPushButton(self.Keypad_Layout)
        self.number3_pushButton.setMinimumSize(QtCore.QSize(79, 79))
        self.number3_pushButton.setMaximumSize(QtCore.QSize(79, 79))
        self.number3_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.number3_pushButton.setObjectName("number3_pushButton")
        self.gridLayout.addWidget(self.number3_pushButton, 2, 2, 1, 1)
        self.number1_pushButton = QtWidgets.QPushButton(self.Keypad_Layout)
        self.number1_pushButton.setMinimumSize(QtCore.QSize(79, 79))
        self.number1_pushButton.setMaximumSize(QtCore.QSize(79, 79))
        self.number1_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.number1_pushButton.setObjectName("number1_pushButton")
        self.gridLayout.addWidget(self.number1_pushButton, 2, 0, 1, 1)
        self.number6_pushButton = QtWidgets.QPushButton(self.Keypad_Layout)
        self.number6_pushButton.setMinimumSize(QtCore.QSize(79, 79))
        self.number6_pushButton.setMaximumSize(QtCore.QSize(79, 79))
        self.number6_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.number6_pushButton.setObjectName("number6_pushButton")
        self.gridLayout.addWidget(self.number6_pushButton, 1, 2, 1, 1)
        self.number8_pushButton = QtWidgets.QPushButton(self.Keypad_Layout)
        self.number8_pushButton.setMinimumSize(QtCore.QSize(79, 79))
        self.number8_pushButton.setMaximumSize(QtCore.QSize(79, 79))
        self.number8_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.number8_pushButton.setObjectName("number8_pushButton")
        self.gridLayout.addWidget(self.number8_pushButton, 0, 1, 1, 1)
        self.number7_pushButton = QtWidgets.QPushButton(self.Keypad_Layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number7_pushButton.sizePolicy().hasHeightForWidth())
        self.number7_pushButton.setSizePolicy(sizePolicy)
        self.number7_pushButton.setMinimumSize(QtCore.QSize(79, 79))
        self.number7_pushButton.setMaximumSize(QtCore.QSize(79, 79))
        self.number7_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.number7_pushButton.setObjectName("number7_pushButton")
        self.gridLayout.addWidget(self.number7_pushButton, 0, 0, 1, 1)
        self.number5_pushButton = QtWidgets.QPushButton(self.Keypad_Layout)
        self.number5_pushButton.setMinimumSize(QtCore.QSize(79, 79))
        self.number5_pushButton.setMaximumSize(QtCore.QSize(79, 79))
        self.number5_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.number5_pushButton.setObjectName("number5_pushButton")
        self.gridLayout.addWidget(self.number5_pushButton, 1, 1, 1, 1)
        self.number2_pushButton = QtWidgets.QPushButton(self.Keypad_Layout)
        self.number2_pushButton.setMinimumSize(QtCore.QSize(79, 79))
        self.number2_pushButton.setMaximumSize(QtCore.QSize(79, 79))
        self.number2_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.number2_pushButton.setObjectName("number2_pushButton")
        self.gridLayout.addWidget(self.number2_pushButton, 2, 1, 1, 1)
        self.reEnter_pushButton = QtWidgets.QPushButton(self.Keypad_Layout)
        self.reEnter_pushButton.setMinimumSize(QtCore.QSize(0, 79))
        self.reEnter_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.reEnter_pushButton.setObjectName("reEnter_pushButton")
        self.gridLayout.addWidget(self.reEnter_pushButton, 3, 1, 1, 2)
        self.number0_pushButton = QtWidgets.QPushButton(self.Keypad_Layout)
        self.number0_pushButton.setMinimumSize(QtCore.QSize(79, 79))
        self.number0_pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.number0_pushButton.setObjectName("number0_pushButton")
        self.gridLayout.addWidget(self.number0_pushButton, 3, 0, 1, 1)
        self.function_Layout.addWidget(self.Keypad_Layout)
        self.camera_show_label = QtWidgets.QLabel(PickUp_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_show_label.sizePolicy().hasHeightForWidth())
        self.camera_show_label.setSizePolicy(sizePolicy)
        self.camera_show_label.setMinimumSize(QtCore.QSize(267, 267))
        self.camera_show_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.camera_show_label.setText("")
        self.camera_show_label.setPixmap(QtGui.QPixmap("UI/Resource/scan_code.png"))
        self.camera_show_label.setScaledContents(True)
        self.camera_show_label.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_show_label.setObjectName("camera_show_label")
        self.function_Layout.addWidget(self.camera_show_label)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.function_Layout)

        self.retranslateUi(PickUp_Dialog)
        QtCore.QMetaObject.connectSlotsByName(PickUp_Dialog)

    def retranslateUi(self, PickUp_Dialog):
        _translate = QtCore.QCoreApplication.translate
        PickUp_Dialog.setWindowTitle(_translate("PickUp_Dialog", "快递自助收取一体机 -确认收货"))
        self.start_scan_button.setText(_translate("PickUp_Dialog", "按下按钮开始尝试自动识别"))
        self.trackingNumber_label.setText(_translate("PickUp_Dialog", "快递单号："))
        self.pickUpCode_label.setText(_translate("PickUp_Dialog", "取货码：  "))
        self.done_pushButton.setText(_translate("PickUp_Dialog", "确认收货"))
        self.number4_pushButton.setText(_translate("PickUp_Dialog", "4"))
        self.number9_pushButton.setText(_translate("PickUp_Dialog", "9"))
        self.number3_pushButton.setText(_translate("PickUp_Dialog", "3"))
        self.number1_pushButton.setText(_translate("PickUp_Dialog", "1"))
        self.number6_pushButton.setText(_translate("PickUp_Dialog", "6"))
        self.number8_pushButton.setText(_translate("PickUp_Dialog", "8"))
        self.number7_pushButton.setText(_translate("PickUp_Dialog", "7"))
        self.number5_pushButton.setText(_translate("PickUp_Dialog", "5"))
        self.number2_pushButton.setText(_translate("PickUp_Dialog", "2"))
        self.reEnter_pushButton.setText(_translate("PickUp_Dialog", "重新输入"))
        self.number0_pushButton.setText(_translate("PickUp_Dialog", "0"))

        self.start_scan_button.clicked.connect(self.start_scan)
        self.number0_pushButton.clicked.connect(lambda: self.inputCode(0))
        self.number1_pushButton.clicked.connect(lambda: self.inputCode(1))
        self.number2_pushButton.clicked.connect(lambda: self.inputCode(2))
        self.number3_pushButton.clicked.connect(lambda: self.inputCode(3))
        self.number4_pushButton.clicked.connect(lambda: self.inputCode(4))
        self.number5_pushButton.clicked.connect(lambda: self.inputCode(5))
        self.number6_pushButton.clicked.connect(lambda: self.inputCode(6))
        self.number7_pushButton.clicked.connect(lambda: self.inputCode(7))
        self.number8_pushButton.clicked.connect(lambda: self.inputCode(8))
        self.number9_pushButton.clicked.connect(lambda: self.inputCode(9))
        self.reEnter_pushButton.clicked.connect(self.re_enter)
        self.done_pushButton.clicked.connect(self.done)

    def inputCode(self, number):
        trackingNumber = self.trackingNumber_lineEdit.text()
        code = self.pickUpCode_lineEdit.text()
        if self.trackingNumber_lineEdit.hasFocus():
            trackingNumber += str(number)
            self.trackingNumber_lineEdit.setText(trackingNumber)
        elif self.pickUpCode_lineEdit.hasFocus():
            code += str(number)
            self.pickUpCode_lineEdit.setText(code)

    def re_enter(self):
        if self.trackingNumber_lineEdit.hasFocus():
            self.trackingNumber_lineEdit.clear()
        elif self.pickUpCode_lineEdit.hasFocus():
            self.pickUpCode_lineEdit.clear()

    def start_scan(self):
        self.start_scan_button.setEnabled(False)
        frame_count = 0
        barcode = None
        pool = mp.Pool(processes=4)
        vs = VideoStream(usePiCamera=True, resolution=(1088,1088)).start()
        self.start_scan_button.setText("正在识别，请参考显示区将条形码对准")
        QtWidgets.QApplication.processEvents()
        time.sleep(2.0)
        start_time = time.clock()
        # 捕捉图像，识别条形码
        while True:
            end_time = time.clock()
            frame = vs.read()
            if frame_count == 1:
                r1 = pool.apply_async(self.spot, [frame])
                barcode = r1.get()
                self.camera_show_label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
            elif frame_count == 5:
                r2 = pool.apply_async(self.spot, [frame])
                barcode = r2.get()
                self.camera_show_label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
            elif frame_count == 9:
                r3 = pool.apply_async(self.spot, [frame])
                barcode = r3.get()
                self.camera_show_label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
            elif frame_count == 13:
                r4 = pool.apply_async(self.spot, [frame])
                barcode = r4.get()
                self.camera_show_label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
            elif frame_count == 16:
                self.camera_show_label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
                frame_count = 0
                # 识别超过10s时自动终止识别
            elif end_time-start_time > 10:
                self.instruction_img_label.setPixmap(QtGui.QPixmap("UI/Resource/oops_instruction.png"))
                self.camera_show_label.setPixmap(QtGui.QPixmap("UI/Resource/scan_code.png"))
                self.start_scan_button.setText("按下按钮再次尝试自动识别")
                vs.stop()
                self.start_scan_button.setEnabled(True)
                break
            elif barcode:
                self.trackingNumber_lineEdit.setText(barcode)
                self.camera_show_label.setPixmap(QtGui.QPixmap("UI/Resource/scan_success.png"))
                self.start_scan_button.setText("识别完成")
                self.pickUpCode_lineEdit.setFocus()
                vs.stop()
                self.start_scan_button.setEnabled(True)
                break
            else:
                self.camera_show_label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
            frame_count += 1
        # pass

    def spot(self, img):
        code = None
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 参数设置为只识别CODE128条形码
        barcodes = pyzbar.decode(gray, symbols=[pyzbar.ZBarSymbol.CODE128])
        for barcode in barcodes:
            # 设置识别出内容的编码
            barcodeData = barcode.data.decode("utf-8")
            # reformat 只留下具体内容
            code = "{}".format(barcodeData)
        return code
        # pass

    # 将np.array格式图像转换为Pixmap格式方便放入Qt中
    def img2pixmap(self, image):
        Y, X = image.shape[:2]
        self._bgra = np.zeros((Y, X, 4), dtype=np.uint8, order='C')
        self._bgra[..., 0] = image[..., 0]
        self._bgra[..., 1] = image[..., 1]
        self._bgra[..., 2] = image[..., 2]
        qimage = QtGui.QImage(self._bgra.data, X, Y, QtGui.QImage.Format_RGB32)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(640, 640)
        return pixmap
        # pass

    def done(self):
        trackingNumber = self.trackingNumber_lineEdit.text()
        code = self.pickUpCode_lineEdit.text()
        controller = DBController()
        goodsid = controller.find_goods(trackingNumber)
        if "had_error" is goodsid:
            pass
        elif goodsid:
            confirm_flag = controller.confirm_code(goodsid, code)
            if confirm_flag is True:
                success_flag = controller.change_status(goodsid, "pickup", True)
                if success_flag is True:
                    self.done_success()
                elif "had_error" is success_flag:
                    pass
                else:
                    QtWidgets.QMessageBox.information(self.window, '出错了!', '该快件已被确认收货，请联系工作人员!',
                                                      QtWidgets.QMessageBox.Close)
                self.instruction_img_label.setPixmap(QtGui.QPixmap("UI/Resource/instruction.png"))
                self.camera_show_label.setPixmap(QtGui.QPixmap("UI/Resource/scan_code.png"))
                self.trackingNumber_lineEdit.clear()
                self.pickUpCode_lineEdit.clear()
            elif "had_error" is confirm_flag:
                pass
            else:
                QtWidgets.QMessageBox.information(self.window, '出错了！', '请检查取货码是否输入正确!', QtWidgets.QMessageBox.Close)
        else:
            QtWidgets.QMessageBox.information(self.window, '出错了！', '请检查快递单号是否输入正确!',QtWidgets.QMessageBox.Close)
        self.start_scan_button.setText("按下按钮开始尝试自动识别")

    def done_success(self):
        # QMessageBox.about(self,'关于','这是一个关于消息对话框!')
        msgBox = QtWidgets.QMessageBox(self.window)
        msgBox.setWindowTitle('收货成功')
        msgBox.setText("恭喜您！您已完成本次收货，本窗口会自动关闭。")
        msgBox.setIconPixmap(QtGui.QPixmap("UI/Resource/done.png"))
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.button(QtWidgets.QMessageBox.Ok).animateClick(3 * 1000)  # 3秒自动关闭
        msgBox.exec()
