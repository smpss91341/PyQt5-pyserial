# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lin\Desktop\Pyquino\core\widgets\serialUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(573, 415)
        Dialog.setSizeGripEnabled(True)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBoxPort = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxPort.setObjectName("comboBoxPort")
        self.gridLayout.addWidget(self.comboBoxPort, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.comboBoxBaud = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxBaud.setObjectName("comboBoxBaud")
        self.gridLayout.addWidget(self.comboBoxBaud, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBoxCheckSum = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxCheckSum.setObjectName("comboBoxCheckSum")
        self.gridLayout.addWidget(self.comboBoxCheckSum, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBoxBits = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxBits.setObjectName("comboBoxBits")
        self.gridLayout.addWidget(self.comboBoxBits, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBoxStopBits = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxStopBits.setObjectName("comboBoxStopBits")
        self.gridLayout.addWidget(self.comboBoxStopBits, 4, 1, 1, 1)
        self.pushButtonOpenSerial = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonOpenSerial.setObjectName("pushButtonOpenSerial")
        self.gridLayout.addWidget(self.pushButtonOpenSerial, 5, 0, 1, 2)
        self.comboBoxPort.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.comboBoxBaud.raise_()
        self.label_3.raise_()
        self.comboBoxCheckSum.raise_()
        self.label_4.raise_()
        self.comboBoxBits.raise_()
        self.label_5.raise_()
        self.comboBoxStopBits.raise_()
        self.pushButtonOpenSerial.raise_()
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEditReceived = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditReceived.sizePolicy().hasHeightForWidth())
        self.textEditReceived.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEditReceived.setFont(font)
        self.textEditReceived.setReadOnly(True)
        self.textEditReceived.setObjectName("textEditReceived")
        self.verticalLayout.addWidget(self.textEditReceived)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEditSent = QtWidgets.QTextEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEditSent.setFont(font)
        self.textEditSent.setObjectName("textEditSent")
        self.horizontalLayout.addWidget(self.textEditSent)
        self.pushButtonSendData = QtWidgets.QPushButton(Dialog)
        self.pushButtonSendData.setAutoDefault(True)
        self.pushButtonSendData.setObjectName("pushButtonSendData")
        self.horizontalLayout.addWidget(self.pushButtonSendData)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "com setting"))
        self.label_2.setText(_translate("Dialog", "com"))
        self.label.setText(_translate("Dialog", "baurd"))
        self.label_3.setText(_translate("Dialog", "first"))
        self.label_4.setText(_translate("Dialog", "data"))
        self.label_5.setText(_translate("Dialog", "stop"))
        self.pushButtonOpenSerial.setText(_translate("Dialog", "open"))
        self.textEditSent.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButtonSendData.setText(_translate("Dialog", "send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

