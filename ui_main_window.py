# -*- coding: utf-8 -*-
#!/usr/bin/env python3


from PyQt5 import QtCore, QtGui, QtWidgets
import main_window

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 486)
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
        self.comboBox_3 = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_3)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 2)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 0, 2, 4, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_4.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_4.addWidget(self.checkBox_2)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 2, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
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
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
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
        
        #chromosome_ref=self.on_actionOuvrir_triggered()
        
        
        self.pushButton.clicked.connect(self.plot_mutation_par_chromosome)
        
        self.actionSauvegarder = QtWidgets.QAction(MainWindow)
        self.actionSauvegarder.setObjectName("actionSauvegarder")
        self.actionCopier = QtWidgets.QAction(MainWindow)
        self.actionCopier.setObjectName("actionCopier")
        self.actionColler = QtWidgets.QAction(MainWindow)
        self.actionColler.setObjectName("actionColler")
        self.actionSupprimer = QtWidgets.QAction(MainWindow)
        self.actionSupprimer.setObjectName("actionSupprimer")
        self.actionFull_screen = QtWidgets.QAction(MainWindow)
        self.actionFull_screen.setObjectName("actionFull_screen")
        self.actionA_propos = QtWidgets.QAction(MainWindow)
        self.actionA_propos.setObjectName("actionA_propos")
        self.actionSignaler_un_bug = QtWidgets.QAction(MainWindow)
        self.actionSignaler_un_bug.setObjectName("actionSignaler_un_bug")
        self.menuFichier.addAction(self.actionNouveau_fichier)
        self.menuFichier.addAction(self.actionSauvegarder)
        self.menuEdition.addAction(self.actionCopier)
        self.menuEdition.addAction(self.actionColler)
        self.menuEdition.addAction(self.actionSupprimer)
        self.menuFen_tre.addAction(self.actionFull_screen)
        self.menuAide.addAction(self.actionA_propos)
        self.menuAide.addAction(self.actionSignaler_un_bug)
        self.menuBar.addAction(self.menuFichier.menuAction())
        self.menuBar.addAction(self.menuEdition.menuAction())
        self.menuBar.addAction(self.menuFen_tre.menuAction())
        self.menuBar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Quelles fonctionnalités voulez-vous utiliser ?"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "\n"
"a\n"
"aa\n"
"a\n"
"a\n"
"a\n"
"a\n"
"a\n"
"aa\n"
"a\n"
"\n"
"a\n"
"aa"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Sélection du chromosome"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Sélection de la mutation"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "a\n"
"a\n"
"a\n"
"a\n"
"a\n"
"a\n"
"a\n"
"\n"
"a\n"
"aa\n"
"a\n"
"a\n"
"a\n"
"a\n"
"a\n"
"a\n"
"\n"
"a\n"
"a\n"
"a\n"
"a\n"
"a\n"
"a\n"
"a\n"
""))
        self.checkBox.setText(_translate("MainWindow", "qualité"))
        self.checkBox_2.setText(_translate("MainWindow", "position"))
        
        self.pushButton.setText(_translate("MainWindow", "Launch"))
        
        
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuEdition.setTitle(_translate("MainWindow", "Edition"))
        self.menuFen_tre.setTitle(_translate("MainWindow", "Fenêtre"))
        self.menuAide.setTitle(_translate("MainWindow", "Aide"))
        self.actionNouveau_fichier.setText(_translate("MainWindow", "Nouveau fichier"))
        self.actionSauvegarder.setText(_translate("MainWindow", "Sauvegarder"))
        self.actionCopier.setText(_translate("MainWindow", "Copier"))
        self.actionCopier.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionColler.setText(_translate("MainWindow", "Coller"))
        self.actionColler.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionSupprimer.setText(_translate("MainWindow", "Retour en arrière"))
        self.actionSupprimer.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionFull_screen.setText(_translate("MainWindow", "Full screen"))
        self.actionFull_screen.setShortcut(_translate("MainWindow", "F11"))
        self.actionA_propos.setText(_translate("MainWindow", "A propos"))
        self.actionSignaler_un_bug.setText(_translate("MainWindow", "Signaler un bug "))
