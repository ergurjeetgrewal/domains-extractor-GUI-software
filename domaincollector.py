import re
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gmail = QtWidgets.QCheckBox(self.centralwidget)
        self.gmail.setGeometry(QtCore.QRect(630, 20, 81, 20))
        self.gmail.setObjectName("gmail")
        self.oal = QtWidgets.QCheckBox(self.centralwidget)
        self.oal.setGeometry(QtCore.QRect(630, 50, 81, 20))
        self.oal.setObjectName("oal")
        self.comcast = QtWidgets.QCheckBox(self.centralwidget)
        self.comcast.setGeometry(QtCore.QRect(630, 80, 81, 20))
        self.comcast.setObjectName("comcast")
        self.yahoo = QtWidgets.QCheckBox(self.centralwidget)
        self.yahoo.setGeometry(QtCore.QRect(630, 110, 81, 20))
        self.yahoo.setObjectName("yahoo")
        self.hotmail = QtWidgets.QCheckBox(self.centralwidget)
        self.hotmail.setGeometry(QtCore.QRect(630, 140, 81, 20))
        self.hotmail.setObjectName("hotmail")
        self.msn = QtWidgets.QCheckBox(self.centralwidget)
        self.msn.setGeometry(QtCore.QRect(630, 170, 81, 20))
        self.msn.setObjectName("msn")
        self.outlook = QtWidgets.QCheckBox(self.centralwidget)
        self.outlook.setGeometry(QtCore.QRect(630, 200, 81, 20))
        self.outlook.setObjectName("outlook")
        self.verizon = QtWidgets.QCheckBox(self.centralwidget)
        self.verizon.setGeometry(QtCore.QRect(630, 230, 81, 20))
        self.verizon.setObjectName("verizon")
        self.outlookconz = QtWidgets.QCheckBox(self.centralwidget)
        self.outlookconz.setGeometry(QtCore.QRect(630, 260, 101, 20))
        self.outlookconz.setObjectName("outlookconz")
        self.xtra = QtWidgets.QCheckBox(self.centralwidget)
        self.xtra.setGeometry(QtCore.QRect(630, 290, 81, 20))
        self.xtra.setObjectName("xtra")
        self.live = QtWidgets.QCheckBox(self.centralwidget)
        self.live.setGeometry(QtCore.QRect(630, 310, 101, 30))
        self.live.setObjectName("live")
        self.att_net = QtWidgets.QCheckBox(self.centralwidget)
        self.att_net.setGeometry(QtCore.QRect(630, 330, 101, 30))
        self.att_net.setObjectName("att")
        self.import_2 = QtWidgets.QPushButton(self.centralwidget)
        self.import_2.setGeometry(QtCore.QRect(30, 320, 93, 28))
        self.import_2.setObjectName("import_2")
        self.extract = QtWidgets.QPushButton(self.centralwidget)
        self.extract.setGeometry(QtCore.QRect(450, 320, 93, 28))
        self.extract.setObjectName("extract")
        self.importtext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.importtext.setGeometry(QtCore.QRect(20, 10, 531, 291))
        self.importtext.setPlainText("")
        self.importtext.setObjectName("importtext")
        self.export_2 = QtWidgets.QPushButton(self.centralwidget)
        self.export_2.setGeometry(QtCore.QRect(240, 520, 93, 28))
        self.export_2.setObjectName("export_2")
        self.generatedtext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.generatedtext.setGeometry(QtCore.QRect(20, 370, 541, 131))
        self.generatedtext.setObjectName("generatedtext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuMENU = QtWidgets.QMenu(self.menubar)
        self.menuMENU.setObjectName("menuMENU")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDeveloper = QtWidgets.QAction(MainWindow)
        self.actionDeveloper.setObjectName("actionDeveloper")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.menuMENU.addAction(self.actionImport)
        self.menuMENU.addAction(self.actionExport)
        self.menuMENU.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionDeveloper)
        self.menuAbout.addAction(self.actionVersion)
        self.menubar.addAction(self.menuMENU.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.extract.clicked.connect(self.extractor)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.import_2.clicked.connect(self.open_text_file)
        self.export_2.clicked.connect(self.save_text_file)
        self.actionImport.triggered.connect(self.open_text_file)
        self.actionExport.triggered.connect(self.save_text_file)
        self.actionExit.triggered.connect(self.app_close)

    def extractor(self, MainWindow):
        self.domainlist = []
        self.domainlist = self.checkbox_status(MainWindow)
        self.generatedtext.clear()
        if len(self.domainlist) == 0:
            self.generatedtext.insertPlainText(
                'Please select alteast one option')
            return 0
        self.str = self.importtext.toPlainText()
        emails = re.findall(
            r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z:0-9!#$%&'()*+,-./;<=>?@[\]^_`{|}~]+", self.str)
        if len(emails) == 0:
            self.generatedtext.insertPlainText('No Matching domain Found')
        for value in self.domainlist:
            if value == 1:
                for email in emails:
                    if email.find('gmail.com') != -1:
                        self.generatedtext.insertPlainText(email+'\n')
            if value == 2:
                for email in emails:
                    if email.find('aol.com') != -1:
                        self.generatedtext.insertPlainText(email+'\n')
            if value == 3:
                for email in emails:
                    if email.find('comcast.net') != -1:
                        self.generatedtext.insertPlainText(email+'\n')
            if value == 4:
                for email in emails:
                    if email.find('yahoo.com') != -1:
                        self.generatedtext.insertPlainText(email+'\n')
            if value == 5:
                for email in emails:
                    if email.find('hotmail.com') != -1:
                        self.generatedtext.insertPlainText(email+'\n')
            if value == 6:
                for email in emails:
                    if email.find('msn.com') != -1:
                        self.generatedtext.insertPlainText(email+'\n')
            if value == 7:
                for email in emails:
                    if email.find('outlook.com') != -1:
                        self.generatedtext.insertPlainText(email+'\n')
            if value == 8:
                for email in emails:
                    if email.find('verizon.net') != -1:
                        self.generatedtext.insertPlainText(email+'\n')
            if value == 9:
                for email in emails:
                    if email.find('outlook.co.nz') != -1:
                        self.generatedtext.insertPlainText(email+'\n')
            if value == 10:
                for email in emails:
                    if email.find('xtra.co.nz') != -1:
                        self.generatedtext.insertPlainText(email+'\n')
            if value == 11:
                for email in emails:
                    if email.find('live.com') != -1:
                        self.generatedtext.insertPlainText(email+'\n')
            if value == 12:
                for email in emails:
                    if email.find('att.net') != -1:
                        self.generatedtext.insertPlainText(email+'\n')

    def checkbox_status(self, MainWindow):
        if self.gmail.isChecked():
            self.domainlist.append(1)
        if self.oal.isChecked():
            self.domainlist.append(2)
        if self.comcast.isChecked():
            self.domainlist.append(3)
        if self.yahoo.isChecked():
            self.domainlist.append(4)
        if self.hotmail.isChecked():
            self.domainlist.append(5)
        if self.msn.isChecked():
            self.domainlist.append(6)
        if self.outlook.isChecked():
            self.domainlist.append(7)
        if self.verizon.isChecked():
            self.domainlist.append(8)
        if self.outlookconz.isChecked():
            self.domainlist.append(9)
        if self.xtra.isChecked():
            self.domainlist.append(10)
        if self.live.isChecked():
            self.domainlist.append(11)
        if self.att_net.isChecked():
            self.domainlist.append(12)
        return self.domainlist

    def open_text_file(self):
        try:
            fname = QFileDialog.getOpenFileName(
                None, 'Open file', '', 'Text (*.csv *.txt)')
            with open(fname[0], 'r') as f:
                file_text = f.read()
                self.importtext.insertPlainText(file_text)
        except Exception as e:
            pass

    def save_text_file(self):
        try:
            fname = QFileDialog.getSaveFileName(
                None, 'Save File', '', 'Text (*.txt)')
            with open(fname[0], 'w') as f:
                file_text = self.generatedtext.toPlainText()
                f.write(file_text)
        except Exception as e:
            pass

    def app_close(self):
        exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Domain Extractor"))
        self.gmail.setText(_translate("MainWindow", "Gmail"))
        self.oal.setText(_translate("MainWindow", "Oal"))
        self.comcast.setText(_translate("MainWindow", "Comcast"))
        self.yahoo.setText(_translate("MainWindow", "Yahoo"))
        self.hotmail.setText(_translate("MainWindow", "Hotmail"))
        self.msn.setText(_translate("MainWindow", "Msn"))
        self.outlook.setText(_translate("MainWindow", "Outlook"))
        self.verizon.setText(_translate("MainWindow", "Verizon"))
        self.outlookconz.setText(_translate("MainWindow", "Outlook.co.nz"))
        self.xtra.setText(_translate("MainWindow", "Xtra"))
        self.live.setText(_translate("MainWindow", "Live"))
        self.att_net.setText(_translate("MainWindow", "att"))
        self.import_2.setText(_translate("MainWindow", "Import"))
        self.extract.setText(_translate("MainWindow", "Extract"))
        self.export_2.setText(_translate("MainWindow", "Export"))
        self.menuMENU.setTitle(_translate("MainWindow", "Menu"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDeveloper.setText(_translate("MainWindow", "Developer"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
