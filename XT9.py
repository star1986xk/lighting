# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XT9.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow9(object):
    def setupUi(self, MainWindow9):
        MainWindow9.setObjectName("MainWindow9")
        MainWindow9.resize(821, 405)
        MainWindow9.setStyleSheet("#centralwidget{\n"
"border-image: url(:/新前缀/img/bg.jpg);\n"
"}\n"
"QLabel{\n"
"color:#ffffff;\n"
"}\n"
"QPushButton{\n"
"padding:2px 2px 2px 2px;\n"
"background-color: rgba(255,255,255,0);\n"
"border-style:none;\n"
"color:#ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"padding:2px 2px 2px 2px;\n"
"background-color: rgba(220, 220, 220,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding:2px 2px 2px 2px;\n"
"    /* 改变背景色 */  \n"
"    background-color:rgba(180, 180, 180,10);  \n"
"    /* 改变边框风格 */  \n"
"    border-style:inset;  \n"
"    /* 使文字有一点移动 */\n"
"    padding-left:1px;\n"
"    padding-top:1px;\n"
"}\n"
"\n"
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
"}\n"
"#widget{\n"
"    border-radius:10px;\n"
"    background-color: rgba(255, 255, 255,50);\n"
"}\n"
"#widget_3,#widget_6{\n"
"    border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"    background-color: rgba(255, 255, 255,50);\n"
"}\n"
"#widget_2,#widget_5{\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 36, 48,200), stop:1 rgba(20, 36, 48,0));\n"
"}\n"
"#page_1,#page_2,#page_3,#page_4{\n"
"    border-bottom-right-radius:10px;\n"
"    background-color: rgba(80, 80, 80,150);\n"
"}\n"
"QTableWidget{\n"
"    background-color: rgba(80, 80, 80,150);\n"
"    color:#ffffff;\n"
"}\n"
"QHeaderView{\n"
"    background-color: rgba(80, 80, 80,150);     \n"
"}\n"
"QHeaderView::section{\n"
"border:none;\n"
"border-right:1px solid rgba(0,0,0,100);\n"
"background-color: rgba(80, 80, 80,150);\n"
"color:#ffffff;\n"
"}\n"
"QListWidget{\n"
"padding:2px 2px 2px 2px;\n"
"border-radius:5px;\n"
"background-color: rgba(255, 255, 255,200);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow9)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 20, 0, 20)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.PB91 = QtWidgets.QPushButton(self.widget)
        self.PB91.setMinimumSize(QtCore.QSize(80, 25))
        self.PB91.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB91.setFont(font)
        self.PB91.setObjectName("PB91")
        self.verticalLayout_3.addWidget(self.PB91)
        self.PB92 = QtWidgets.QPushButton(self.widget)
        self.PB92.setMinimumSize(QtCore.QSize(80, 25))
        self.PB92.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB92.setFont(font)
        self.PB92.setObjectName("PB92")
        self.verticalLayout_3.addWidget(self.PB92)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.PB911 = QtWidgets.QPushButton(self.widget)
        self.PB911.setMinimumSize(QtCore.QSize(80, 25))
        self.PB911.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB911.setFont(font)
        self.PB911.setObjectName("PB911")
        self.verticalLayout_3.addWidget(self.PB911)
        self.horizontalLayout.addWidget(self.widget)
        self.stk91 = QtWidgets.QStackedWidget(self.centralwidget)
        self.stk91.setObjectName("stk91")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.page_5)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setContentsMargins(15, -1, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.page_5)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.PB93 = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB93.sizePolicy().hasHeightForWidth())
        self.PB93.setSizePolicy(sizePolicy)
        self.PB93.setMinimumSize(QtCore.QSize(80, 25))
        self.PB93.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB93.setFont(font)
        self.PB93.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PB93.setObjectName("PB93")
        self.verticalLayout_5.addWidget(self.PB93)
        self.PB94 = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB94.sizePolicy().hasHeightForWidth())
        self.PB94.setSizePolicy(sizePolicy)
        self.PB94.setMinimumSize(QtCore.QSize(80, 25))
        self.PB94.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB94.setFont(font)
        self.PB94.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PB94.setObjectName("PB94")
        self.verticalLayout_5.addWidget(self.PB94)
        self.PB95 = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB95.sizePolicy().hasHeightForWidth())
        self.PB95.setSizePolicy(sizePolicy)
        self.PB95.setMinimumSize(QtCore.QSize(80, 25))
        self.PB95.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB95.setFont(font)
        self.PB95.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PB95.setObjectName("PB95")
        self.verticalLayout_5.addWidget(self.PB95)
        self.PB96 = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB96.sizePolicy().hasHeightForWidth())
        self.PB96.setSizePolicy(sizePolicy)
        self.PB96.setMinimumSize(QtCore.QSize(80, 25))
        self.PB96.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB96.setFont(font)
        self.PB96.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PB96.setObjectName("PB96")
        self.verticalLayout_5.addWidget(self.PB96)
        self.horizontalLayout_5.addWidget(self.widget_4)
        self.stk92 = QtWidgets.QStackedWidget(self.widget_3)
        self.stk92.setObjectName("stk92")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_17 = QtWidgets.QLabel(self.page_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.tableWidget = QtWidgets.QTableWidget(self.page_1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.stk92.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.widget_10 = QtWidgets.QWidget(self.page_2)
        self.widget_10.setObjectName("widget_10")
        self.label_2 = QtWidgets.QLabel(self.widget_10)
        self.label_2.setGeometry(QtCore.QRect(200, 20, 80, 16))
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_10)
        self.lineEdit.setGeometry(QtCore.QRect(289, 17, 200, 25))
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_8.addWidget(self.widget_10)
        self.widget_11 = QtWidgets.QWidget(self.page_2)
        self.widget_11.setObjectName("widget_11")
        self.label_5 = QtWidgets.QLabel(self.widget_11)
        self.label_5.setGeometry(QtCore.QRect(200, 20, 80, 16))
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.widget_11)
        self.comboBox.setGeometry(QtCore.QRect(289, 17, 200, 25))
        self.comboBox.setMinimumSize(QtCore.QSize(200, 25))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_8.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.page_2)
        self.widget_12.setObjectName("widget_12")
        self.label_3 = QtWidgets.QLabel(self.widget_12)
        self.label_3.setGeometry(QtCore.QRect(200, 20, 80, 16))
        self.label_3.setMinimumSize(QtCore.QSize(80, 0))
        self.label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_12)
        self.lineEdit_2.setGeometry(QtCore.QRect(289, 17, 200, 25))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_8.addWidget(self.widget_12)
        self.widget_14 = QtWidgets.QWidget(self.page_2)
        self.widget_14.setObjectName("widget_14")
        self.label_4 = QtWidgets.QLabel(self.widget_14)
        self.label_4.setGeometry(QtCore.QRect(200, 20, 80, 16))
        self.label_4.setMinimumSize(QtCore.QSize(80, 0))
        self.label_4.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_14)
        self.lineEdit_3.setGeometry(QtCore.QRect(289, 17, 200, 25))
        self.lineEdit_3.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_8.addWidget(self.widget_14)
        self.widget_15 = QtWidgets.QWidget(self.page_2)
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem1 = QtWidgets.QSpacerItem(490, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.PB97 = QtWidgets.QPushButton(self.widget_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB97.sizePolicy().hasHeightForWidth())
        self.PB97.setSizePolicy(sizePolicy)
        self.PB97.setMinimumSize(QtCore.QSize(80, 25))
        self.PB97.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB97.setFont(font)
        self.PB97.setObjectName("PB97")
        self.horizontalLayout_14.addWidget(self.PB97)
        self.verticalLayout_8.addWidget(self.widget_15)
        self.stk92.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_9.addWidget(self.label_12)
        self.widget_13 = QtWidgets.QWidget(self.page_3)
        self.widget_13.setObjectName("widget_13")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_13)
        self.lineEdit_6.setGeometry(QtCore.QRect(289, 17, 200, 25))
        self.lineEdit_6.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.widget_13)
        self.label_7.setGeometry(QtCore.QRect(200, 20, 80, 16))
        self.label_7.setMinimumSize(QtCore.QSize(80, 0))
        self.label_7.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.widget_13)
        self.widget_16 = QtWidgets.QWidget(self.page_3)
        self.widget_16.setObjectName("widget_16")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_16)
        self.lineEdit_7.setGeometry(QtCore.QRect(289, 17, 200, 25))
        self.lineEdit_7.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.widget_16)
        self.label_8.setGeometry(QtCore.QRect(200, 20, 80, 16))
        self.label_8.setMinimumSize(QtCore.QSize(80, 0))
        self.label_8.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.widget_16)
        self.widget_17 = QtWidgets.QWidget(self.page_3)
        self.widget_17.setObjectName("widget_17")
        self.label_6 = QtWidgets.QLabel(self.widget_17)
        self.label_6.setGeometry(QtCore.QRect(200, 20, 80, 16))
        self.label_6.setMinimumSize(QtCore.QSize(80, 0))
        self.label_6.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_17)
        self.lineEdit_5.setGeometry(QtCore.QRect(289, 17, 200, 25))
        self.lineEdit_5.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_9.addWidget(self.widget_17)
        self.widget_18 = QtWidgets.QWidget(self.page_3)
        self.widget_18.setObjectName("widget_18")
        self.label_9 = QtWidgets.QLabel(self.widget_18)
        self.label_9.setGeometry(QtCore.QRect(200, 20, 80, 16))
        self.label_9.setMinimumSize(QtCore.QSize(80, 0))
        self.label_9.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_18)
        self.lineEdit_4.setGeometry(QtCore.QRect(289, 17, 200, 25))
        self.lineEdit_4.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_9.addWidget(self.widget_18)
        self.widget_19 = QtWidgets.QWidget(self.page_3)
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_19)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem2 = QtWidgets.QSpacerItem(490, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_6.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_13.addWidget(self.pushButton_6)
        self.verticalLayout_9.addWidget(self.widget_19)
        self.stk92.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 15)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.page_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13)
        self.widget_20 = QtWidgets.QWidget(self.page_4)
        self.widget_20.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_20.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_20.setObjectName("widget_20")
        self.label_19 = QtWidgets.QLabel(self.widget_20)
        self.label_19.setGeometry(QtCore.QRect(200, 20, 80, 16))
        self.label_19.setMinimumSize(QtCore.QSize(80, 0))
        self.label_19.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_20)
        self.comboBox_2.setGeometry(QtCore.QRect(289, 17, 200, 25))
        self.comboBox_2.setMinimumSize(QtCore.QSize(200, 25))
        self.comboBox_2.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_10.addWidget(self.widget_20)
        self.widget_21 = QtWidgets.QWidget(self.page_4)
        self.widget_21.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_21.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_21.setObjectName("widget_21")
        self.label_15 = QtWidgets.QLabel(self.widget_21)
        self.label_15.setGeometry(QtCore.QRect(200, 20, 80, 16))
        self.label_15.setMinimumSize(QtCore.QSize(80, 0))
        self.label_15.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget_21)
        self.lineEdit_9.setGeometry(QtCore.QRect(289, 17, 200, 25))
        self.lineEdit_9.setMinimumSize(QtCore.QSize(200, 25))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_10.addWidget(self.widget_21)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem3)
        self.widget_22 = QtWidgets.QWidget(self.page_4)
        self.widget_22.setObjectName("widget_22")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_22)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(490, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_7.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.verticalLayout_10.addWidget(self.widget_22)
        self.stk92.addWidget(self.page_4)
        self.horizontalLayout_5.addWidget(self.stk92)
        self.verticalLayout.addWidget(self.widget_3)
        self.stk91.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_5 = QtWidgets.QWidget(self.page_6)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setContentsMargins(15, -1, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.verticalLayout_4.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.page_6)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_7 = QtWidgets.QWidget(self.widget_6)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_16 = QtWidgets.QLabel(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_9.addWidget(self.label_16)
        self.label_18 = QtWidgets.QLabel(self.widget_7)
        self.label_18.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_9.addWidget(self.label_18)
        self.verticalLayout_7.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_6)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.listWidget = QtWidgets.QListWidget(self.widget_8)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout_10.addWidget(self.listWidget)
        self.widget_9 = QtWidgets.QWidget(self.widget_8)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.PB98 = QtWidgets.QPushButton(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB98.sizePolicy().hasHeightForWidth())
        self.PB98.setSizePolicy(sizePolicy)
        self.PB98.setMinimumSize(QtCore.QSize(100, 25))
        self.PB98.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB98.setFont(font)
        self.PB98.setObjectName("PB98")
        self.verticalLayout_6.addWidget(self.PB98)
        self.PB99 = QtWidgets.QPushButton(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB99.sizePolicy().hasHeightForWidth())
        self.PB99.setSizePolicy(sizePolicy)
        self.PB99.setMinimumSize(QtCore.QSize(100, 25))
        self.PB99.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB99.setFont(font)
        self.PB99.setObjectName("PB99")
        self.verticalLayout_6.addWidget(self.PB99)
        self.PB910 = QtWidgets.QPushButton(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB910.sizePolicy().hasHeightForWidth())
        self.PB910.setSizePolicy(sizePolicy)
        self.PB910.setMinimumSize(QtCore.QSize(100, 25))
        self.PB910.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PB910.setFont(font)
        self.PB910.setObjectName("PB910")
        self.verticalLayout_6.addWidget(self.PB910)
        self.horizontalLayout_10.addWidget(self.widget_9)
        self.verticalLayout_7.addWidget(self.widget_8)
        self.verticalLayout_4.addWidget(self.widget_6)
        self.stk91.addWidget(self.page_6)
        self.horizontalLayout.addWidget(self.stk91)
        MainWindow9.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow9)
        self.stk91.setCurrentIndex(0)
        self.stk92.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow9)

    def retranslateUi(self, MainWindow9):
        _translate = QtCore.QCoreApplication.translate
        MainWindow9.setWindowTitle(_translate("MainWindow9", "MainWindow"))
        self.PB91.setText(_translate("MainWindow9", "用户管理"))
        self.PB92.setText(_translate("MainWindow9", "系统管理"))
        self.PB911.setText(_translate("MainWindow9", "退出"))
        self.label.setText(_translate("MainWindow9", "用户管理"))
        self.PB93.setText(_translate("MainWindow9", "用户列表"))
        self.PB94.setText(_translate("MainWindow9", "新增用户"))
        self.PB95.setText(_translate("MainWindow9", "修改密码"))
        self.PB96.setText(_translate("MainWindow9", "删除用户"))
        self.label_17.setText(_translate("MainWindow9", "用户列表"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow9", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow9", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow9", "用户权限"))
        self.label_11.setText(_translate("MainWindow9", "新增用户"))
        self.label_2.setText(_translate("MainWindow9", "用户名"))
        self.label_5.setText(_translate("MainWindow9", "用户权限"))
        self.label_3.setText(_translate("MainWindow9", "密  码"))
        self.label_4.setText(_translate("MainWindow9", "确认密码"))
        self.PB97.setText(_translate("MainWindow9", "确定"))
        self.label_12.setText(_translate("MainWindow9", "修改密码"))
        self.label_7.setText(_translate("MainWindow9", "用户名"))
        self.label_8.setText(_translate("MainWindow9", "旧密码"))
        self.label_6.setText(_translate("MainWindow9", "密  码"))
        self.label_9.setText(_translate("MainWindow9", "确认密码"))
        self.pushButton_6.setText(_translate("MainWindow9", "确定"))
        self.label_13.setText(_translate("MainWindow9", "删除用户"))
        self.label_19.setText(_translate("MainWindow9", "用户名"))
        self.label_15.setText(_translate("MainWindow9", "密  码"))
        self.pushButton_7.setText(_translate("MainWindow9", "确定"))
        self.label_10.setText(_translate("MainWindow9", "系统管理"))
        self.label_16.setText(_translate("MainWindow9", "当前系统:"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow9", "所有系统:"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.PB98.setText(_translate("MainWindow9", " 添加新系统 "))
        self.PB99.setText(_translate("MainWindow9", "更改系统名称"))
        self.PB910.setText(_translate("MainWindow9", "删除"))
import img_rc
