# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self):
        self.wd=QtWidgets.QMainWindow()
        self.setupUi(self.wd)
    def show(self):
        self.wd.show()
    def close(self):
        self.wd.close()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(211, 133)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 10, 169, 107))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.user = QtWidgets.QLineEdit(self.widget)
        self.user.setObjectName("user")
        self.horizontalLayout.addWidget(self.user)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setObjectName("password")
        self.horizontalLayout_2.addWidget(self.password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.forgotPassword = QtWidgets.QPushButton(self.widget)
        self.forgotPassword.setObjectName("forgotPassword")
        self.horizontalLayout_3.addWidget(self.forgotPassword)
        self.loginBt = QtWidgets.QPushButton(self.widget)
        self.loginBt.setObjectName("loginBt")
        self.horizontalLayout_3.addWidget(self.loginBt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录界面"))
        self.label.setText(_translate("Form", "账号"))
        self.label_2.setText(_translate("Form", "密码"))
        self.checkBox.setText(_translate("Form", "记住密码"))
        self.forgotPassword.setText(_translate("Form", "忘记密码？"))
        self.loginBt.setText(_translate("Form", "登录"))
