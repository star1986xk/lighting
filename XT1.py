# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XT1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 871)
        MainWindow.setStyleSheet("#centralwidget{\n"
"border-image: url(:/新前缀/img/bg.jpg);\n"
"}\n"
"QLabel{\n"
"color:#ffffff;\n"
"}\n"
"QPushButton{\n"
"padding:2px 2px 2px 2px;\n"
"background-color: rgba(255,255,255,100);\n"
"border-style:none;\n"
"border-radius: 5px;\n"
"color:#ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"padding:2px 2px 2px 2px;\n"
"background-color: rgba(220, 220, 220,200);\n"
"border-radius: 5px;\n"
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
"    border-radius: 5px;\n"
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
"QTabWidget::pane{\n"
"border:none;\n"
"border-top:1px solid rgba(150,150,150,200);\n"
"}\n"
"#tab,#tab_2{\n"
"background-color: rgba(255, 255, 255,0);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"     left: 5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"     background: gray;\n"
"     border-bottom-color: #C2C7CB;\n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     min-width: 60px;\n"
"    height:25px;\n"
"    font: 11pt;\n"
"     padding: 2px;\n"
"margin-right:4px;\n"
"background-color: rgba(71,87,100,0);\n"
"color:rgb(180,180,180);\n"
" }\n"
"/*选中teble背景色*/\n"
"QTabBar::tab:selected{\n"
"background-color: rgba(50,66,78,220);\n"
"color:#ffffff;\n"
"}\n"
"#widget_A,#widget_B,#widget_E,#widget_F{\n"
"border-radius:20px;\n"
"    background-color: rgba(255, 255, 255,20);\n"
"}\n"
"#widget_A_1,#widget_B_1,#widget_C_1,#widget_D_1,#widget_E_1,#widget_F_1,#widget_G_1,#widget_H_1{\n"
"border-top-left-radius:20px;\n"
"border-top-right-radius:20px;\n"
"background-color: rgba(20, 36, 48,150);\n"
"}\n"
"QTextBrowser{\n"
"    padding:2px 2px 2px 2px;\n"
"    border-radius:5px;\n"
"    background-color: rgba(255, 255, 255,200);\n"
"}\n"
"QListWidget{\n"
"padding:2px 2px 2px 2px;\n"
"border-radius:5px;\n"
"background-color: rgba(255, 255, 255,200);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_A = QtWidgets.QWidget(self.tab_2)
        self.widget_A.setObjectName("widget_A")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_A)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_A_1 = QtWidgets.QWidget(self.widget_A)
        self.widget_A_1.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_A_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_A_1.setObjectName("widget_A_1")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_A_1)
        self.horizontalLayout_9.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.widget_A_1)
        self.label_8.setMinimumSize(QtCore.QSize(100, 0))
        self.label_8.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8, 0, QtCore.Qt.AlignLeft)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.verticalLayout_4.addWidget(self.widget_A_1)
        self.widget_2 = QtWidgets.QWidget(self.widget_A)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_2.setObjectName("widget_2")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(133, 5, 150, 16))
        self.label_9.setMinimumSize(QtCore.QSize(150, 0))
        self.label_9.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.comboBox_1 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_1.setGeometry(QtCore.QRect(320, 2, 200, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_1.sizePolicy().hasHeightForWidth())
        self.comboBox_1.setSizePolicy(sizePolicy)
        self.comboBox_1.setMinimumSize(QtCore.QSize(200, 25))
        self.comboBox_1.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_1.setFont(font)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.verticalLayout_4.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget_A)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_3.setObjectName("widget_3")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(133, 5, 150, 16))
        self.label_10.setMinimumSize(QtCore.QSize(150, 0))
        self.label_10.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 2, 200, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMinimumSize(QtCore.QSize(200, 25))
        self.comboBox_2.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.verticalLayout_4.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_A)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_4.setObjectName("widget_4")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_3.setGeometry(QtCore.QRect(320, 2, 200, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setMinimumSize(QtCore.QSize(200, 25))
        self.comboBox_3.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.verticalLayout_4.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_A)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_5.setObjectName("widget_5")
        self.label_12 = QtWidgets.QLabel(self.widget_5)
        self.label_12.setGeometry(QtCore.QRect(133, 0, 350, 30))
        self.label_12.setMinimumSize(QtCore.QSize(350, 30))
        self.label_12.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget_A)
        self.widget_B = QtWidgets.QWidget(self.tab_2)
        self.widget_B.setObjectName("widget_B")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_B)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_B_1 = QtWidgets.QWidget(self.widget_B)
        self.widget_B_1.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_B_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_B_1.setObjectName("widget_B_1")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_B_1)
        self.horizontalLayout_10.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.widget_B_1)
        self.label_11.setMinimumSize(QtCore.QSize(100, 0))
        self.label_11.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11, 0, QtCore.Qt.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.widget_B_1)
        self.widget = QtWidgets.QWidget(self.widget_B)
        self.widget.setMinimumSize(QtCore.QSize(0, 100))
        self.widget.setObjectName("widget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_1.setStyleSheet("")
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.horizontalLayout_11.addWidget(self.textBrowser_1)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.PBkszd = QtWidgets.QPushButton(self.widget_6)
        self.PBkszd.setMinimumSize(QtCore.QSize(80, 25))
        self.PBkszd.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PBkszd.setFont(font)
        self.PBkszd.setObjectName("PBkszd")
        self.verticalLayout_6.addWidget(self.PBkszd)
        self.PByjcz = QtWidgets.QPushButton(self.widget_6)
        self.PByjcz.setMinimumSize(QtCore.QSize(80, 25))
        self.PByjcz.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PByjcz.setFont(font)
        self.PByjcz.setObjectName("PByjcz")
        self.verticalLayout_6.addWidget(self.PByjcz)
        self.horizontalLayout_11.addWidget(self.widget_6)
        self.verticalLayout_5.addWidget(self.widget)
        self.verticalLayout.addWidget(self.widget_B)
        self.widget_7 = QtWidgets.QWidget(self.tab_2)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_C = QtWidgets.QWidget(self.widget_7)
        self.widget_C.setObjectName("widget_C")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_C)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_C_1 = QtWidgets.QWidget(self.widget_C)
        self.widget_C_1.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_C_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_C_1.setObjectName("widget_C_1")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_C_1)
        self.horizontalLayout_12.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.widget_C_1)
        self.label_13.setMinimumSize(QtCore.QSize(100, 0))
        self.label_13.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13, 0, QtCore.Qt.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        self.verticalLayout_8.addWidget(self.widget_C_1)
        self.listWidget_2 = QtWidgets.QListWidget(self.widget_C)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_8.addWidget(self.listWidget_2)
        self.horizontalLayout_4.addWidget(self.widget_C)
        self.widget_D = QtWidgets.QWidget(self.widget_7)
        self.widget_D.setObjectName("widget_D")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_D)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_D_1 = QtWidgets.QWidget(self.widget_D)
        self.widget_D_1.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_D_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_D_1.setObjectName("widget_D_1")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_D_1)
        self.horizontalLayout_13.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.widget_D_1)
        self.label_14.setMinimumSize(QtCore.QSize(100, 0))
        self.label_14.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14, 0, QtCore.Qt.AlignLeft)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.verticalLayout_9.addWidget(self.widget_D_1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.widget_D)
        self.textBrowser_3.setStyleSheet("")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_9.addWidget(self.textBrowser_3)
        self.horizontalLayout_4.addWidget(self.widget_D)
        self.verticalLayout.addWidget(self.widget_7)
        self.widget_B_2 = QtWidgets.QWidget(self.tab_2)
        self.widget_B_2.setObjectName("widget_B_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_B_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout.addWidget(self.widget_B_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.PBlr = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBlr.sizePolicy().hasHeightForWidth())
        self.PBlr.setSizePolicy(sizePolicy)
        self.PBlr.setMinimumSize(QtCore.QSize(80, 25))
        self.PBlr.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PBlr.setFont(font)
        self.PBlr.setObjectName("PBlr")
        self.horizontalLayout_5.addWidget(self.PBlr)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.PBtc = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBtc.sizePolicy().hasHeightForWidth())
        self.PBtc.setSizePolicy(sizePolicy)
        self.PBtc.setMinimumSize(QtCore.QSize(80, 25))
        self.PBtc.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PBtc.setFont(font)
        self.PBtc.setObjectName("PBtc")
        self.horizontalLayout_5.addWidget(self.PBtc)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_E = QtWidgets.QWidget(self.tab)
        self.widget_E.setObjectName("widget_E")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_E)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.widget_E_1 = QtWidgets.QWidget(self.widget_E)
        self.widget_E_1.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_E_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_E_1.setObjectName("widget_E_1")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_E_1)
        self.horizontalLayout_14.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_15 = QtWidgets.QLabel(self.widget_E_1)
        self.label_15.setMinimumSize(QtCore.QSize(100, 0))
        self.label_15.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_14.addWidget(self.label_15, 0, QtCore.Qt.AlignLeft)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem15)
        self.verticalLayout_10.addWidget(self.widget_E_1)
        self.widget_8 = QtWidgets.QWidget(self.widget_E)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget_8)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_2.setMinimumSize(QtCore.QSize(60, 25))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_10.addWidget(self.widget_8)
        self.verticalLayout_3.addWidget(self.widget_E)
        self.widget_F = QtWidgets.QWidget(self.tab)
        self.widget_F.setObjectName("widget_F")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_F)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.widget_F_1 = QtWidgets.QWidget(self.widget_F)
        self.widget_F_1.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_F_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_F_1.setObjectName("widget_F_1")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_F_1)
        self.horizontalLayout_15.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.widget_F_1)
        self.label_16.setMinimumSize(QtCore.QSize(100, 0))
        self.label_16.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16, 0, QtCore.Qt.AlignLeft)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem16)
        self.verticalLayout_11.addWidget(self.widget_F_1)
        self.widget_9 = QtWidgets.QWidget(self.widget_F)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_9)
        self.label_4.setMinimumSize(QtCore.QSize(0, 25))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.widget_9)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.label_5 = QtWidgets.QLabel(self.widget_9)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget_9)
        self.comboBox_4.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_4.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_3.addWidget(self.comboBox_4)
        self.verticalLayout_11.addWidget(self.widget_9)
        self.verticalLayout_3.addWidget(self.widget_F)
        self.widget_10 = QtWidgets.QWidget(self.tab)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_G = QtWidgets.QWidget(self.widget_10)
        self.widget_G.setObjectName("widget_G")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_G)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.widget_G_1 = QtWidgets.QWidget(self.widget_G)
        self.widget_G_1.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_G_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_G_1.setObjectName("widget_G_1")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_G_1)
        self.horizontalLayout_16.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_17 = QtWidgets.QLabel(self.widget_G_1)
        self.label_17.setMinimumSize(QtCore.QSize(100, 0))
        self.label_17.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_16.addWidget(self.label_17, 0, QtCore.Qt.AlignLeft)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem17)
        self.verticalLayout_12.addWidget(self.widget_G_1)
        self.listWidget = QtWidgets.QListWidget(self.widget_G)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_12.addWidget(self.listWidget)
        self.horizontalLayout_6.addWidget(self.widget_G)
        self.widget_H = QtWidgets.QWidget(self.widget_10)
        self.widget_H.setObjectName("widget_H")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_H)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.widget_H_1 = QtWidgets.QWidget(self.widget_H)
        self.widget_H_1.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_H_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_H_1.setObjectName("widget_H_1")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget_H_1)
        self.horizontalLayout_17.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_18 = QtWidgets.QLabel(self.widget_H_1)
        self.label_18.setMinimumSize(QtCore.QSize(100, 0))
        self.label_18.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_17.addWidget(self.label_18, 0, QtCore.Qt.AlignLeft)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem18)
        self.verticalLayout_13.addWidget(self.widget_H_1)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_H)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_13.addWidget(self.textBrowser)
        self.horizontalLayout_6.addWidget(self.widget_H)
        self.verticalLayout_3.addWidget(self.widget_10)
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "故障范围选择"))
        self.label_9.setText(_translate("MainWindow", "请选择故障发生阶段:"))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "--请选择--"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "开机阶段"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "使用阶段"))
        self.label_10.setText(_translate("MainWindow", "请选择故障范围:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "--请选择--"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "--请选择--"))
        self.label_12.setText(_translate("MainWindow", "提示:若无二级故障范围可选，可直接开始诊断"))
        self.label_11.setText(_translate("MainWindow", "诊断步骤"))
        self.textBrowser_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.PBkszd.setText(_translate("MainWindow", "   开始诊断   "))
        self.PByjcz.setText(_translate("MainWindow", "应急处置"))
        self.label_13.setText(_translate("MainWindow", "诊断结果"))
        self.label_14.setText(_translate("MainWindow", "诊断建议"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.PBlr.setText(_translate("MainWindow", "     录入     "))
        self.PBtc.setText(_translate("MainWindow", "     退出     "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "故障诊断"))
        self.label_15.setText(_translate("MainWindow", "故障检索"))
        self.pushButton.setText(_translate("MainWindow", "检索"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))
        self.label_16.setText(_translate("MainWindow", "检索范围"))
        self.label_4.setText(_translate("MainWindow", "故障阶段选择"))
        self.label_5.setText(_translate("MainWindow", "检索内容"))
        self.label_17.setText(_translate("MainWindow", "检索结果"))
        self.label_18.setText(_translate("MainWindow", "故障说明"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "故障检索"))
import img_rc
