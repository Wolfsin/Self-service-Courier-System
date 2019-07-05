from PyQt5 import QtWidgets


def show(error_message):
    msgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '出错了', error_message+"，请联系工作人员")
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec()


def show_fail_item(fail_item):
    msgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '出错了', "添加失败的快递单号为："+str(fail_item)[1:-1]+"，请重新添加")
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec()
