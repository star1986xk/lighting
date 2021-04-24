# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XT3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3):
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(597, 344)
        MainWindow3.setStyleSheet("#centralwidget{\n"
"border-radius:20px;\n"
"border-image: url(:/新前缀/img/bg.jpg);\n"
"}\n"
"QLabel{\n"
"color:#ffffff;\n"
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
"    padding:2px 2px 2px 2px;\n"
"    /* 改变背景色 */  \n"
"    background-color:rgba(180, 180, 180,100);  \n"
"    /* 改变边框风格 */  \n"
"    border-style:inset;  \n"
"    /* 使文字有一点移动 */\n"
"    padding-left:1px;\n"
"    padding-top:1px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#pushButton_close{\n"
"background-color:rgba(180, 180, 180,0);  \n"
"padding:2px 2px 2px 2px;\n"
"border-style:none;\n"
"border-radius: 3px;\n"
"color:#ffffff;\n"
"image: url(:/新前缀/img/关闭.png);\n"
"}\n"
"\n"
"#pushButton_close:hover{\n"
"background-color:rgba(180, 180, 180,50);  \n"
"padding:2px 2px 2px 2px;\n"
"border-radius: 3px;\n"
"image: url(:/新前缀/img/关闭1.png);\n"
"}\n"
"\n"
"#pushButton_close:pressed {\n"
"background-color:rgba(180, 180, 180,0);  \n"
"    padding:2px 2px 2px 2px;\n"
"    /* 改变边框风格 */  \n"
"    border-style:inset;  \n"
"    /* 使文字有一点移动 */\n"
"    padding-left:1px;\n"
"    padding-top:1px;\n"
"    border-radius: 3px;\n"
"}\n"
"QLineEdit{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border: 1px solid #000000;\n"
"border-radius:3px;\n"
"color:#ffffff;\n"
"padding-left: 5px;\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    border:1px solid rgba(31,156,220) ;\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgba(255, 255, 255,120);\n"
"border: 1px solid #000000;\n"
"border-radius:3px;\n"
"color:#ffffff;\n"
"padding-left: 5px;\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"    border:1px solid rgba(30,150,220);\n"
"}\n"
"/*点击combox的样式*/\n"
"QComboBox:on\n"
"{\n"
"    border-radius:3px;\n"
"    background-color: rgba(255, 255, 255,120);\n"
"    color:rgb(255,255,255);\n"
"    border:1px solid rgba(30,150,220);\n"
"}\n"
"/*下拉框的样式*/\n"
"QComboBox QAbstractItemView \n"
"{\n"
"    outline: 0px solid gray;  /*取消选中虚线*/\n"
"    border:1px solid rgba(30,150,220);\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgba(255, 255, 255,120);\n"
"    selection-background-color: rgb(90,90,90);   \n"
"}\n"
" /*选中每一项高度*/\n"
"QComboBox QAbstractItemView::item\n"
" { \n"
"    height: 40px;  \n"
" }\n"
"/*选中每一项的字体颜色和背景颜色*/\n"
"QComboBox QAbstractItemView::item:selected \n"
"{\n"
"    color: rgb(31,163,246);\n"
"    background-color: rgb(90,90,90); \n"
"}\n"
" /*下拉箭头的边框*/\n"
"QComboBox::drop-down \n"
"{\n"
"    border:none;\n"
"}\n"
" /*下拉箭头样式*/\n"
"QComboBox::down-arrow \n"
"{\n"
"    right:10px;/*控制箭头左右偏移*/\n"
"    width: 9px;  \n"
"    height: 9px;   \n"
"    image: url(:/新前缀/img/下箭头.png);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 10, 20, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_close = QtWidgets.QPushButton(self.widget)
        self.pushButton_close.setMinimumSize(QtCore.QSize(24, 24))
        self.pushButton_close.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_close.setText("")
        self.pushButton_close.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.verticalLayout.addWidget(self.widget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.LEyhm = QtWidgets.QLineEdit(self.widget_2)
        self.LEyhm.setMinimumSize(QtCore.QSize(200, 25))
        self.LEyhm.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LEyhm.setFont(font)
        self.LEyhm.setObjectName("LEyhm")
        self.horizontalLayout_2.addWidget(self.LEyhm)
        self.verticalLayout.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setMinimumSize(QtCore.QSize(80, 0))
        self.label_4.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.LEmm = QtWidgets.QLineEdit(self.widget_3)
        self.LEmm.setMinimumSize(QtCore.QSize(200, 25))
        self.LEmm.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LEmm.setFont(font)
        self.LEmm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LEmm.setObjectName("LEmm")
        self.horizontalLayout_4.addWidget(self.LEmm)
        self.verticalLayout.addWidget(self.widget_3, 0, QtCore.Qt.AlignHCenter)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.cbox = QtWidgets.QComboBox(self.widget_4)
        self.cbox.setMinimumSize(QtCore.QSize(200, 25))
        self.cbox.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cbox.setFont(font)
        self.cbox.setObjectName("cbox")
        self.horizontalLayout_5.addWidget(self.cbox)
        self.verticalLayout.addWidget(self.widget_4, 0, QtCore.Qt.AlignHCenter)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setSpacing(80)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.PB0_1 = QtWidgets.QPushButton(self.widget_5)
        self.PB0_1.setMinimumSize(QtCore.QSize(80, 25))
        self.PB0_1.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB0_1.setFont(font)
        self.PB0_1.setObjectName("PB0_1")
        self.horizontalLayout_6.addWidget(self.PB0_1)
        self.PB0_2 = QtWidgets.QPushButton(self.widget_5)
        self.PB0_2.setMinimumSize(QtCore.QSize(80, 25))
        self.PB0_2.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB0_2.setFont(font)
        self.PB0_2.setObjectName("PB0_2")
        self.horizontalLayout_6.addWidget(self.PB0_2)
        self.verticalLayout.addWidget(self.widget_5, 0, QtCore.Qt.AlignHCenter)
        MainWindow3.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow3", "MainWindow"))
        self.label.setText(_translate("MainWindow3", "故障诊断专家系统"))
        self.label_2.setText(_translate("MainWindow3", "用户名:"))
        self.label_4.setText(_translate("MainWindow3", "密  码:"))
        self.label_5.setText(_translate("MainWindow3", "系统选择:"))
        self.PB0_1.setText(_translate("MainWindow3", "登录"))
        self.PB0_2.setText(_translate("MainWindow3", "退出"))
import img_rc
