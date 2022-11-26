import sys
from tkinter import dialog
from xml.dom import UserDataHandler
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Program(QDialog):
    def __init__(self): #Main Header
        super(Program,self).__init__()
        #Load the UI into the python
        loadUi(r'492_GUI.ui',self)
        
        #Connect the buttons to the main functionality
        #push_Parse ~ Name of button on designer.exe
        #on_click ~ Name of method that contains action 
        self.push_Parse.clicked.connect(self.on_click)
        

    def on_click(self): #Method Parsing Through Excel
        print("Button Works")


app=QApplication(sys.argv)
mainwindow=Program()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(300)
widget.show()
app.exec_()