#!/bin/env python3
# -*- coding: utf-8 -*-

'''
CRAVAT: crafty variant analyser tool

The file contain all the graphical methods connected to the data analysis method
'''


#LIBRARY
import dialogue
import os
from PyQt5.QtWidgets import *
from ui_main_window import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot
import re
import matplotlib.pyplot as plt
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import numpy.random
import matplotlib.pyplot as plt
""""
Declaration of the class About
contain information about program and author
"""

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
    Save text of thje right box in GUI  in a file

    """
    @pyqtSlot() 
    def file_save(self):
        (name,filte) = QFileDialog.getSaveFileName(self, 'Save File', filter="txt(*.txt)")
        file = open(name,'w')
        text = self.plainTextEdit_2.toPlainText()
        file.write(text)
        file.close()
    """
    Open the file tree with a filter on the VCF file
    Creation of the chromosome dictionnary, containing a position dictionnary
    with the value of a list containing
    """
    @pyqtSlot()
    def on_actionOuvrir_triggered(self):
        (nomFichier,filtre) = QFileDialog.getOpenFileName(self,"New_file",  filter="vcf(*.vcf)")
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
        if os.path.getsize(nomFichier)==0:
            message="Sorry, the file seems corrupted. Check the status of the file. It seems to be empty"
            QMessageBox.question(self, "File corrupted",message)

        if nomFichier:
            QMessageBox.information(self,"TRACE", "File to open:\n\n%s"%nomFichier)
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
        
    #Count every mutation in a Chromosome(x=chromosome select in the drop-down list)
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
            liste_chromosome_nb_mutation.append("Chromosome: "+str(chromosome)+" Mutation number: "+str(compteur_mutation))
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
            plt.ylabel('Mutation number')
            plt.show()
        except ZeroDivisionError:
            message="Please, open file"
            QMessageBox.question(self,"Error",message,QMessageBox.Yes)

    #Function that allows to count the number of mutations of a chromosome with a filter on the quality and the position
    def mutationCounterPerChromosome(self):
        mutationCounter={}
        #correspond à la liste déroulante de chromosome
        chromosome=self.comboBox_2.currentText()
        #corresponds to box 1 of the quality
        qual1=self.lineEdit_3.text().strip().strip("'")
        #corresponds to box 2 of the quality
        qual2=self.lineEdit_4.text().strip().strip("'")
        #correspond to box 1 of the intervalle
        pos2=self.lineEdit.text().strip().strip("'")
        #corresponde to box 2 of the intervalle
        pos1=self.lineEdit_2.text()
        #check if the box is ticked

        if self.checkBox.isChecked()==True and self.checkBox_2.isChecked()==True:
            try: 
                for position in self.chromosome_ref[chromosome]:
                    try:
                        if position!="" and position !=".":
                            if float(position)>=float(pos1) and float(position)<=float(pos2):
                                listInfo=self.chromosome_ref[chromosome].get(position)
                                quality=listInfo[2]#correspond to quality in vcf file
                                mutation=listInfo[1]#correspond to mutation in vcf file
                                try:
                                    if self.comboBox.currentIndex()!=0:
                                        if float(quality)>=float(qual1) and float(quality)<=float(qual2)\
                                                and mutation==self.comboBox.currentText():
                                                    if mutation in mutationCounter:
                                                        mutationCounter[mutation]=mutationCounter.get(mutation)+1
                                                    else:
                                                        mutationCounter[mutation]=1
                                    else:
                                        if float(quality)>=float(qual1) and float(quality)<=float(qual2):
                                            if listInfo[1] in mutationCounter:
                                                mutationCounter[mutation]=mutationCounter.get(mutation)+1
                                            else:
                                                mutationCounter[mutation]=1
                                        else:
                                            continue
                                except:
                                    message="Please, enter the quality"
                                    QMessageBox.question(self,"Error", message, QMessageBox.yes)
                                    break
                        else:
                            message="Quality seems to be empty or deteriorate. Please checjk the validity of your file"
                            QMessageBox.question(self,"Error",message,QMessageBox.Yes)
                    except:
                        message="Please, enter position"
                        QMessageBox.question(self, "Error", message,QMessageBox.Yes)
                        break

                self.plainTextEdit_2.setPlainText(self.plainTextEdit_2.toPlainText()+"\n"+"Chromosome :" +chromosome+"\n#Mutation\t#tMutation number\t#Mutation percent\n")
                for mutation in mutationCounter:
                    message=self.plainTextEdit_2.toPlainText()+str(mutation)+"\t"+str(mutationCounter[mutation])+"\t"+str(mutationCounter[mutation]/self.mutationCounter(chromosome)*100)+"%\n "
                    self.plainTextEdit_2.setPlainText(message)
            except:
                message="Please select Chromosome"
                QMessageBox.question(self,"Error",message,QMessageBox.Yes)
                

        if self.checkBox_2.isChecked()==True and self.checkBox.isChecked()==False:
            #try:
            for position in self.chromosome_ref[chromosome]:
                #try:
                listInfo=self.chromosome_ref[chromosome].get(position)
                mutation=listInfo[1]
                quality=listInfo[2]
                if self.comboBox.currentIndex()!=0:
                    if float(position)>=float(pos1) and float(position)<=float(pos2)and mutation==self.comboBox.currentText():
                        if mutation in mutationCounter:
                            mutationCounter[mutation]=mutationCounter.get(mutation)+1
                        else:
                            mutationCounter[mutation]=1
                    else:
                        continue

                
                else:
                     if float(position)>=float(pos1) and float(position)<=float(pos2):
                        listInfo=self.chromosome_ref[chromosome].get(position)
                        mutation=listInfo[1]
                        if mutation in mutationCounter:
                            mutationCounter[mutation]=mutationCounter.get(mutation)+1
                        else:
                            mutationCounter[mutation]=1
                     else:
                        continue
                  
                #except:
                    #message="Please, select position"
                    #QMessageBox.question(self,"Error", message, QMessageBox.Yes)
                    #break

            self.plainTextEdit_2.setPlainText(self.plainTextEdit_2.toPlainText()+"\n"+"Chromosome :" +chromosome+"\n"+"#Mutation\t#tMutation number\t#Mutation percent\n")
            for mutation in mutationCounter:
                message=self.plainTextEdit_2.toPlainText()+str(mutation)+"\t"+str(mutationCounter[mutation])+"\t "+str(mutationCounter[mutation]/self.mutationCounter(chromosome)*100)+"%\n"
                
                self.plainTextEdit_2.setPlainText(message)
            #except:
                #message="Please, select Chromosome"
                #QMessageBox.question(self,"Error",message,QMessageBox.Yes)

        if self.checkBox_2.isChecked()==False and self.checkBox.isChecked()==True:
            try:
                for position in self.chromosome_ref[chromosome]:
                    listInfo=self.chromosome_ref[chromosome].get(position)
                    quality=listInfo[2]
                    mutation=listInfo[1]
                    try:
                        if quality!="" and quality!='.':
                            if self.comboBox.currentText!=0:
                                if float(quality)>=float(qual1) and float(quality)<=float(qual2)and mutation==self.comboBox.currentText():
                                    if mutation in mutationCounter:
                                        mutationCounter[mutation]=mutationCounter.get(mutation)+1
                                    else:
                                        mutationCounter[mutation]=1
                            else:
                                if float(quality)>=float(qual1) and float(quality)<=float(qual2):
                                    if [mutation] in mutationCounter:
                                        mutationCounter[mutation]=mutationCounter.get(mutation)+1
                                    else:
                                        mutationCounter[mutation]=1

                        else:
                            message="Quality seems to be empty or deteriorate, please check the validity of your file"
                            QMessageBox.question(self,"Error", message,QMessageBox.Yes)
                            break
                    except:
                        message="Please, enter quality"
                        QMessageBox.question(self, "Error", message, QMessageBox.Yes)
                        break
                
                self.plainTextEdit_2.setPlainText(self.plainTextEdit_2.toPlainText()+"\n"+"#Chromosome :"+chromosome+"\n"+"#Mutation\t#Mutation number\t#Mutation percent \n")
                for mutation in mutationCounter:
                    message=self.plainTextEdit_2.toPlainText()+str(mutation)+"\t"+str(mutationCounter[mutation])+"\t"+str(mutatationCounter[mutation]/self.mutationCounter(chromosome)*100)+"%\n"
                    
                    self.plainTextEdit_2.setPlainText(message)
            except:
                message="Please, select Chromosome"
                QMessageBox.question(self,"Error",message,QMessageBox.Yes)

        if self.checkBox_2.isChecked()==False and self.checkBox.isChecked()==False:
            try:
                if self.comboBox.currentIndex()!=0:
                    for position in self.chromosome_ref[chromosome]:
                        listInfo=self.chromosome_ref[chromosome].get(position)
                        mutation=listInfo[1]
                        if mutation==self.comboBox.currentText():
                            if mutation in mutationCounter:
                                mutationCounter[mutation]=mutationCounter.get(mutation)+1
                            else:
                                mutationCounter[mutation]=1
                    

                else:
                    for position in self.chromosome_ref[chromosome]:
                        listInfo=self.chromosome_ref[chromosome].get(position)
                        mutation=listInfo[1]
                        if mutation in mutationCounter:
                            mutationCounter[mutation]=mutationCounter.get(mutation)+1
                        else:
                            mutationCounter[mutation]=1

                self.plainTextEdit_2.setPlainText(self.plainTextEdit_2.toPlainText()+"\n"+"#Chromosome :"+chromosome+"\n"+ "#Mutation\t#tMutation number\t#Mutation percent\n")
                for mutation in mutationCounter:
                    message=self.plainTextEdit_2.toPlainText()+str(mutation)+"\t"+str(mutationCounter[mutation])+"\t"+str(mutationCounter[mutation]/self.mutationCounter(chromosome)*100)+"%"+"\n"
                    
                    self.plainTextEdit_2.setPlainText(message)
            except:
                message="Please select Chromosome"
                QMessageBox.question(self,"Error",message,QMessageBox.Yes)






    #Dynamic graph representing the different mutations along the chromosome
    def dynamicPlot(self, chromosome):
        if type(chromosome)==str:
            try:
                positionLoop=self.chromosome_ref[chromosome]
                liste_position=[]
                mutation=[]
                liste_ref_mutation=[]
                liste_insert_mutation=[]
                
                for position in self.chromosome_ref[chromosome]:
                    liste_position.append(position)
                    mut=(self.chromosome_ref[chromosome].get(position))#ecovers the mutations of the position
                    mutation.append(mut)#add mutation
                    liste_ref_mutation.append(mut[0])#add reference
                    liste_insert_mutation.append(mut[1])#add the insertion, exemple= <INS:ALU>
                    
                    '''
                    Generator to browse the values of the first key,
                    and retrieve the variable from the index when index is equal 
                    to the total size of the number of value of the first key
                    '''
                def valueIt(x):
                    j=0
                    for i in x:
                        j=j+1
                        if j==len(x):
                            yield i 

                #Get the last value from the list with the generator
                for i in valueIt(positionLoop):
                    last=int(i)

                #Calculate the percentage of each mutation
                liste_position_percent=[]
                liste_values=[]
                for i in liste_position:
                    j=(int(i)*100)/int(last)
                    liste_position_percent.append(j)
                    liste_values.append(1)

                #Initialize the values of the y and x axis
                x=liste_position_percent
                y=liste_values
                
                position=liste_position
                fig,(ax,ax2) = plt.subplots(nrows=2, ncols=1,sharex=False)
                ax.get_xaxis().set_visible(False)
                ax.get_yaxis().set_visible(False)
                ax2.get_xaxis().set_visible(False)
                ax2.get_yaxis().set_visible(False)

                ax.set_title("Distribution of mutations on the Chromosome"+chromosome+"\n \n", size=13, color='Black', style='normal')
                #Size of the points, color black
                point= ax.scatter(x,y,color="black",  s=10)
                #De base les annotations ne sont pas visibiles
                annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",bbox=dict(boxstyle="round", fc="w"),arrowprops=dict(arrowstyle="->"))
                annot.set_visible(False)
                ax.legend(["Nombre de mutation: "+str(len(liste_position))+"\nNombre estimé de nucléotides: "+str(last)+"\nPourcentage de nucléotide mutant: "+str(len(liste_position)/last)]).draggable()

               # Add the list of types of mutations to label the mutation and its type
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
                img=Image.open("picture/blanc.png")


                #New plot heat map
                plt.imshow(img,zorder=0,extent=[0.1, 105.0, -1.0, 3.0])
                # Create heatmap
                heatmap, xedges, yedges = np.histogram2d(y, x, bins=(1,100))
                 
                # Plot heatmap
                #.plt.clf()
                #plt.title('HeatMap')
                #plt.ylabel('y')
                #plt.xlabel('x')
              # need a colorbar to show the intensity scale
                img= plt.imshow(heatmap, extent=[0.1, 105.0, -1.0, 3.0],facecolor='hot)
                plt.colorbar(img)
                fig.subplots_adjust(hspace=0)
                plt.show()


            except KeyError:
                 message="Please select Chromosome & open file"
                 QMessageBox.question(self,"Error",message,QMessageBox.Yes)
                 
    #Function to close the window with an event asking for confirmation of the action             
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
            
    #updated information about the functions selected in the drop-down list        
    def updateText(self, message):
        self.plainTextEdit.clear()
        if self.comboBox_3.currentIndex()==0:
            message="Open file before launch any function.\n\
                This section provide informations about chosen method.\n\
                Dont forget to read every parameter the function need.\n\
                Clear button allow you to clean the entire box.\n\
                Don't forget, you can save and compare every informations in the box until you don't clear. "
            self.plainTextEdit.setPlainText(message )
        if self.comboBox_3.currentIndex()==1:
            message="Function which calcul the current number of Chromosome in the current vcf file \n\
            Type= Text\n\
            Could be save with Ctrl-s in a file"
            self.plainTextEdit.setPlainText(message )

        if self.comboBox_3.currentIndex()==2:
            message="Function which calcul the current number of Chromosome mutation in the current vcf file. \n\
            Type=Text.\n\
            Could be save as text file with Ctrl-s in a file."
            self.plainTextEdit.setPlainText(message )

        if self.comboBox_3.currentIndex()==3:
            message="Graphs of the current number of chromosome mutation in the current vcf file. \n\
            Type= Graph.\n\
            Color code mean that the number of mutation is above or behind the average Chromosome of the entire file.\n\
            The graph can be enlarged, save and move with the menu bar under the graph"
            self.plainTextEdit.setPlainText(message )


        if  self.comboBox_3.currentIndex()==4:
            message="Dynamic graph representing the different mutations along the chromosome.\n\
            Type=Graph.\n\
            The plot could be draggable.\n\
            The graph can be enlarged, save and move with the menu bar under the graph."
            self.plainTextEdit.setPlainText(message) 

        if  self.comboBox_3.currentIndex()==5:
            message="Function which calcul the number of a type of mutation and his percentage in the current chromosome, with parameter :mutation type, quality & position.\n\
            Type=Text.\n\
            Select mutation if you want to filter the resultats only for this mutation type. \n\
            Check position or quality if you want to filter the results with its values.\n\
            If no values appear, it mean that no values corresponde with your filter.\n\
            Could be save as txt file(Ctrl-S).\n\
            Could be compare with anoter chromosome or file."
            self.plainTextEdit.setPlainText(message)

    #Method to connect a box to the launcher and launch the right method
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

        if self.comboBox_3.currentIndex()==5:
            self.mutationCounterPerChromosome()
    #Clear the right box
    def Clear(self):
        self.plainTextEdit_2.clear()

    #Open window about the program
    def About(self):
        widget=QDialog(self)
        ui=dialogue.Dialog()
        ui.setupUi(widget)
        widget.exec_()
    
