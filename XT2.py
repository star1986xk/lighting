# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XT2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(635, 298)
        MainWindow2.setStyleSheet("#centralwidget{\n"
"border-image: url(:/新前缀/img/bg.jpg);\n"
"}\n"
"QPushButton{\n"
"padding:2px 2px 2px 2px;\n"
"background-color: rgba(255,255,255,100);\n"
"border-style:none;\n"
"border-radius: 3px;\n"
"color:#ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"padding:2px 2px 2px 2px;\n"
"background-color: rgba(220, 220, 220,200);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"padding:2px 2px 2px 2px;\n"
"    /* 改变背景色 */  \n"
"    background-color:rgba(180, 180, 180,100);  \n"
"    /* 改变边框风格 */  \n"
"    border-style:inset;  \n"
"    /* 使文字有一点移动 */\n"
"    padding-left:1px;\n"
"    padding-top:1px;\n"
"    border-radius: 3px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 230, 616, 63))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PB1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB1.sizePolicy().hasHeightForWidth())
        self.PB1.setSizePolicy(sizePolicy)
        self.PB1.setMinimumSize(QtCore.QSize(90, 25))
        self.PB1.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB1.setFont(font)
        self.PB1.setObjectName("PB1")
        self.horizontalLayout.addWidget(self.PB1)
        self.PB2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB2.sizePolicy().hasHeightForWidth())
        self.PB2.setSizePolicy(sizePolicy)
        self.PB2.setMinimumSize(QtCore.QSize(90, 25))
        self.PB2.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB2.setFont(font)
        self.PB2.setObjectName("PB2")
        self.horizontalLayout.addWidget(self.PB2)
        self.PB5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.PB5.setMinimumSize(QtCore.QSize(90, 25))
        self.PB5.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB5.setFont(font)
        self.PB5.setObjectName("PB5")
        self.horizontalLayout.addWidget(self.PB5)
        self.PB4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB4.sizePolicy().hasHeightForWidth())
        self.PB4.setSizePolicy(sizePolicy)
        self.PB4.setMinimumSize(QtCore.QSize(90, 25))
        self.PB4.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB4.setFont(font)
        self.PB4.setObjectName("PB4")
        self.horizontalLayout.addWidget(self.PB4)
        self.PB3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB3.sizePolicy().hasHeightForWidth())
        self.PB3.setSizePolicy(sizePolicy)
        self.PB3.setMinimumSize(QtCore.QSize(90, 25))
        self.PB3.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB3.setFont(font)
        self.PB3.setObjectName("PB3")
        self.horizontalLayout.addWidget(self.PB3)
        MainWindow2.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "灯光故障诊断系统"))
        self.PB1.setText(_translate("MainWindow2", "   故障诊断   "))
        self.PB2.setText(_translate("MainWindow2", "  知识库管理  "))
        self.PB5.setText(_translate("MainWindow2", "   故障记录   "))
        self.PB4.setText(_translate("MainWindow2", "   系统设置   "))
        self.PB3.setText(_translate("MainWindow2", "     退出     "))
import img_rc
