# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pick_up.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
import picamera
import picamera.array
from PIL import Image,ImageEnhance
import time
import sys
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import pytesseract
import multiprocessing as mp
from picamera.array import PiRGBArray


class Ui_Dialog(object):
    def __init__(self):
        print("open")
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(922, 745)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 640, 640))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(420, 710, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.test)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        
    def test(self):
        # initialize the video stream and allow the camera sensor to warm up
        print("[INFO] starting video stream...")
        count=0
        pool = mp.Pool( processes=4 )
        vs = VideoStream(usePiCamera=True, resolution=(1088,1088)).start()
        time.sleep(2.0)
        # loop over the frames from the video stream
        while True:
            # grab the frame from the threaded video stream and resize it to
            # have a maximum width of 1088 pixels
            frame = vs.read()
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #frame = imutils.resize(frame, width=640)
            #self.label.setPixmap(self.img2pixmap(frame))
            QtWidgets.QApplication.processEvents()
            if count == 1:
                r1 = pool.apply_async( self.do, [ frame ] )
                frame = imutils.resize(frame, width=640)
                self.label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
 
            elif count == 5:
                r2 = pool.apply_async(self.do, [ frame ] )
                frame = imutils.resize(frame, width=640)
                self.label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
 
            elif count == 9:
                r3 = pool.apply_async(self.do, [ frame ] )
                frame = imutils.resize(frame, width=640)
                self.label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
 
            elif count == 13:
                r4 = pool.apply_async( self.do, [ frame ] )
                frame = imutils.resize(frame, width=640)
                self.label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
                
            elif count == 16:
                self.label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()
                count = 0
            else:
                self.label.setPixmap(self.img2pixmap(frame))
                QtWidgets.QApplication.processEvents()                
                
            # find the barcodes in the frame and decode each of the barcodes
            #if count==4:
                #barcodes = pyzbar.decode(gray)
            # ocr=pytesseract.image_to_string(gray)
            # print(ocr)
                #print(barcodes)
                #count=0
            # loop over the detected barcodes
            #for barcode in barcodes:
                # extract the bounding box location of the barcode and draw
                # the bounding box surrounding the barcode on the image
                #(x, y, w, h) = barcode.rect
                #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # the barcode data is a bytes object so if we want to draw it
                # on our output image we need to convert it to a string first
                #barcodeData = barcode.data.decode("utf-8")
                #barcodeType = barcode.type
                # draw the barcode data and barcode type on the image
                #text = "{} ({})".format(barcodeData, barcodeType)
                #print(text)
                #cv2.putText(frame, text, (x, y - 10),
                #cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            # show the output frame
            #cv2.imshow("Barcode Scanner", frame)
            count+=1
            #key = cv2.waitKey(1) & 0xFF
            # if the `q` key was pressed, break from the loop
            #if key == ord("q"): 
                #break
        # close the output CSV file do a bit of cleanup
        print("[INFO] cleaning up...")
        #cv2.destroyAllWindows()
        vs.stop()
    
    def do(self,img):
        gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
        barcodes = pyzbar.decode(gray)
        print(barcodes)
        return barcodes
    
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
    
    def test2(self):
        # initialize the video stream and allow the camera sensor to warm up
        print("[INFO] starting video stream...")
        count=0
        vs = VideoStream(usePiCamera=True,resolution=(1088,1088)).start()
        time.sleep(2.0)
        while True:
            # grab the frame from the threaded video stream and resize it to
            # have a maximum width of 1088 pixels
            frame = vs.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = imutils.resize(frame, width=640)
            self.label.setPixmap(self.img2pixmap(frame))
            QtWidgets.QApplication.processEvents()    
            # find the barcodes in the frame and decode each of the barcodes
            if count==10:
                barcodes = pyzbar.decode(gray)
            # ocr=pytesseract.image_to_string(gray)
            # print(ocr)
                print(barcodes)
                count=0
            # loop over the detected barcodes
            #for barcode in barcodes:
                # extract the bounding box location of the barcode and draw
                # the bounding box surrounding the barcode on the image
                #(x, y, w, h) = barcode.rect
                #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # the barcode data is a bytes object so if we want to draw it
                # on our output image we need to convert it to a string first
                #barcodeData = barcode.data.decode("utf-8")
                #barcodeType = barcode.type
                # draw the barcode data and barcode type on the image
                #text = "{} ({})".format(barcodeData, barcodeType)
                #print(text)
                #cv2.putText(frame, text, (x, y - 10),
                #cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            # show the output frame
            #cv2.imshow("Barcode Scanner", frame)
            count+=1
            #key = cv2.waitKey(1) & 0xFF
            # if the `q` key was pressed, break from the loop
            #if key == ord("q"): 
                #break
        # close the output CSV file do a bit of cleanup
        print("[INFO] cleaning up...")
        #cv2.destroyAllWindows()
        vs.stop()        
        
def launch_app():
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    function_selection_window = Ui_Dialog()
    function_selection_window.setupUi(main)
    main.show()
    sys.exit(app.exec_())


launch_app()

