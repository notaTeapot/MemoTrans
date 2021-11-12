# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Vasco\Documents\Python\SchwurbelTranskipt\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 232)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.folder_edit = QtWidgets.QLineEdit(self.groupBox)
        self.folder_edit.setText("")
        self.folder_edit.setReadOnly(True)
        self.folder_edit.setObjectName("folder_edit")
        self.gridLayout.addWidget(self.folder_edit, 0, 0, 1, 1)
        self.folder_btn = QtWidgets.QPushButton(self.groupBox)
        self.folder_btn.setObjectName("folder_btn")
        self.gridLayout.addWidget(self.folder_btn, 0, 1, 1, 1)
        self.convert_check = QtWidgets.QCheckBox(self.groupBox)
        self.convert_check.setChecked(True)
        self.convert_check.setObjectName("convert_check")
        self.gridLayout.addWidget(self.convert_check, 1, 0, 1, 1)
        self.init_btn = QtWidgets.QPushButton(self.groupBox)
        self.init_btn.setEnabled(False)
        self.init_btn.setObjectName("init_btn")
        self.gridLayout.addWidget(self.init_btn, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setEnabled(False)
        self.start_btn.setObjectName("start_btn")
        self.verticalLayout.addWidget(self.start_btn)
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.status_label.setFont(font)
        self.status_label.setObjectName("status_label")
        self.verticalLayout.addWidget(self.status_label)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SchwurbelTranskript v0.1"))
        self.groupBox.setTitle(_translate("MainWindow", "Orderauswahl"))
        self.folder_btn.setText(_translate("MainWindow", "Ordner auswählen"))
        self.convert_check.setText(_translate("MainWindow", ".ogg dateien konvertieren und aufteilen"))
        self.init_btn.setText(_translate("MainWindow", "Dateien suchen"))
        self.start_btn.setText(_translate("MainWindow", "Starten!"))
        self.status_label.setText(_translate("MainWindow", "TextLabel"))
