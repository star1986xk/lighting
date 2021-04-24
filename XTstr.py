from XT1 import Ui_MainWindow
from XT2 import Ui_MainWindow2
from XT3 import Ui_MainWindow3
from XT5 import Ui_MainWindow5
from XT6 import Ui_MainWindow6
from XT7 import Ui_MainWindow7
from XT9 import Ui_MainWindow9

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel, QTreeWidget, QTreeWidgetItem, \
    QLineEdit, QTextEdit, QShortcut
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QFont
import sys
import sqlite3
import string
import time


# 登录页面3
class Window0(QMainWindow, Ui_MainWindow3):
    def __init__(self):
        super(Window0, self).__init__()
        self.setupUi(self)
        self.PB0_1.clicked.connect(self.PB0_1Cao)
        QShortcut(QtGui.QKeySequence(self.tr("Return")), self, self.PB0_1Cao)
        conn = sqlite3.connect("goon.db")
        c = conn.cursor()
        usersql = c.execute("SELECT * FROM user")
        self.user = usersql.fetchall()
        all_xtsql = c.execute("SELECT breakpoint FROM all_xt")
        all_xt = all_xtsql.fetchone()
        for all_xts in all_xt:
            self.cbox.addItem(all_xts)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # 窗口无边框

        self.pushButton_close.clicked.connect(self.close)
        self.PB0_2.clicked.connect(self.close)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False

    def PB0_1Cao(self):
        username = [x[1] for x in self.user]
        password = [y[2] for y in self.user]
        userpass = dict(zip(username, password))
        if self.LEyhm.text() == '' or self.LEmm.text() == '':
            self.lbtip.setText("请输入用户名或密码!")
        else:
            if self.LEyhm.text() in username:
                if userpass[self.LEyhm.text()] == self.LEmm.text():
                    win0.close()
                    win.show()
                else:
                    self.lbtip.setText("用户名或密码错误!")
            else:
                self.lbtip.setText("该用户不存在!")


# 选择页面2
class Window(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super(Window, self).__init__(parent=None)
        self.setupUi(self)
        self.PB1.clicked.connect(self.PB1Cao)
        self.PB3.clicked.connect(self.PB3Cao)
        self.PB2.clicked.connect(self.PB2Cao)
        self.PB5.clicked.connect(self.PB5Cao)
        self.PB4.clicked.connect(self.PB4Cao)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        pic = QtGui.QPixmap("12.jpg")
        painter.drawPixmap(self.rect(), pic)

    def PB1Cao(self):
        win.close()
        win1.show()

    def PB2Cao(self):
        win.close()
        wink.show()

    def PB3Cao(self):
        win.close()
        win0.show()

    def PB4Cao(self):
        win.close()
        wins.show()

    def PB5Cao(self):
        winj.show()


# 诊断页面
class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        conn = sqlite3.connect("goon.db")
        c = conn.cursor()
        xt_name = '灯光设施故障'
        xt0sql = c.execute("select sign,tablename from all_xt where breakpoint='%s'" % xt_name)
        self.xt0 = xt0sql.fetchone()
        xt0ml1sql = c.execute(
            "SELECT x1.breakpoint,x2.breakpoint FROM {0} AS x1 INNER JOIN {0} AS x2 WHERE x2.sign_conn=x1.sign AND x1.sign_conn='{1}'".format(
                self.xt0[1], self.xt0[0]))
        ml1 = xt0ml1sql.fetchall()
        xt0ml2sql = c.execute(
            "SELECT x1.breakpoint,x2.breakpoint FROM {0} AS x1 INNER JOIN {0} AS x2 WHERE x2.sign_conn=x1.sign AND x1.sign_conn!='{1}'".format(
                self.xt0[1], self.xt0[0]))
        ml2 = xt0ml2sql.fetchall()
        self.ZD1 = {}
        self.ZD2 = {}
        for i in range(0, len(ml1)):
            if i == 0 or k != ml1[i][0]:
                self.ZD1.setdefault(ml1[i][0], []).append("--请选择--")
            self.ZD1.setdefault(ml1[i][0], []).append(ml1[i][1])
            k = ml1[i][0]
        for i in range(0, len(ml2)):
            if i == 0 or k != ml2[i][0]:
                self.ZD2.setdefault(ml2[i][0], []).append("--请选择--")
            self.ZD2.setdefault(ml2[i][0], []).append(ml2[i][1])
            k = ml2[i][0]
        super().__init__(parent=None)
        self.setupUi(self)
        self.comboBox_1.currentIndexChanged.connect(self.comboCao1)
        self.comboBox_2.currentIndexChanged.connect(self.comboCao2)
        self.PBkszd.clicked.connect(self.PBkszdCao)
        self.PBtc.clicked.connect(self.PBtcCao)
        self.PBlr.clicked.connect(self.PBlrCao)

    def PBlrCao(self):
        winl.show()


    def comboCao1(self):
        self.comboDX1 = self.comboBox_1.currentText()
        if self.comboDX1 != "--请选择--":
            self.comboBox_2.clear()
            self.comboBox_2.addItems(self.ZD1[self.comboDX1] if self.comboDX1 in self.ZD1.keys() else ["--请选择--"])
        else:
            self.comboBox_2.clear()
            self.comboBox_2.addItem("--请选择--")

    def comboCao2(self):
        self.comboDX2 = self.comboBox_2.currentText()
        if self.comboDX2 != "--请选择--":
            self.comboBox_3.clear()
            self.comboBox_3.addItems(self.ZD2[self.comboDX2] if self.comboDX2 in self.ZD2.keys() else ["--请选择--"])
        else:
            self.comboBox_3.clear()
            self.comboBox_3.addItem("--请选择--")

    def PBkszdCao(self):
        self.textBrowser_1.clear()
        print(1)
        self.listWidget_2.clear()
        print(2)
        self.comboDX3 = self.comboBox_3.currentText()
        if self.comboDX3 == "--请选择--" and not self.ZD2.get(self.comboDX2):
            gjz = self.comboDX2
            self.textBrowser_1.append(self.comboDX1 + "\t" + self.comboDX2)
            self.textBrowser_1.append('👇')
        elif self.comboDX3 != "--请选择--":
            gjz = self.comboDX3
            self.textBrowser_1.append(self.comboDX1 + "\t" + self.comboDX2 + "\t" + self.comboDX3)
            self.textBrowser_1.append('👇')
        else:
            gjz = None
            self.tshowDG()
        if gjz:
            print(3)
            conn = sqlite3.connect("goon.db")
            c = conn.cursor()
            frsql=c.execute("SELECT tablename FROM %s WHERE breakpoint='%s'" % (self.xt0[1],gjz))
            fr=frsql.fetchone()
            self.zbm = fr[0]
            cx2 = c.execute("select rule from %s where id='R1'" % (self.zbm+'_rule'))
            w_1 = cx2.fetchone()
            self.showDG(w_1)

    def showDG(self, w):
        self.xwDG = QDialog()
        self.xwDG.setFixedSize(400, 135)
        self.label = QLabel(self.xwDG)
        self.label.move(50, 30)
        self.label.setText("%s?" % w[0])
        self.btn1 = QPushButton("是", self.xwDG)
        self.btn2 = QPushButton("否", self.xwDG)
        self.btn1.move(70, 80)
        self.btn2.move(230, 80)
        self.xwDG.setWindowTitle("请选择")
        self.xwDG.setWindowModality(Qt.ApplicationModal)
        self.btn1.clicked.connect(self.btn1Cao)
        self.btn2.clicked.connect(self.btn2Cao)
        self.xwDG.exec_()

    def tshowDG(self):
        self.tsDG = QDialog()
        self.tsDG.setFixedSize(400, 135)
        self.label = QLabel(self.tsDG)
        self.label.move(50, 30)
        self.label.setText('请确定搜索范围是否有效！')
        self.btn3 = QPushButton("确定", self.tsDG)
        self.btn3.move(150, 80)
        self.tsDG.setWindowTitle("提示")
        self.tsDG.setWindowModality(Qt.ApplicationModal)
        self.btn3.clicked.connect(self.tsDG.close)
        self.tsDG.exec_()

    def btn1Cao(self):
        self.xwDG.close()
        wt = self.label.text()
        wt = wt.strip(string.punctuation)
        conn = sqlite3.connect("goon.db")
        c = conn.cursor()
        ncx1sql=c.execute("SELECT id FROM %s WHERE rule='%s'" % ((self.zbm+'_rule'),wt))
        ncx1=ncx1sql.fetchone()
        rulere=ncx1[0]+'-1'
        ncx2sql=c.execute("SELECT b1.breakpoint,b2.rule_re FROM {0} as b1 INNER JOIN {0} as b2 WHERE b1.rule_re='{1}' AND b2.sign_conn=b1.sign".format(self.zbm,rulere))
        ncx2=ncx2sql.fetchall()
        if ncx2!=[]:
            self.godate1 = ncx2[0][0]
            ncx2rule = ncx2[0][1]
            ncx2rule=ncx2rule[0:-2]
            ncx3sql = c.execute("SELECT rule FROM %s WHERE id='%s'" % ((self.zbm + '_rule'), ncx2rule))
            w = ncx3sql.fetchone()
            self.textBrowser_1.append('%s\t是\t%s' % (wt,ncx2[0][0]))
            self.textBrowser_1.append('👇')
            self.showDG(w)
        else:
            self.textBrowser_1.append("故障点:"+self.godate1)
            self.listWidget_2.addItem(self.godate1)


    def btn2Cao(self):
        self.xwDG.close()
        wt = self.label.text()
        wt = wt.strip(string.punctuation)
        conn = sqlite3.connect("goon.db")
        c = conn.cursor()
        ncx1sql = c.execute("SELECT id FROM %s WHERE rule='%s'" % ((self.zbm + '_rule'), wt))
        ncx1 = ncx1sql.fetchone()
        rulere = ncx1[0] + '-2'
        ncx2sql = c.execute(
            "SELECT b1.breakpoint,b2.rule_re FROM {0} as b1 INNER JOIN {0} as b2 WHERE b1.rule_re='{1}' AND b2.sign_conn=b1.sign".format(
                self.zbm, rulere))
        ncx2 = ncx2sql.fetchall()
        if ncx2 != []:
            self.godate1 = ncx2[0][0]
            ncx2rule = ncx2[0][1]
            ncx2rule = ncx2rule[0:-2]
            ncx3sql = c.execute("SELECT rule FROM %s WHERE id='%s'" % ((self.zbm + '_rule'), ncx2rule))
            w = ncx3sql.fetchone()
            self.textBrowser_1.append('%s\t否\t%s' % (wt, ncx2[0][0]))
            self.textBrowser_1.append('👇')
            self.showDG(w)
        else:
            self.textBrowser_1.append("故障点:" + self.godate1)
            self.listWidget_2.addItem(self.godate1)

    def PBtcCao(self):
        win1.close()
        win.show()


# 知识管理
class KWindow(QMainWindow, Ui_MainWindow5):
    def __init__(self):
        super(KWindow, self).__init__(parent=None)
        self.setupUi(self)
        conn = sqlite3.connect('goon.db')
        c = conn.cursor()
        xt_name = '灯光设施故障'
        xt0sql = c.execute("select tablename,breakpoint from all_xt where breakpoint='%s'" % xt_name)
        xt0 = xt0sql.fetchone()
        ml0sql = c.execute("select * from {0}".format(xt0[0]))
        ml0tuple = ml0sql.fetchall()
        ml0 = []
        for mli in ml0tuple:
            mlis = list(mli)
            mlis.append('')
            ml0.append(mlis)
        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0, xt0[1])
        for ml0root in ml0:
            if ml0root[2][0] == 'X':
                ml0root[-1] = QTreeWidgetItem(root)
                ml0root[-1].setText(0, ml0root[1])
        for j1 in ml0:
            for j2 in ml0:
                mlml = []
                if j2[2] == j1[0] and j2[3] is None:
                    j2[4] = QTreeWidgetItem(j1[4])
                    j2[4].setText(0, j2[1])
                elif j2[2] == j1[0] and j2[3] is not None:
                    j2[4] = QTreeWidgetItem(j1[4])
                    j2[4].setText(0, j2[1])
                    mlsql = c.execute("select * from {0}".format(j2[3]))
                    ml = mlsql.fetchall()
                    for mls in ml:
                        mlss = list(mls)
                        mlss.append('')
                        mlml.append(mlss)
                    for mlmlroot in mlml:
                        if mlmlroot[2][0] == 'S':
                            mlmlroot[-1] = QTreeWidgetItem(j2[4])
                            mlmlroot[-1].setText(0, mlmlroot[1])
                    for j3 in mlml[1:]:
                        for j4 in mlml:
                            if j4[0] == j3[2]:
                                j3[-1] = QTreeWidgetItem(j4[-1])
                                j3[-1].setText(0, j3[1])
        self.PBzstj.clicked.connect(self.try1Cao)
        self.PBzsxg.clicked.connect(self.try2Cao)
        self.PBzssc.clicked.connect(self.try3Cao)
        self.PBzstc.clicked.connect(self.try4Cao)
        self.qdtj = 0
        self.qdxg = 0
        self.qdsc = 0
        self.treeWidget.expandToDepth(2)

    def try1Cao(self):
        self.onNode = []
        self.qdNode = self.treeWidget.currentItem()
        self.onNode.append(self.qdNode.text(0))
        while True:
            self.qdNode = self.qdNode.parent()
            if self.qdNode is not None:
                self.onNode.append(self.qdNode.text(0))
            else:
                break
        conn = sqlite3.connect('goon.db')
        c = conn.cursor()
        treetopc = c.execute(
            "SELECT tablename,sign FROM all_xt WHERE all_xt.breakpoint = '%s'" % self.onNode[-1])
        treetop = treetopc.fetchone()
        dssql = c.execute("SELECT tablename FROM %s WHERE breakpoint='%s'" % (treetop[0], self.onNode[0]))
        ds = dssql.fetchone()
        if ds == (None,) and 2 < len(self.onNode) < 4:
            self.tjsshow()
        else:
            self.showTJ()

    def try2Cao(self):
        xgNode = self.treeWidget.currentItem().text(0)
        self.showXG(xgNode)

    def try3Cao(self):
        self.qdsc = 1
        self.QRshow()

    def try4Cao(self):
        wink.close()
        win.show()

    def showTJ(self):
        self.zsTJ = QDialog()
        self.zsTJ.setFixedSize(491, 345)
        self.label1 = QLabel(self.zsTJ)
        self.label1.move(20, 275)
        self.label1.setText("提示：如若为中间节点，则无需填写故障说明")
        self.label2 = QLabel(self.zsTJ)
        self.label2.move(20, 15)
        self.label2.setText("请输入新增节点名称")
        self.label3 = QLabel(self.zsTJ)
        self.label3.move(20, 65)
        self.label3.setText("请输入相应故障说明")
        self.PBtjqd = QPushButton("    确定    ", self.zsTJ)
        self.PBtjqd.move(90, 300)
        self.PBtjqx = QPushButton("    取消    ", self.zsTJ)
        self.PBtjqx.move(290, 300)
        self.nodeline = QLineEdit(self.zsTJ)
        self.nodeline.setGeometry(QRect(20, 35, 445, 23))
        self.nodetext = QTextEdit(self.zsTJ)
        self.nodetext.setGeometry(QRect(20, 85, 445, 181))
        self.zsTJ.setWindowTitle("添加")
        self.zsTJ.setWindowModality(Qt.ApplicationModal)
        font = QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label2.setFont(font)
        self.label3.setFont(font)
        self.PBtjqx.clicked.connect(self.zsTJ.close)
        self.PBtjqd.clicked.connect(self.PBtjqdCao)
        self.zsTJ.exec_()

    def PBtjqdCao(self):
        self.qdtj = 1
        self.QRshow()
        self.zsTJ.close()

    def showXG(self, xgNode):
        self.zsXG = QDialog()
        self.zsXG.setFixedSize(491, 345)
        self.label4 = QLabel(self.zsXG)
        self.label4.move(20, 275)
        self.label4.setText("提示：如若为中间节点，则无需填写故障说明")
        self.label5 = QLabel(self.zsXG)
        self.label5.move(20, 15)
        self.label5.setText("请输入修改后节点名称")
        self.label6 = QLabel(self.zsXG)
        self.label6.move(20, 65)
        self.label6.setText("请输入相应故障说明")
        self.PBxgqd = QPushButton("    确定    ", self.zsXG)
        self.PBxgqd.move(90, 300)
        self.PBxgqx = QPushButton("    取消    ", self.zsXG)
        self.PBxgqx.move(290, 300)
        self.nodeline = QLineEdit(self.zsXG)
        self.nodeline.setGeometry(QRect(20, 35, 445, 23))
        self.nodeline.setText('%s' % xgNode)
        self.nodetext = QTextEdit(self.zsXG)
        self.nodetext.setGeometry(QRect(20, 85, 445, 181))
        self.zsXG.setWindowTitle("修改")
        self.zsXG.setWindowModality(Qt.ApplicationModal)
        font = QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label5.setFont(font)
        self.label6.setFont(font)
        self.PBxgqx.clicked.connect(self.zsXG.close)
        self.PBxgqd.clicked.connect(self.PBxgqdCao)
        self.zsXG.exec_()

    def PBxgqdCao(self):
        self.qdxg = 1
        self.QRshow()
        self.zsXG.close()

    def QRshow(self):
        self.QRCK = QDialog()
        self.QRCK.setFixedSize(400, 135)
        qrlabel = QLabel(self.QRCK)
        qrlabel.move(50, 30)
        qrlabel.setText("您确定要进行此操作?")
        qd = QPushButton("是", self.QRCK)
        qx = QPushButton("否", self.QRCK)
        qd.move(70, 80)
        qx.move(230, 80)
        self.QRCK.setWindowTitle("提示")
        self.QRCK.setWindowModality(Qt.ApplicationModal)
        qd.clicked.connect(self.qdCao)
        qx.clicked.connect(self.QRCK.close)
        self.QRCK.exec_()

    def tjsshow(self):
        self.TJSCK = QDialog()
        self.TJSCK.setFixedSize(303, 208)
        tjslabel = QLabel(self.TJSCK)
        tjslabel.move(50, 30)
        tjslabel.setText("请选择您所需要进行的操作:")
        btncj = QPushButton("创建新故障树", self.TJSCK)
        btntjz = QPushButton("添加子节点", self.TJSCK)
        btnqxc = QPushButton("取消", self.TJSCK)
        btncj.move(90, 60)
        btntjz.move(90, 100)
        btnqxc.move(90, 140)
        self.TJSCK.setWindowTitle("提示")
        self.TJSCK.setWindowModality(Qt.ApplicationModal)
        btncj.clicked.connect(self.btncjCao)
        btntjz.clicked.connect(self.btntjzCao)
        btnqxc.clicked.connect(self.TJSCK.close)
        self.TJSCK.exec_()

    def btncjCao(self):
        self.TJSCK.close()
        self.showTJntree()

    def showTJntree(self):
        self.TJntree = QDialog()
        self.TJntree.setFixedSize(400, 145)
        self.label7 = QLabel(self.TJntree)
        self.label7.move(20, 15)
        self.label7.setText("请输入子故障树根节点名称")
        self.PBtjtqd = QPushButton("    确定    ", self.TJntree)
        self.PBtjtqd.move(70, 90)
        self.PBtjtqx = QPushButton("    取消    ", self.TJntree)
        self.PBtjtqx.move(230, 90)
        self.nodeline2 = QLineEdit(self.TJntree)
        self.nodeline2.setGeometry(QRect(20, 40, 350, 23))
        self.TJntree.setWindowTitle("创建子故障树")
        self.TJntree.setWindowModality(Qt.ApplicationModal)
        font = QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label7.setFont(font)
        self.PBtjtqx.clicked.connect(self.TJntree.close)
        self.PBtjtqd.clicked.connect(self.PBtjtqdCao)
        self.TJntree.exec_()

    def PBtjtqdCao(self):
        sNode = self.treeWidget.currentItem()
        addNode = QTreeWidgetItem()
        addNode.setText(0, '%s' % self.nodeline2.text())
        sNode.addChild(addNode)
        conn = sqlite3.connect("goon.db")
        c = conn.cursor()
        newtablesql = c.execute("SELECT count(1) from sqlite_master WHERE type='table'")
        newtable = newtablesql.fetchone()
        c.execute("CREATE TABLE {0}('sign' TEXT,'breakpoint' TEXT,'sign_conn' TEXT)".format("new" + str(newtable[0])))
        conn.commit()
        self.qdCao()
        treetopc = c.execute(
            "SELECT tablename,sign FROM all_xt WHERE all_xt.breakpoint = '%s'" % self.onNode[-1])
        treetop = treetopc.fetchone()
        onsignsql = c.execute("SELECT sign FROM {0} WHERE breakpoint='{1}'".format(treetop[0], self.onNode[0]))
        onsign = onsignsql.fetchone()
        fs = c.execute("SELECT sign FROM %s" % treetop[0])
        fsnum = fs.fetchall()
        Snum = 0
        for fsnums in fsnum:
            if fsnums[0][0] == 'S':
                Snum += 1
        new_sign = "S" + str(Snum + 1)
        c.execute(
            "INSERT INTO {0} (sign,breakpoint,sign_conn,tablename) VALUES('{1}','{2}','{3}','{4}')".format(treetop[0],
                                                                                                           new_sign,
                                                                                                           self.nodeline2.text(),
                                                                                                           onsign[0],
                                                                                                           'new' + str(
                                                                                                               newtable[
                                                                                                                   0])))
        conn.commit()
        c.execute("INSERT INTO addform VALUES('%s','%s','%s','%s')" % (
            new_sign, self.nodeline2.text(), onsign[0], treetop[0]))
        conn.commit()
        self.TJntree.close()

    def btntjzCao(self):
        self.showTJ()
        self.TJSCK.close()

    def qdCao(self):
        self.onNode = []
        self.qdNode = self.treeWidget.currentItem()
        self.onNode.append(self.qdNode.text(0))
        while True:
            self.qdNode = self.qdNode.parent()
            if self.qdNode is not None:
                self.onNode.append(self.qdNode.text(0))
            else:
                break
        if self.qdtj == 1:
            sNode = self.treeWidget.currentItem()
            addNode = QTreeWidgetItem()
            addNode.setText(0, '%s' % self.nodeline.text())
            sNode.addChild(addNode)
            conn = sqlite3.connect('goon.db')
            c = conn.cursor()
            treetopc = c.execute(
                "SELECT tablename,sign FROM all_xt WHERE all_xt.breakpoint = '%s'" % self.onNode[-1])
            treetop = treetopc.fetchone()
            if len(self.onNode) == 1:
                ft = c.execute("SELECT sign FROM %s" % treetop[0])
                ftnum = ft.fetchall()
                Tnum = 0
                for ftnums in ftnum:
                    if ftnums[0][0] == 'T':
                        Tnum += 1
                c.execute(
                    "INSERT INTO %s(sign,breakpoint,sign_conn) VALUES('%s','%s','%s')" % (
                        treetop[0], "T" + str(Tnum + 1), self.nodeline.text(), treetop[1]))
                conn.commit()
                c.execute("INSERT INTO addform VALUES('%s','%s','%s','%s')" % (
                    "T" + str(Tnum + 1), self.nodeline.text(), treetop[1], treetop[0]))
                conn.commit()
            else:
                n = 2
                while n <= len(self.onNode):
                    treetopc2 = c.execute(
                        "SELECT tablename,sign FROM %s WHERE breakpoint = '%s'" % (treetop[0], self.onNode[-n]))
                    treetop2 = treetopc2.fetchone()
                    if treetop2[0] != None:
                        break
                    n += 1
                num_tjc = c.execute("SELECT COUNT(*) FROM addform")
                num_tj = num_tjc.fetchone()
                new_sign = 'G' + str(num_tj[0] + 1)
                if treetop2[0] != None:
                    treeparc = c.execute("SELECT sign FROM %s WHERE breakpoint = '%s'" % (treetop2[0], self.onNode[0]))
                    treepar = treeparc.fetchone()
                    if treepar != None:
                        c.execute(
                            "INSERT INTO %s VALUES('%s','%s','%s')" % (
                                treetop2[0], new_sign, self.nodeline.text(), treepar[0]))
                        conn.commit()
                        c.execute("INSERT INTO addform VALUES('%s','%s','%s','%s')" % (
                            new_sign, self.nodeline.text(), treepar[0], treetop2[0]))
                        conn.commit()
                    else:
                        c.execute(
                            "INSERT INTO %s VALUES('%s','%s','%s')" % (
                                treetop2[0], new_sign, self.nodeline.text(), treetop2[1]))
                        conn.commit()
                        c.execute("INSERT INTO addform VALUES('%s','%s','%s','%s')" % (
                            new_sign, self.nodeline.text(), treetop2[1], treetop2[0]))
                        conn.commit()
                else:
                    treeparc = c.execute("select sign from %s where breakpoint='%s'" % (treetop[0], self.onNode[0]))
                    treepar = treeparc.fetchone()
                    c.execute(
                        "INSERT INTO %s(sign,breakpoint,sign_conn) VALUES('%s','%s','%s')" % (
                            treetop[0], new_sign, self.nodeline.text(), treepar[0]))
                    conn.commit()
                    c.execute("INSERT INTO addform VALUES('%s','%s','%s','%s')" % (
                        new_sign, self.nodeline.text(), treepar[0], treetop[0]))
                    conn.commit()
            self.qdtj = 0
            self.QRCK.close()
        elif self.qdxg == 1:
            gNode = self.treeWidget.currentItem()
            conn = sqlite3.connect('goon.db')
            c = conn.cursor()
            if len(self.onNode) == 1:
                c.execute(
                    "UPDATE all_xt SET breakpoint='%s' WHERE breakpoint='%s'" % (
                        self.nodeline.text(), gNode.text(0)))
            else:
                treetopc = c.execute(
                    "SELECT all_xt.tablename FROM all_xt WHERE all_xt.breakpoint = '%s'" % self.onNode[-1])
                treetop = treetopc.fetchone()
                treetopc2 = c.execute(
                    "SELECT tablename FROM %s WHERE breakpoint = '%s'" % (treetop[0], self.onNode[0]))
                treetop2 = treetopc2.fetchone()
                if treetop2 is not None:
                    treeparc = c.execute(
                        "SELECT sign,sign_conn FROM %s WHERE breakpoint = '%s'" % (treetop[0], self.onNode[0]))
                    treepar = treeparc.fetchone()
                    c.execute(
                        "UPDATE %s SET breakpoint='%s' WHERE sign='%s'" % (
                            treetop[0], self.nodeline.text(), treepar[0]))
                    conn.commit()
                    c.execute("INSERT INTO alterform VALUES('%s','%s','%s','%s','%s')" % (
                        treepar[0], gNode.text(0), self.nodeline.text(), treepar[1], treetop[0]))
                    conn.commit()
                else:
                    n = 2
                    while n <= len(self.onNode):
                        treetoppc2 = c.execute(
                            "SELECT tablename,sign FROM %s WHERE breakpoint = '%s'" % (treetop[0], self.onNode[-n]))
                        treetopp2 = treetoppc2.fetchone()
                        if treetopp2[0] != None:
                            break
                        n += 1
                    treeparc = c.execute(
                        "SELECT sign,sign_conn FROM %s WHERE breakpoint = '%s'" % (treetopp2[0], self.onNode[0]))
                    treepar = treeparc.fetchone()
                    c.execute(
                        "UPDATE %s SET breakpoint='%s' WHERE sign='%s'" % (
                            treetopp2[0], self.nodeline.text(), treepar[0]))
                    conn.commit()
                    c.execute("INSERT INTO alterform VALUES('%s','%s','%s','%s','%s')" % (
                        treepar[0], gNode.text(0), self.nodeline.text(), treepar[1], treetopp2[0]))
                    conn.commit()
            gNode.setText(0, '%s' % self.nodeline.text())
            self.qdxg = 0
            self.QRCK.close()
        elif self.qdsc == 1:
            try:
                sNode = self.treeWidget.currentItem()
                parentNode = sNode.parent()
                parentNode.removeChild(sNode)
            except:
                rootIndex = self.treeWidget.indexOfTopLevelItem(sNode)
                self.treeWidget.takeTopLevelItem(rootIndex)
            conn = sqlite3.connect("goon.db")
            c = conn.cursor()
            treetopc = c.execute(
                "SELECT all_xt.tablename FROM all_xt WHERE all_xt.breakpoint = '%s'" % self.onNode[-1])
            treetop = treetopc.fetchone()
            treetopc2 = c.execute(
                "SELECT tablename,sign FROM %s WHERE breakpoint = '%s'" % (treetop[0], self.onNode[0]))
            treetop2 = treetopc2.fetchone()
            if treetop2 is not None:
                if treetop2[0] is None:
                    treeparc = c.execute(
                        '''WITH RECURSIVE gz AS (
                            SELECT *FROM {0} WHERE breakpoint='{1}'
                            UNION ALL 
                            SELECT {0}.* FROM gz JOIN {0} ON gz.sign={0}.sign_conn)
                            SELECT sign,tablename FROM gz'''.format(treetop[0], self.onNode[0]))
                    treepar = treeparc.fetchall()
                    for treepars in treepar:
                        c.execute("delete from {0} where sign ='{1}'".format(treetop[0], treepars[0]))
                        conn.commit()
                        if treepars[1] is not None:
                            c.execute("drop table %s" % treepars[1])
                            conn.commit()
                else:
                    c.execute("delete from {0} where tablename ='{1}'".format(treetop[0], treetop2[0]))
                    conn.commit()
                    c.execute("drop table %s" % treetop2[0])
                    conn.commit()
            else:
                n = 2
                while n <= len(self.onNode):
                    treetoppc2 = c.execute(
                        "SELECT tablename,sign FROM %s WHERE breakpoint = '%s'" % (treetop[0], self.onNode[-n]))
                    treetopp2 = treetoppc2.fetchone()
                    if treetopp2[0] != None:
                        break
                    n += 1

                pdsql = c.execute(
                    "SELECT breakpoint FROM {0} WHERE breakpoint='{1}'".format(treetopp2[0], self.onNode[1]))
                pdpd = pdsql.fetchone()
                if pdpd != None:
                    treeparc = c.execute(
                        "SELECT b1.sign FROM {0} AS b1 INNER JOIN {0} AS b2 WHERE b1.sign_conn = b2.sign AND b1.breakpoint ='{1}' AND b2.breakpoint = '{2}'".format(
                            treetopp2[0], self.onNode[0], self.onNode[1]))
                    treepar = treeparc.fetchone()
                else:
                    treeparc = c.execute(
                        "SELECT sign FROM {0} WHERE breakpoint = '{1}'".format(treetopp2[0], self.onNode[0]))
                    treepar = treeparc.fetchone()
                c.execute("delete from {0} where sign ='{1}'".format(treetopp2[0], treepar[0]))
                conn.commit()
            self.qdsc = 0
            self.QRCK.close()


# 录入界面6
class LWindow(QMainWindow, Ui_MainWindow6):
    def __init__(self):
        super(LWindow, self).__init__(parent=None)
        self.setupUi(self)
        self.PB6qd.clicked.connect(self.PB6qdCao)

    def PB6qdCao(self):
        conn = sqlite3.connect("goon.db")
        c = conn.cursor()
        if self.LE61.text() != '' and self.TE61.text() != '' and self.TE62.text() != '' and self.TE63.text() != '' and self.LE62.text() != '':
            c.execute("INSERT INTO failure_logging VALUES ('%s','%s','%s','%s','%s')" % (
                self.LE61.text(), self.TE61.text(), self.TE62.text(), self.TE63.text(), self.LE62.text()))
            conn.commit()
        else:
            self.lb6tip.setText("请将信息填写完整!")


# 故障记录界面
class JWindow(QMainWindow, Ui_MainWindow7):
    def __init__(self):
        super(JWindow, self).__init__(parent=None)
        self.setupUi(self)
        self.PB7tc.clicked.connect(self.PB7tcCao)

    def PB7tcCao(self):
        winj.close()


# 系统设置界面9
class SWindow(QMainWindow, Ui_MainWindow9):
    def __init__(self):
        super(SWindow, self).__init__(parent=None)
        self.setupUi(self)
        self.PB91.clicked.connect(self.display1)
        self.PB92.clicked.connect(self.display2)
        self.PB93.clicked.connect(self.display3)
        self.PB94.clicked.connect(self.display4)
        self.PB95.clicked.connect(self.display5)
        self.PB96.clicked.connect(self.display6)
        self.PB911.clicked.connect(self.PB911Cao)

    def PB911Cao(self):
        wins.close()
        win.show()

    def display1(self):
        self.stk91.setCurrentIndex(0)

    def display2(self):
        self.stk91.setCurrentIndex(1)

    def display3(self):
        self.stk92.setCurrentIndex(0)

    def display4(self):
        self.stk92.setCurrentIndex(1)

    def display5(self):
        self.stk92.setCurrentIndex(2)

    def display6(self):
        self.stk92.setCurrentIndex(3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wink = KWindow()
    win0 = Window0()
    win = Window()
    winl = LWindow()
    winj = JWindow()
    wins = SWindow()
    win0.show()
    win1 = MainWin()
    sys.exit(app.exec())
