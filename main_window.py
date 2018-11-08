#Main window
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from ui_main_window import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
    @pyqtSlot()
    def on_actionOuvrir_triggered(self):
        (nomFichier,filtre) = QFileDialog.getOpenFileName(self,"Nouveau_fichier",  filter="vcf(*.vcf)")
        if nomFichier:
            QMessageBox.information(self,"TRACE", "Fichier à ouvrir:\n\n%s"%nomFichier)

            
    @pyqtSlot()
    def on_actionQuitter_triggered(self):
        self.close()
    def closeEvent(self,event):
        messageConfirmation = "Êtes-vous sûr de vouloir quitter VCF-VS ?"
        reponse = QMessageBox.question(self,"Confirmation",messageConfirmation,QMessageBox.Yes,QMessageBox.No)
        if reponse == QMessageBox.Yes:
            event.accept()
            message="Très bien j'espère vous avoir été utile"
            reponse1=QMessageBox.question(self, "Confirmation", message, QMessageBox.Yes)
        else:
            event.ignore()
