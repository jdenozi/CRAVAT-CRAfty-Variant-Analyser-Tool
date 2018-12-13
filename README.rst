CRAVAT: Crafty Variant Analyser Tool Version 1.0
================================================
The CRAVAT project is a program designed for working with VCF file (only). The aim of CRAVAT tool is to provide easily accessible methods with GUI for working with complex genetic variation data in the form of VCF files.

This toolset can be used to perform the following operations on VCF files:

    Filter out specific Chromosome
    Compare files
    Summarize variants
    Filter out 
    Filter out specifiquely with quality and position



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

-Pillow, see https://pillow.readthedocs.io/en/5.3.x/

Installation
============
::
git clone https://github.com/jdenozi/CRAVAT-CRAfty-Variant-Analyser-Tool.git

Usage
=====
Goes to CRAVAT directory
::
python3 start_app.py


