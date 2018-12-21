#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from main_window import *
"""
This class create each object for the GUI
"""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.windowAbout=None
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 470)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.setWindowIcon(QtGui.QIcon("picture/cravatfox.jpg"))
        
        #Création des items de la liste déroulante des différentes méthodes
        self.comboBox_3 = QtWidgets.QComboBox(self.centralWidget)
        global comboBox_3
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("") 
        self.verticalLayout_3.addWidget(self.comboBox_3)

        #Création de l'espace d'information des différentes méthodes de la liste
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        
        #Creation de la liste déroulante des chromosomes
        self.comboBox_2 = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("Select Chromosome")
        self.verticalLayout_3.addWidget(self.comboBox_2)

        #Création liste déroulante des mutatations
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        
        #Creation de la zone d'information des méthodes
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 2)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
         
         #Bouton Launch
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setObjectName("pushButton_2")
       
        self.gridLayout.addWidget(self.pushButton_2,2.5,2, 4, 1)

        self.gridLayout.addWidget(self.plainTextEdit_2, 0, 2, 3, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        #Check box pour la qualité
        self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_4.addWidget(self.checkBox)
        
        #Check box pour la position
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_4.addWidget(self.checkBox_2)
        
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 2, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        #Line edit de la check box de la qualité
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        #Line edit de la check box de la position
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        
        #Line edit de la check box de la qualité
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        #Bouton clear
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        
        
        
        self.verticalLayout_5.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout_5, 3, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 673, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFichier = QtWidgets.QMenu(self.menuBar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuEdition = QtWidgets.QMenu(self.menuBar)
        self.menuEdition.setObjectName("menuEdition")
        self.menuFen_tre = QtWidgets.QMenu(self.menuBar)
        self.menuFen_tre.setObjectName("menuFen_tre")
        self.menuAide = QtWidgets.QMenu(self.menuBar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNouveau_fichier = QtWidgets.QAction(MainWindow)
        
        #chromosome_ref=self.on_actionOuvrir_triggered()
        
        self.actionNouveau_fichier.setObjectName("actionNouveau_fichier")
        self.actionNouveau_fichier.triggered.connect(self.on_actionOuvrir_triggered)
        #Connection Lauch -> méthode
        self.pushButton.clicked.connect(self.Launcher)
        self.pushButton_2.clicked.connect(self.Clear )
        
        self.actionSauvegarder = QtWidgets.QAction(MainWindow)
        self.actionSauvegarder.setObjectName("actionSauvegarder")
        self.actionSauvegarder.setShortcut("Ctrl+S")
        self.actionSauvegarder.setStatusTip("Save File")
        self.actionSauvegarder.triggered.connect(self.file_save)


        self.actionCopier = QtWidgets.QAction(MainWindow)
        self.actionCopier.setObjectName("actionCopier")
        self.actionCopier.setShortcut("Ctrl+C")
        self.actionColler = QtWidgets.QAction(MainWindow)
        self.actionColler.setObjectName("actionColler")
        self.actionColler.setShortcut("Ctrl+V")
        self.actionSupprimer = QtWidgets.QAction(MainWindow)
        self.actionSupprimer.setObjectName("actionSupprimer")
        self.actionSupprimer.setShortcut("Ctrl+z")
        self.actionFull_screen = QtWidgets.QAction(MainWindow)
        self.actionFull_screen.setObjectName("actionFull_screen")
        self.actionA_propos = QtWidgets.QAction(MainWindow)
        self.actionA_propos.setObjectName("actionA_propos")
        
        self.actionSignaler_un_bug = QtWidgets.QAction(MainWindow)
        self.menuFichier.addAction(self.actionNouveau_fichier)
        self.menuFichier.addAction(self.actionSauvegarder)
        self.menuEdition.addAction(self.actionCopier)
        self.menuEdition.addAction(self.actionColler)
        self.menuEdition.addAction(self.actionSupprimer)
        self.menuFen_tre.addAction(self.actionFull_screen)
        self.menuAide.addAction(self.actionA_propos)
        self.menuBar.addAction(self.menuFichier.menuAction())
        self.menuBar.addAction(self.menuEdition.menuAction())
        self.menuBar.addAction(self.menuFen_tre.menuAction())
        self.menuBar.addAction(self.menuAide.menuAction())
        self.actionA_propos.triggered.connect(self.About)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        
        #Connect any comboBox with plaintextEdit for refresh the information about the current method
        MainWindow.setWindowTitle(_translate("MainWindow", "CRAVAT(CRAfty Variant Analyser Tool)"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Which function do you want to use?"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "How many Chromosome do file have"))
        self.comboBox_3.activated[int].connect(self.updateText)
        self.comboBox_3.setItemText(2, _translate("MainWindow", "How many mutation do file have"))
        self.comboBox_3.activated[int].connect(self.updateText)
        self.comboBox_3.setItemText(3, _translate("MainWindow", "How many mutation do chromosome have"))
        self.comboBox_3.activated[int].connect(self.updateText)
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Dynamic visualization plot for every Chromosome mutation in a choosen Chromosome "))
        self.comboBox_3.activated[int].connect(self.updateText)
         
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Mutation filter with quality and interval position "))
        self.comboBox_3.activated[int].connect(self.updateText)
        
        
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Open file before launch any function.\n\
                This section provide informations about chosen method.\n\
                Dont forget to read every parameter the function need.\n\
                Clear button allow you to clean the entire box.\n\
                Don't forget, you can save and compare every informations in the box until you don't clear.") )
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Select Chromosome"))
        
        self.comboBox.setItemText(0, _translate("MainWindow", "Select mutation"))
        
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", ""))
        
        
        self.checkBox.setText(_translate("MainWindow", "Quality"))
        self.checkBox_2.setText(_translate("MainWindow", "Position"))
        
        self.pushButton.setText(_translate("MainWindow", "Launch"))
        self.pushButton_2.setText(_translate("MainWindow","Clear"))
        
        self.menuFichier.setTitle(_translate("MainWindow", "File"))
        self.menuEdition.setTitle(_translate("MainWindow", "Edition"))
        self.menuFen_tre.setTitle(_translate("MainWindow", "Window"))
        self.menuAide.setTitle(_translate("MainWindow", "Help"))
        self.actionNouveau_fichier.setText(_translate("MainWindow", "New file"))
        self.actionSauvegarder.setText(_translate("MainWindow", "Save"))
        self.actionCopier.setText(_translate("MainWindow", "Copier"))
        self.actionCopier.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionColler.setText(_translate("MainWindow", "Coller"))
        self.actionColler.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionSupprimer.setText(_translate("MainWindow", "Back"))
        self.actionSupprimer.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionFull_screen.setText(_translate("MainWindow", "Full screen"))
        self.actionFull_screen.setShortcut(_translate("MainWindow", "F11"))
        self.actionA_propos.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
