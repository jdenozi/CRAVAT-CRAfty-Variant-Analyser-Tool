#!/bin/env python3 

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import * 
class Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About project"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:600;\">CRAVAT: Crafty Variant Analyser Tool Version 1.0</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The CRAVAT project is a program designed for working with VCF file (only). The aim of CRAVAT tool is to provide easily accessible methods with GUI for working with complex genetic variation data in the form of VCF files.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This toolset can be used to perform the following operations on VCF files:</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">Filter out specific Chromosome</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">Compare files</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">Summarize variants</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">Filter out</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">Filter out specifiquely with quality and position<a name=\"user-content-author\"></a> </li></ul>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"user-content-author\"></a><span style=\" font-size:x-large; font-weight:600;\">A</span><span style=\" font-size:x-large; font-weight:600;\">uthor</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Denozi Julien &lt;<a href=\"mailto:denozi.j@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">denozi.j@gmail.com</span></a>&gt;</p></body></html>"))


