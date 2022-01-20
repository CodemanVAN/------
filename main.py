import sys
import threading
import time
import datetime
import random

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import mainWindows
import login
import checkError
import downloadFile
import uploadFiles
import modifyEquipment
import reportError
import systemUpdata
import findPassword

def showMessage(message,wd,mtype='information'):
    if mtype == 'information':
        QtWidgets.QMessageBox.information(wd.wd,'提示',message)
    if mtype == 'warning':
        QtWidgets.QMessageBox.warning(wd.wd,'警告',message)
    if mtype == 'critical':
        QtWidgets.QMessageBox.critical(wd.wd,'错误',message)
def loginFuntion():
    user=loginWd.user.text()
    password=loginWd.password.text()
    if password=='':
        showMessage('登录成功',loginWd)
        loginWd.close()
        mainWd.show()
    else:
        showMessage('账号或密码错误',loginWd,'critical')
def findPasswordFuntion():
    showMessage('找回密码后原来的密码将无法使用！',loginWd,'warning')
    findPasswordWd.show()
def findPasswordDoneFuntion():
    if findPasswordWd.lineEdit.text()=='******':
        showMessage('你的新密码为'+str(random.randint(100000,999999)),findPasswordWd)
    else:
        showMessage('序列号不正确',findPasswordWd,'critical')


def updataComboboxFuntion(comboBox):
    comboBox.clear()
    comboBox.addItems(equipmentList)
def equipmentChangeFuntion():
    info=[[96,0,40,0,'已关机','无','2021年12月28日'],
          [40,60,70,44,'故障中','程序无响应','2021年11月20日'],
          [64,0,55,0,'已关机','无','2021年12月06日']
          ]
    idx=mainWd.comboBox.currentIndex()
    mainWd.lcdNumber.display(info[idx][0])
    mainWd.progressBar.setValue(info[idx][1])
    mainWd.progressBar_2.setValue(info[idx][2])
    mainWd.progressBar_3.setValue(info[idx][3])
    mainWd.label_9.setText(info[idx][4])
    mainWd.label_11.setText(info[idx][5])
    mainWd.label_10.setText(info[idx][6])
def switchStateFuntion():
    showMessage('成功关机！',mainWd)

def addEquipmentFuntion():
    item=QtWidgets.QTableWidgetItem(modifyEquipmentWd.name.text())
    modifyEquipmentWd.tableWidget.setItem(3, 0, item)
    item=QtWidgets.QTableWidgetItem(modifyEquipmentWd.ip.text())
    modifyEquipmentWd.tableWidget.setItem(3, 1, item)
    item=QtWidgets.QTableWidgetItem(datetime.datetime.now().strftime('%Y年%m月%d日'))
    modifyEquipmentWd.tableWidget.setItem(3, 2, item)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    equipmentList=['1号设备','2号设备','3号设备']
    loginWd=login.Ui_Form()
    loginWd.loginBt.clicked.connect(loginFuntion)
    loginWd.forgotPassword.clicked.connect(findPasswordFuntion)
    loginWd.show()
    
    findPasswordWd=findPassword.Ui_Form()
    findPasswordWd.pushButton.clicked.connect(findPasswordDoneFuntion)
    
    checkErrorWd=checkError.Ui_Form()
    
    
    downloadFileWd=downloadFile.Ui_Form()
    
    
    uploadFilesWd=uploadFiles.Ui_Form()
    
    
    modifyEquipmentWd=modifyEquipment.Ui_Form()
    modifyEquipmentWd.add.clicked.connect(addEquipmentFuntion)
    modifyEquipmentWd.remove.clicked.connect(lambda idx:modifyEquipmentWd.tableWidget.removeRow(modifyEquipmentWd.tableWidget.currentRow()))
    systemUpdataWd=systemUpdata.Ui_Form()
    
    
    reportErrorWd=reportError.Ui_Form()
    
    mainWd=mainWindows.Ui_Form()
    mainWd.reportError.clicked.connect(reportErrorWd.show)
    mainWd.checkError.clicked.connect(checkErrorWd.show)
    #mainWd.comboBox.activated.connect(lambda comboBox:updataComboboxFuntion(mainWd.comboBox))
    mainWd.comboBox.currentIndexChanged.connect(equipmentChangeFuntion)
    mainWd.switchState.clicked.connect(switchStateFuntion)
    mainWd.modifyEquipment.clicked.connect(modifyEquipmentWd.show)
    sys.exit(app.exec_())
    