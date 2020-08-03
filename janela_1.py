# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Senha import main


class Ui_painel(object):
    def setupUi(self, painel):
        painel.setObjectName("painel")
        painel.resize(704, 446)
        painel.setMaximumSize(QtCore.QSize(704, 446))
        self.radioButton = QtWidgets.QRadioButton(painel)
        self.radioButton.setGeometry(QtCore.QRect(30, 70, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.botton1 = QtWidgets.QPushButton(painel)
        self.botton1.setGeometry(QtCore.QRect(560, 370, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.botton1.setFont(font)
        self.botton1.setObjectName("botton1")
        self.textbox = QtWidgets.QLineEdit(painel)
        self.textbox.setGeometry(QtCore.QRect(0, 310, 701, 32))
        self.textbox.setObjectName("textbox")
        self.horizontalScrollBar = QtWidgets.QScrollBar(painel)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(310, 70, 311, 16))
        self.horizontalScrollBar.setMinimum(6)
        self.horizontalScrollBar.setMaximum(16)
        self.horizontalScrollBar.setPageStep(1)
        self.horizontalScrollBar.setProperty("value", 8)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.label = QtWidgets.QLabel(painel)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(400, 30, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(painel)
        self.label_2.setGeometry(QtCore.QRect(280, 60, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(painel)
        self.label_3.setGeometry(QtCore.QRect(630, 60, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(painel)
        QtCore.QMetaObject.connectSlotsByName(painel)

    def retranslateUi(self, painel):
        _translate = QtCore.QCoreApplication.translate
        painel.setWindowTitle(_translate("painel", "Dialog"))
        self.radioButton.setText(_translate("painel", "Somente letras"))
        self.botton1.setText(_translate("painel", "Gerar"))
        self.label.setText(_translate("painel", "Tamanho da senha"))
        self.label_2.setText(_translate("painel", "6"))
        self.label_3.setText(_translate("painel", "16"))

        self.botton1.clicked.connect(self.start)
        self.horizontalScrollBar.valueChanged.connect(self.start)

    def start(self):
        self.label_3.setText(str(self.horizontalScrollBar.value()))
        if self.radioButton.isChecked():
            self.textbox.setText(main.gerar(int(self.horizontalScrollBar.value())))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    painel = QtWidgets.QDialog()
    ui = Ui_painel()
    ui.setupUi(painel)
    painel.show()
    sys.exit(app.exec_())