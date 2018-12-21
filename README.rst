CRAVAT: Crafty Variant Analyser Tool Version 1.0
================================================
'CRAVAT/picture/cravatfox.jpg' 
The CRAVAT project is a program designed for working with VCF file (only). The aim of CRAVAT tool is to provide easily accessible methods with GUI for working with complex genetic variation data in the form of VCF files.

This toolset can be used to perform the following operations on VCF files:

    - Filter out specific Chromosome
    - Compare files
    - Summarize variants
    - Filter out 
    - Filter out specifiquely with quality and position



Author
======
Denozi Julien <denozi.j@gmail.com>

Python Requirements
===================

I currently recommend using Python 3.6.5 from http://www.python.org
CRAVAT is currently supported and tested on the following Python
implementations:
Python 3.5

Dependencies
============

- matplotlib, see http://matplotlib.org/ 
  CRAVAT uses this package to plot graphic. Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.
  
- Qt, see https://www.qt.io/ 
  This package is only used in GUI. It's a cross-platform application framework and widget toolkit for creating classic and embedded graphical user interfaces, and applications that run on various software and hardware platforms with little or no change in the underlying codebase, while still being a native application with native capabilities and speed.

- Pillow, see https://pillow.readthedocs.io/en/5.3.x/

Installation
============

::
git clone https://github.com/jdenozi/CRAVAT-CRAfty-Variant-Analyser-Tool.git

or unzip file
Usage
=====
Goes to CRAVAT directory
::
python3 start_app.py

Or execute cravat.exe()(first lauching is a bit long around 30 seconde)


Fonctionnality
=============
How many Chromosome file have
------------------------------
Function which calcul the current number of Chromosome in the current vcf file
Type= Text
Could be save with Ctrl-s in a file

How mutation do file have
--------------------------
Function which calcul the current number of Chromosome mutation in the current vcf file. 
Type=Text.
Could be save as text file with Ctrl-s in a file.

How many mutation do chromosome have
------------------------------------
Graphs of the current number of chromosome mutation in the current vcf file.
Type= Graph.
Color code mean that the number of mutation is above or behind the average Chromosome of the entire file.
The graph can be enlarged, save and move with the menu bar under the graph.

Dynamic visualization plot for every chromosome mutation in a chosen chromosome
-------------------------------------------------------------------------------
Dynamic graph representing the different mutations along the chromosome.
Type=Graph.
The plot could be draggable.
The graph can be enlarged, save and move with the menu bar under the graph.

Mutation filter with quality, position and mutation
---------------------------------------------------
Function which calcul the number of a type of mutation and his percentage in the current chromosome, with parameter :mutation type, quality & position.
Type=Text.
Select mutation if you want to filter the resultats only for this mutation type.
Check position or quality if you want to filter the results with its values.
If no values appear, it mean that no values corresponde with your filter.
Could be save as txt file(Ctrl-S).
Could be compare with anoter chromosome or file.
