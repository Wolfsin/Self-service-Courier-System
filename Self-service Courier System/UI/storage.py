# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storage.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from UI.storage_add import Ui_Manual_add_Dialog
from entity.Goods import Goods
from Connect import DBController
import cv2
import imutils
from imutils.video import VideoStream
import numpy as np
import multiprocessing as mp
from pyzbar import pyzbar
import time
import MakeCode
import SendSMS

class Ui_Storage_Dialog(object):
    def setupUi(self, Storage_Dialog):
        self.window = Storage_Dialog
        Storage_Dialog.setObjectName("Storage_Dialog")
        Storage_Dialog.resize(977, 830)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/Resource/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Storage_Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Storage_Dialog)
        self.verticalLayout_2.setContentsMargins(40, 40, 40, 40)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cameraFrame = QtWidgets.QFrame(Storage_Dialog)
        self.cameraFrame.setObjectName("cameraFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.cameraFrame)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_show_label = QtWidgets.QLabel(self.cameraFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_show_label.sizePolicy().hasHeightForWidth())
        self.img_show_label.setSizePolicy(sizePolicy)
        self.img_show_label.setMinimumSize(QtCore.QSize(200, 200))
        self.img_show_label.setMaximumSize(QtCore.QSize(200, 200))
        self.img_show_label.setFrameShape(QtWidgets.QFrame.Box)
        self.img_show_label.setText("")
        self.img_show_label.setPixmap(QtGui.QPixmap("UI/Resource/scan_code.png"))
        self.img_show_label.setScaledContents(True)
        self.img_show_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_show_label.setObjectName("img_show_label")
        self.horizontalLayout.addWidget(self.img_show_label)
        self.scanButtonLayout = QtWidgets.QVBoxLayout()
        self.scanButtonLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.scanButtonLayout.setContentsMargins(20, 0, 20, 0)
        self.scanButtonLayout.setObjectName("scanButtonLayout")
        self.startScan_pushButton = QtWidgets.QPushButton(self.cameraFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startScan_pushButton.sizePolicy().hasHeightForWidth())
        self.startScan_pushButton.setSizePolicy(sizePolicy)
        self.startScan_pushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.startScan_pushButton.setMaximumSize(QtCore.QSize(150, 50))
        self.startScan_pushButton.setObjectName("startScan_pushButton")
        self.scanButtonLayout.addWidget(self.startScan_pushButton)
        self.stopScan_pushButton = QtWidgets.QPushButton(self.cameraFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopScan_pushButton.sizePolicy().hasHeightForWidth())
        self.stopScan_pushButton.setSizePolicy(sizePolicy)
        self.stopScan_pushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.stopScan_pushButton.setMaximumSize(QtCore.QSize(150, 50))
        self.stopScan_pushButton.setObjectName("stopScan_pushButton")
        self.scanButtonLayout.addWidget(self.stopScan_pushButton)
        self.horizontalLayout.addLayout(self.scanButtonLayout)
        self.verticalLayout_2.addWidget(self.cameraFrame, 0, QtCore.Qt.AlignHCenter)
        self.resulttable = QtWidgets.QTableWidget(Storage_Dialog)
        self.resulttable.setMinimumSize(QtCore.QSize(600, 0))
        self.resulttable.setObjectName("resulttable")
        self.resulttable.setColumnCount(3)
        self.resulttable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.resulttable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.resulttable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.resulttable.setHorizontalHeaderItem(2, item)
        # 设置第1列的列宽
        self.resulttable.setColumnWidth(0, 350)
        # 设置第2列的列宽
        self.resulttable.setColumnWidth(1, 300)
        self.resulttable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.resulttable)
        self.addFrame = QtWidgets.QFrame(Storage_Dialog)
        self.addFrame.setObjectName("addFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.addFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_pushButton = QtWidgets.QPushButton(self.addFrame)
        self.add_pushButton.setMinimumSize(QtCore.QSize(120, 40))
        self.add_pushButton.setObjectName("add_pushButton")
        self.horizontalLayout_2.addWidget(self.add_pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.done_pushButton = QtWidgets.QPushButton(self.addFrame)
        self.done_pushButton.setMinimumSize(QtCore.QSize(120, 40))
        self.done_pushButton.setObjectName("done_pushButton")
        self.horizontalLayout_2.addWidget(self.done_pushButton)
        self.verticalLayout_2.addWidget(self.addFrame, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Storage_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Storage_Dialog)
        self.previous_barcode = set()

    def retranslateUi(self, Storage_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Storage_Dialog.setWindowTitle(_translate("Storage_Dialog", "快递自助收取一体机 -快件入库"))
        self.startScan_pushButton.setText(_translate("Storage_Dialog", "开始扫描"))
        self.stopScan_pushButton.setText(_translate("Storage_Dialog", "停止扫描"))
        item = self.resulttable.horizontalHeaderItem(0)
        item.setText(_translate("Storage_Dialog", "快递单号"))
        item = self.resulttable.horizontalHeaderItem(1)
        item.setText(_translate("Storage_Dialog", "收货手机"))
        item = self.resulttable.horizontalHeaderItem(2)
        item.setText(_translate("Storage_Dialog", "货柜号"))
        self.add_pushButton.setText(_translate("Storage_Dialog", "手动添加"))
        self.done_pushButton.setText(_translate("Storage_Dialog", "完成添加"))

        self.startScan_pushButton.clicked.connect(self.start_scan)
        self.add_pushButton.clicked.connect(self.manual_add)
        self.done_pushButton.clicked.connect(self.done)
        self.stopScan_pushButton.clicked.connect(self.stop_scan)
        self.stopScan_pushButton.setEnabled(False)

    def stop_scan(self):
        self.stopflag = True
        self.stopScan_pushButton.setEnabled(False)
        self.startScan_pushButton.setEnabled(True)
        
    def start_scan(self):
        self.stopScan_pushButton.setEnabled(True)
        self.startScan_pushButton.setEnabled(False)
        self.stopflag = False
        frame_count = 0
        barcode = None
        pool = mp.Pool(processes=4)
        vs = VideoStream(usePiCamera=True, resolution=(1088,1088)).start()
        time.sleep(2.0)
        # 捕捉图像，识别条形码
        while True:
            frame = vs.read()
            if frame_count == 1:
                r1 = pool.apply_async(self.spot, [frame])
                barcode = r1.get()
                self.img_show_label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
            elif frame_count == 5:
                r2 = pool.apply_async(self.spot, [frame])
                barcode = r2.get()
                self.img_show_label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
            elif frame_count == 9:
                r3 = pool.apply_async(self.spot, [frame])
                barcode = r3.get()
                self.img_show_label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
            elif frame_count == 13:
                r4 = pool.apply_async(self.spot, [frame])
                barcode = r4.get()
                self.img_show_label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
            elif frame_count == 16:
                self.img_show_label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
                frame_count = 0
                # 当按下停止识别按钮
            elif self.stopflag:
                self.img_show_label.setPixmap(QtGui.QPixmap("UI/Resource/scan_code.png"))
                QtWidgets.QApplication.processEvents()
                vs.stop()
                break
            elif barcode:
                if barcode in self.previous_barcode:
                    self.img_show_label.setPixmap(QtGui.QPixmap("UI/Resource/scan_code.png"))
                    QtWidgets.QApplication.processEvents()
                    QtWidgets.QMessageBox.information(self.window, '出错了!', '该快递单号已在列表中！!', QtWidgets.QMessageBox.Close)
                    vs.stop()
                    break
                else:
                    self.previous_barcode.add(barcode)
                    self.img_show_label.setPixmap(QtGui.QPixmap("UI/Resource/scan_success.png"))
                    QtWidgets.QApplication.processEvents()
                    self.auto_add(barcode)
                    barcode = None
                    # 休眠2秒
                    time.sleep(2.0)
            else:
                self.img_show_label.setPixmap(self.img2pixmap(frame))
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

    def auto_add(self, barcode):
        allrow = self.resulttable.rowCount()
        self.resulttable.setRowCount(allrow + 1)
        express_number = barcode
        DBMaxContainerNumber = DBController().find_max_container_number()
        container_number = int(DBMaxContainerNumber)+1
        if self.resulttable.item(allrow - 1, 2):
            if int(self.resulttable.item(allrow - 1, 2).text()) >= container_number:
                container_number = "%03d" % (int(self.resulttable.item(allrow - 1, 2).text()) + 1)
        else:
            container_number = "%03d" % container_number
        # 创建item
        express_number_item = QtWidgets.QTableWidgetItem(express_number)
        phone_item = QtWidgets.QTableWidgetItem("")
        container_number_item = QtWidgets.QTableWidgetItem(container_number)
        # item居中对齐
        express_number_item.setTextAlignment(QtCore.Qt.AlignCenter)
        phone_item.setTextAlignment(QtCore.Qt.AlignCenter)
        container_number_item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.resulttable.setItem(allrow, 0, express_number_item)
        self.resulttable.setItem(allrow, 1, phone_item)
        self.resulttable.setItem(allrow, 2, container_number_item)

    def manual_add(self):
        manual_add_dialog = QtWidgets.QDialog()
        ui = Ui_Manual_add_Dialog()
        ui.setupUi(manual_add_dialog)
        select_ok = manual_add_dialog.exec_()
        manual_goods = ui.done()
        if select_ok:
            allrow = self.resulttable.rowCount()
            express_number = manual_goods.express_number
            phone = manual_goods.phone
            container_number = int(manual_goods.container_number)+1
            if self.resulttable.item(allrow - 1, 2):
                if int(self.resulttable.item(allrow - 1, 2).text()) >= container_number:
                    container_number = "%03d" % (int(self.resulttable.item(allrow - 1, 2).text()) + 1)
            else:
                container_number = "%03d" % container_number
            if express_number in self.previous_barcode:
                    QtWidgets.QMessageBox.information(self.window, '出错了!', '该快递单号已在列表中！!', QtWidgets.QMessageBox.Close)
            else:
                self.previous_barcode.add(express_number)
                self.resulttable.setRowCount(allrow + 1)
                # 创建item
                express_number_item = QtWidgets.QTableWidgetItem(express_number)
                phone_item = QtWidgets.QTableWidgetItem(phone)
                container_number_item = QtWidgets.QTableWidgetItem(container_number)
                # item居中对齐
                express_number_item.setTextAlignment(QtCore.Qt.AlignCenter)
                phone_item.setTextAlignment(QtCore.Qt.AlignCenter)
                container_number_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.resulttable.setItem(allrow, 0, express_number_item)
                self.resulttable.setItem(allrow, 1, phone_item)
                self.resulttable.setItem(allrow, 2, container_number_item)

    def done(self):
        item_list = []
        controller = DBController()
        for i in range(self.resulttable.rowCount()):
            goods_item = Goods(self.resulttable.item(i, 0).text())
            goods_item.phone = self.resulttable.item(i, 1).text()
            goods_item.container_number = self.resulttable.item(i, 2).text()
            goods_item.pick_up_code = MakeCode.make()
            if goods_item.express_number and goods_item.phone and goods_item.container_number:
                item_list.append(goods_item)
            else:
                QtWidgets.QMessageBox.information(self.window, '出错了!', '列表中有项目填写不完整，请完善信息!', QtWidgets.QMessageBox.Close)
                item_list.clear()
                break
        if item_list:
            success_item = controller.add_list_goods(item_list)
            if success_item:
                pass
            self.question(success_item)
            self.done_success()
            self.resulttable.setRowCount(0)
            self.resulttable.clearContents()

    def question(self, item_list):
        question_box = QtWidgets.QMessageBox(self.window)
        question_box.setWindowTitle('最后一步')
        question_box.setText("货物已入库，是否发送短信？")
        question_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        question_box.button(QtWidgets.QMessageBox.Yes).setText('发送')
        question_box.button(QtWidgets.QMessageBox.No).setText('稍后自行发送')
        question_box.exec()
        if question_box.clickedButton() == question_box.button(QtWidgets.QMessageBox.Yes):
            fail_item = []
            for goods in item_list:
                statusStr = SendSMS.send(goods.phone, goods.express_number, goods.container_number, goods.pick_up_code)
                if "0" is statusStr:
                    DBController().change_status(goods.goods_id, "msg", True)
                else:
                    fail_item.append(goods.express_number)
            if fail_item:
                    QtWidgets.QMessageBox.information(self.window, '出错了!',
                                                      "快递单号："+str(fail_item)[1:-1]+"短信发生失败，请前往Web端了解详情",
                                                      QtWidgets.QMessageBox.Close)

    def done_success(self):
        # QMessageBox.about(self,'关于','这是一个关于消息对话框!')
        msgBox = QtWidgets.QMessageBox(self.window)
        msgBox.setWindowTitle('添加成功')
        msgBox.setText("已完成添加，本窗口会自动关闭。")
        msgBox.setIconPixmap(QtGui.QPixmap("UI/Resource/done.png"))
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.button(QtWidgets.QMessageBox.Ok).animateClick(3 * 1000)  # 3秒自动关闭
        msgBox.exec()
