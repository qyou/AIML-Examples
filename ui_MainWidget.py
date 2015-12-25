# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWidget.ui'
#
# Created: Fri Dec 25 16:34:06 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import aiml
import datetime

class AliceBot(object):
    def __init__(self, xmlpath="startup.xml"):
        self.kernel = aiml.Kernel()
        self.kernel.learn(xmlpath)
        self.kernel.respond("LOAD ALICE")
    def respond(self, text):
        return self.kernel.respond(text)

class Ui_Form(object):
    def setupUi(self, Form):
        self.content = ""
        self.bot = AliceBot()
        Form.setObjectName("Form")
        Form.resize(525, 300)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 501, 281))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 2)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setFocus()
        self.pushButton.setAutoDefault(True)
        
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.update_lineEdit)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.update_textEdit)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("editingFinished()"), self.update_lineEdit)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("editingFinished()"), self.update_textEdit)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Alice机器人", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "发送", None, QtGui.QApplication.UnicodeUTF8))
        
    def update_lineEdit(self):
        lineText = self.lineEdit.text().strip()
        if lineText and lineText != "":
            self.content += "%s You said: %s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), lineText, )
            self.content += "%s Alice said: %s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.bot.respond(lineText))
            self.lineEdit.clear()
        pass
    
    def update_textEdit(self):
        self.textEdit.setText(self.content)
        # automatically move to the last line
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        pass

