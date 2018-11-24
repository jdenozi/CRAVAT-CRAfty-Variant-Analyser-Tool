#Main window
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from ui_main_window import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot

import re
import matplotlib.pyplot as plt

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        qApp.installEventFilter(self)
        self.chromosome_ref={}
        self.setupUi(self)
        self.show()
    
    def createItemsList(self, i):        
        return (self.comboBox_2.addItem(i))
    
    
    @pyqtSlot()
    def on_actionOuvrir_triggered(self):
        (nomFichier,filtre) = QFileDialog.getOpenFileName(self,"Nouveau_fichier",  filter="vcf(*.vcf)")
        if nomFichier:
            QMessageBox.information(self,"TRACE", "Fichier à ouvrir:\n\n%s"%nomFichier)
            with open(nomFichier,"r") as vcf:
                file_read=vcf.readlines()
            #Boucle sur le fichier vcf
            for line_vcf in file_read:
                if not line_vcf.startswith("#"):#si la ligne ne commence pas par # -> lecture de la ligne
                    information=re.findall("\S+",line_vcf)
                    #Instruction permettant de valider la présence d'informations pour chaque ligne, sinon remplit par ?
                    if len(information)>0:
                        chromosome=information[0]
                    if len(information)==0:
                        chromosome, position, identifiant,  ref, alt, qual="?", "?", "?", "?", "?", "?"
                    if len(information)>1:
                        position=information[1]
                    if len(information)>2:
                        identifiant=information[2]
                    if len(information)>3:
                        ref=information[3]
                    if len(information)>4:
                        alt=information[4]
                    if len(information)>5:
                        qual=information[5]
                        liste_mutation=[]
                        if chromosome in self.chromosome_ref:
                            if position in self.chromosome_ref[chromosome].keys():
                                liste_mutation.append(ref)
                                liste_mutation.append(alt)
                                liste_mutation.append(qual)
                                self.chromosome_ref[chromosome][position]=liste_mutation
                            else:
                                liste_mutation.append(ref)
                                liste_mutation.append(alt)
                                liste_mutation.append(qual)
                                self.chromosome_ref.get(chromosome)[position]=liste_mutation
                           
                        else:
                            liste_mutation.append(ref)
                            liste_mutation.append(alt)
                            liste_mutation.append(qual)
                            self.chromosome_ref[chromosome]={}
                            self.chromosome_ref[chromosome][position]=liste_mutation
            #
            for i in self.chromosome_ref:
                self.createItemsList(i)
      
    def compteur_chromosome(self):
        compteur_chromosome=0
        for i in self.chromosome_ref:
            compteur_chromosome=compteur_chromosome+1
        return(str(compteur_chromosome))
        
    def nombre_mutation_total(self):
        liste_chromosome_nb_mutation=[]
        liste_mutation=[]
        liste_chromosome=[]
       #parcours des clé du dictionnaire
        for chromosome in self.chromosome_ref:
            compteur_mutation=0
            #parcours des clé du dictionnaire de dictionnaire
            for position in self.chromosome_ref.get(chromosome):
                compteur_mutation=compteur_mutation+1 # compteur pour chaque mutation de l'intégralité du dictionnaire de dictionnaire
            liste_chromosome_nb_mutation.append("Chromosome: "+str(chromosome)+" Nombre de mutation: "+str(compteur_mutation))
            liste_chromosome.append(chromosome)
            liste_mutation.append(compteur_mutation)
            #print(compteur_mutation)
        return (liste_chromosome, liste_mutation)
        
        
    def plot_mutation_par_chromosome(self):
        liste_chromosome=[]
        liste_mutation=[]
        somme=0
        moyenne=0
        #print(self.nombre_mutation_total(chromosome_ref))
        for chromosome in self.nombre_mutation_total()[0]:
            liste_chromosome.append(chromosome)
        for mutation in self.nombre_mutation_total()[1]:
            liste_mutation.append(mutation)
            somme=somme+mutation
        moyenne=somme/len(self.nombre_mutation_total()[1])
        plt.title("Nombre de mutation par genome")
        bars=plt.bar(liste_chromosome, liste_mutation)
        for index,  mutation in enumerate(liste_mutation):
             if mutation<=(moyenne*(0.8) ):
                
                bars[index].set_facecolor("red")
             elif mutation>=(moyenne*(1.2)):
              
                bars[index].set_facecolor("Green")
             else:

                bars[index].set_facecolor("Yellow")
    
        plt.xlabel("Chromosome")
        plt.ylabel('Nombre de Mutation')
        plt.show()
        
        
    @pyqtSlot()
    def on_actionQuitter_triggered(self):
        self.close()
    def closeEvent(self,event):
        messageConfirmation = "Are you sure you want to quit ?"
        reponse = QMessageBox.question(self,"Confirmation",messageConfirmation,QMessageBox.Yes,QMessageBox.No)
        if reponse == QMessageBox.Yes:
            event.accept()
            message="Hope it was usefull"
            reponse1=QMessageBox.question(self, "Confirmation", message, QMessageBox.Yes)
        else:
            event.ignore()
            
            
    def updateText(self, message):
        self.plainTextEdit.clear()
        if self.comboBox_3.currentIndex()==0:
                message="Open file before launch any function\nThis section provide informations about choosen method\nDont forget to read every parameter the function need"
                self.plainTextEdit.setPlainText(message )
        if self.comboBox_3.currentIndex()==1:
            message="Function which calcul the current number of Chromosome in the current vcf file \nType= Text"
            self.plainTextEdit.setPlainText(message )
        if self.comboBox_3.currentIndex()==2:
                message="Function which calcul the current number of Chromosome mutation in the current vcf file \nType=text"
                self.plainTextEdit.setPlainText(message )
        if self.comboBox_3.currentIndex()==3:
                message="Graphs of the current number of chromosome mutation in the current vcf file \nType= Graph\nColor code mean that the number of mutation is above or behind the average Chromosome of the entire file"
                self.plainTextEdit.setPlainText(message )
        if self.comboBox_3.currentIndex()==4:
                message="Graphs of the current number of chromosome mutation in the current Chromosome \nType= Graph"
                self.plainTextEdit.setPlainText(message )
    
    #Méthode permettant de connection de la comboBox au Launcher et de lancer la bonne méthode
    def Launcher(self):
        if self.comboBox_3.currentIndex()==1:
            self.plainTextEdit_2.clear()
            self.plainTextEdit_2.setPlainText("Current file contain "+self.compteur_chromosome() +" Chromosomes")
            
        if self.comboBox_3.currentIndex()==2:
            self.plot_mutation_par_chromosome()
            

   
