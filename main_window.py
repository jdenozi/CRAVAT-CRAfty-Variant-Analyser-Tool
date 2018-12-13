#!/bin/env python3
# -*- coding: utf-8 -*-

'''
CRAVAT: crafty variant analyser tool

The file contain all the graphical methods connected to the data analysis method
'''


#LIBRARY
import os
from PyQt5.QtWidgets import *
from ui_main_window import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot
import re
import matplotlib.pyplot as plt
from PIL import Image

"""
Déclaration of the class main window
contains all connections between graphical object and data analysis method
"""
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        qApp.installEventFilter(self)
        self.chromosome_ref={}
        self.setupUi(self)
        self.show()
   #Updated from the drop-down list of chromosomes/mutations to each new file 
    def createItemsList(self, i):        
        return (self.comboBox_2.addItem(i))
    
    def createItemsListMutation(self,i):
        return(self.comboBox.addItem(i))
   #Création of the list of the different mutations 
    def typeOfMutation(self):
        differentMutation=[]
        differentMutation.clear()
        
        for chromosome in self.chromosome_ref:
            for position in self.chromosome_ref[chromosome]:
                listeInfo=self.chromosome_ref[chromosome].get(position)
                if listeInfo[1] not in differentMutation:
                    differentMutation.append(listeInfo[1])
        return (differentMutation)
    """
    Open the file tree with a filter on the VCF file
    Creation of the chromosome dictionnary, containing a position dictionnary
    with the value of a list containing
    """
    @pyqtSlot()
    def on_actionOuvrir_triggered(self):
        (nomFichier,filtre) = QFileDialog.getOpenFileName(self,"Nouveau_fichier",  filter="vcf(*.vcf)")
        #Updated old items from each drop-down list when a new file is opened
        if self.comboBox_2.count()>1 :
            numberOfItemsList=self.comboBox_2.count()
            numberOfItemsListMutation=self.comboBox.count()
            item=0
            itembis=1
            while item<numberOfItemsList:
                self.comboBox_2.removeItem(itembis)
                item=item+1
            item = 0
            itembis = 1
            while item<numberOfItemsListMutation:
                self.comboBox.removeItem(itembis)
                item=item+1
        else:
            pass
        self.chromosome_ref.clear()
        #Message error if the file is empty
        if os.path.getsize(nomFichier)==0:
            message="Sorry, the file seems corrupted. Check the status of the file. It seems to be empty"
            QMessageBox.question(self, "File corrupted",message)

        if nomFichier:
            QMessageBox.information(self,"TRACE", "Fichier à ouvrir:\n\n%s"%nomFichier)
            with open(nomFichier,"r") as vcf:
                file_read=vcf.readlines()
            #Reading the VCF file and creating the dictionary
            for line_vcf in file_read:
                #Read lines only after the header
                if not line_vcf.startswith("#"):
                    information=re.findall("\S+",line_vcf)
                    """
                    Instruction filling variables with a ?
                    if the file isnt correct
                    """
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
            #Message error, if there is no line after header
            if bool(self.chromosome_ref)==False:
                    message="Sorry, the file seems corrupted. Check the status of the file. It seems to have header but no data"
                    QMessageBox.question(self, "File corrupted",message)

            #Creation of drop-down lists 
            for chromosome in self.chromosome_ref:
                self.createItemsList(chromosome)
                
            for typeMutation in self.typeOfMutation():
                self.createItemsListMutation(typeMutation)
                
    #Count every chrosomome in current file
    def compteur_chromosome(self):
        compteur_chromosome=0
        for i in self.chromosome_ref:
            compteur_chromosome=compteur_chromosome+1
        return(str(compteur_chromosome))
        
    #Count every mutation in current file
    def mutationCounter(self, x):
        counter=0
        try:
            for mutation in self.chromosome_ref.get(x):
                counter=counter+1
            return counter
        except TypeError:
            message="Please select Chromosome"
            QMessageBox.question(self,"Error",message,QMessageBox.Yes)
            
    def totalMutationCounter(self):
        liste_chromosome_nb_mutation=[]
        liste_mutation=[]
        liste_chromosome=[]
        for chromosome in self.chromosome_ref:
            compteur_mutation=0
            for position in self.chromosome_ref.get(chromosome):
                compteur_mutation=compteur_mutation+1
            liste_chromosome_nb_mutation.append("Chromosome: "+str(chromosome)+" Nombre de mutation: "+str(compteur_mutation))
            liste_chromosome.append(chromosome)
            liste_mutation.append(compteur_mutation)
            
        return (liste_chromosome, liste_mutation)
        
    #Graph which contains the number of mutation for each chromosome
    def plot_mutation_par_chromosome(self):
        try:
            liste_chromosome=[]
            liste_mutation=[]
            somme=0
            moyenne=0
            for chromosome in self.totalMutationCounter()[0]:
                liste_chromosome.append(chromosome)
            for mutation in self.totalMutationCounter()[1]:
                liste_mutation.append(mutation)
                somme=somme+mutation
            moyenne=somme/len(self.totalMutationCounter()[1])
            plt.title("Number of mutation per Chromosome")
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
        except ZeroDivisionError:
            message="Please, open file"
            QMessageBox.question(self,"Error",message,QMessageBox.Yes)

    def mutationCounterPerChromosome(self):
        mutationCounter={}
        chromosome=self.comboBox_2.currentText()
        qual1=self.lineEdit_3.text()
        qual2=self.lineEdit_4.text()
        pos2=self.lineEdit.text()
        pos1=self.lineEdit_2.text()
        if self.checkBox.checkState()==True and self.checkBox_2.checkState()==True:
            try: 
                for position in self.chromosome_ref[chromosome]:
                    try:
                        if float(position)>=float(pos1) and float(position)<=float(pos2):
                            listInfo=self.chromosome_ref[chromosome].get(position)
                            try:
                                if float(listInfo[2])>=float(qual1) and float(listInfo[2])<=float(qual2):
                                    if listInfo[1] in mutationCounter:
                                        mutationCounter[listInfo[1]]=mutationCounter.get(listInfo[1])+1
                                    else:
                                        mutationCounter[listInfo[1]]=1
                                else:
                                    continue
                            except:
                                message="Please, enter the quality"
                                QMessageBox.question(self,"Error", message, QMessageBox.yes)
                        else:
                            continue
                    except:
                        message="Please, enter position"
                        QMessageBox.question(self, "Error", message,QMessageBox.Yes)

                self.plainTextEdit_2.setPlainText(self.plainTextEdit_2.toPlainText()+"\n"+"Chromosome :" +chromosome+"\n"+"######### \n")
                for mutation in mutationCounter:
                    message=self.plainTextEdit_2.toPlainText()+str(mutation)+"  "+str(mutationCounter[mutation])+"\n"
                    
                    self.plainTextEdit_2.setPlainText(message)
            except:
                message="Please, enter the right interval or right quality"
                QMessageBox.question(self,"Error",message,QMessageBox.Yes)

        if self.checkBox_2.checkState()==True and self.checkBox.checkState()==False:
            try:
                for position in self.chromosome_ref[chromosome]:
                    try:
                         if float(position)>=float(pos1) and float(position)<=float(pos2):
                            listInfo=self.chromosome_ref[chromosome].get(position)
                            if listInfo[1] in mutationCounter:
                                mutationCounter[listInfo[1]]=mutationCounter.get(listInfo[1])+1
                            else:
                                mutationCounter[listInfo[1]]=1
                         else:
                            continue
                    except:
                        message="Please, select position"
                        QMessageBox.question(self,"Error", message, QMessageBox.Yes)

                self.plainTextEdit_2.setPlainText(self.plainTextEdit_2.toPlainText()+"\n"+"Chromosome :" +chromosome+"\n"+"######### \n")
                for mutation in mutationCounter:
                    message=self.plainTextEdit_2.toPlainText()+str(mutation)+"  "+str(mutationCounter[mutation])+"\n"
                    
                    self.plainTextEdit_2.setPlainText(message)
            except:
                message="Please, select Chromosome"
                QMessageBox.question(self,"Error",message,QMessageBox.Yes)

        if self.checkBox_2.checkState()==False and self.checkBox.checkState()==True:
            try:
                for position in self.chromosome_ref[chromosome]:
                    listInfo=self.chromosome_ref[chromosome].get(position)
                    try:
                        if float(listeInfo[2])>=float(qual1) and float(listeInfo[2])<=float(qual2):
                            if listInfo[1] in mutationCounter:
                                mutationCounter[listInfo[1]]=mutationCounter.get(listInfo[1])+1
                            else:
                                mutationCounter[listInfo[1]]=1
                        else:
                            continue
                    
                    except:
                        message="Please, enter quality"
                        QMessageBox.question(self, "Error", message, QMessageBox.Yes)
                
                self.plainTextEdit_2.setPlainText(self.plainTextEdit_2.toPlainText()+"\n"+"Chromosome :"+chromosome+"\n"+"######### \n")
                for mutation in mutationCounter:
                    message=self.plainTextEdit_2.toPlainText()+str(mutation)+"  "+str(mutationCounter[mutation])+"\n"
                    
                    self.plainTextEdit_2.setPlainText(message)
            except:
                message="Please, select Chromosome"
                QMessageBox.question(self,"Error",message,QMessageBox.Yes)

        if self.checkBox_2.checkState()==False and self.checkBox.checkState()==False:
            try:
                for position in self.chromosome_ref[chromosome]:
                    listInfo=self.chromosome_ref[chromosome].get(position)
                    if listInfo[1] in mutationCounter:
                        mutationCounter[listInfo[1]]=mutationCounter.get(listInfo[1])+1
                    else:
                        mutationCounter[listInfo[1]]=1

                self.plainTextEdit_2.setPlainText(self.plainTextEdit_2.toPlainText()+"\n"+"Chromosome :"+chromosome+"\n"+"######### \n")
                for mutation in mutationCounter:
                    message=self.plainTextEdit_2.toPlainText()+str(mutation)+"  "+str(mutationCounter[mutation])+"\n"
                    
                    self.plainTextEdit_2.setPlainText(message)
            except:
                message="Please select Chromosome"
                QMessageBox.question(self,"Error",message,QMessageBox.Yes)






    #Fonction 
    def dynamicPlot(self, chromosome):
    
        
        if type(chromosome)==str:#Récupère le paramètre, le fais devenir une var type str si c'est un int
            try:
                positionLoop=self.chromosome_ref[chromosome]
                liste_position=[]
                mutation=[]
                liste_ref_mutation=[]
                liste_insert_mutation=[]
                
                for position in self.chromosome_ref[chromosome]: #boucle sur les différentes positions de la clé chromosome passer en paramètre dans la fonction
                    liste_position.append(position)#création d'une liste comprenant toutes les positions de la clé
                    mut=(self.chromosome_ref[chromosome].get(position))
                    mutation.append(mut)
                    liste_ref_mutation.append(mut[0])
                    liste_insert_mutation.append(mut[1])
                    
                    #Générateur permettant de parcourir les valeurs de la première clé, et récupérer la variable à partir de l'indice lorsque l'indice est égale à
                    #la taille total du nombre de valeur de la premiere clé
                def valueIt(x):
                    j=0
                    for i in x:
                        j=j+1
                        if j==len(x):
                            yield i #ici yield renvois i, qui correspond à la dernière valeur de la premiere clé, sous python 3 les dictionnaires garde
                                #leur ordre d'entrée, donc la derniere valeur correspond à la position la plus élevé
                        
                for i in valueIt(positionLoop):#Récupère la derniere valeurs de la liste avec le générateur
                    last=int(i)
                liste_position_percent=[]
                liste_values=[]
                
                for i in liste_position:
                    j=(int(i)*100)/int(last)
                    liste_position_percent.append(j)
                    liste_values.append(1)
                
                x=liste_position_percent
                y=liste_values
                
                position=liste_position
                fig,ax = plt.subplots()
                ax.get_xaxis().set_visible(False)
                ax.get_yaxis().set_visible(False)
                ax.set_title("Distribution of mutations on the Chromosome"+chromosome, size=13, color='Black', style='normal')
                #Size of the points, color black
                point= plt.scatter(x,y,color="black",  s=10)
                #De base les annotations ne sont pas visibiles
                annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",bbox=dict(boxstyle="round", fc="w"),arrowprops=dict(arrowstyle="->"))
                annot.set_visible(False)
                ax.legend(["Nombre de mutation: "+str(len(liste_position))+"\nNombre estimé de nucléotides: "+str(last)+"\nPourcentage de nucléotide mutant: "+str(len(liste_position)/last)]).draggable()

                #Rajouter la liste des types de mutations pour avoir en label la mutation et son type
                def update_annot(ind):
                    pos = point.get_offsets()[ind["ind"][0]]
                    annot.xy = pos
                    information = "Mutation:{},Insertion:{},Position:{}".format(",".join([liste_ref_mutation[n] for n in ind["ind"]]),",".join([liste_insert_mutation[n] for n in ind["ind"]]), ",".join([position[n] for n in ind["ind"]]))
                    annot.set_text(information)
                    
                def hover(event):
                    vis = annot.get_visible()
                    if event.inaxes == ax:
                        cont, ind = point.contains(event)
                        if cont:
                            update_annot(ind)
                            annot.set_visible(True)
                            fig.canvas.draw_idle()
                        else:
                            if vis:
                                annot.set_visible(False)
                                fig.canvas.draw_idle()
                                
                fig.canvas.mpl_connect("motion_notify_event", hover)
                img=Image.open("blanc.png")
                plt.imshow(img, zorder=0,  extent=[0.1, 105.0, -1.0, 3.0])
                plt.show()
            except KeyError:
                 message="Please select Chromosome & open file"
                 QMessageBox.question(self,"Error",message,QMessageBox.Yes)
                 
    @pyqtSlot()
    def on_actionQuitter_triggered(self):
        self.close()
    def closeEvent(self,event):
        messageConfirmation = "Are you sure you want to quit ?"
        reponse = QMessageBox.question(self,"Confirmation",messageConfirmation,QMessageBox.Yes,QMessageBox.No)
        if reponse == QMessageBox.Yes:
            event.accept()
            message="Hope it was usefull"
            QMessageBox.question(self, "Confirmation", message, QMessageBox.Yes)
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
        if  self.comboBox_3.currentIndex()==5:
            message="Dynamic graph"
            self.plainTextEdit.setPlainText(message) 
        if  self.comboBox_3.currentIndex()==6:
            message="Function which calcul the number of a type of mutation, with parameter :quality & position"
            self.plainTextEdit.setPlainText(message)
    
    #Méthode permettant de connection de la comboBox au Launcher et de lancer la bonne méthode
    def Launcher(self):
        
        if self.comboBox_3.currentIndex()==1:
            self.plainTextEdit_2.setPlainText("Current file contain "+self.compteur_chromosome() +" Chromosomes")
            
        if self.comboBox_3.currentIndex()==2:
            chromosome=self.comboBox_2.currentText()
            self.plainTextEdit_2.setPlainText("Current chromosome contain "+str(self.mutationCounter(chromosome)) +" mutations")
            
        if self.comboBox_3.currentIndex()==3:
            self.plot_mutation_par_chromosome()
        
        if self.comboBox_3.currentIndex()==4:
            chromosome=self.comboBox_2.currentText()
            self.dynamicPlot(chromosome)
        if self.comboBox_3.currentIndex()==6:
            self.mutationCounterPerChromosome()

    def Clear(self):
        self.plainTextEdit_2.clear()
