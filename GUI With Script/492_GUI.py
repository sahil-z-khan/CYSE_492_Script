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
        loadUi(r'GUI With Script\492_GUI.ui',self)
        
        #Connect the buttons to the main functionality
        #push_Parse ~ Name of button on designer.exe
        #nmap_Scan ~ Name of method that contains action 
        self.nmap_Push.clicked.connect(self.nmap_Scan)
        
        self.db_Push.clicked.connect(self.db_scan)
        
        self.nikto_Push.clicked.connect(self.nikto_scan)

    def nmap_Scan(self): #Method to Conduct NMAP Scan
        print("Button Works")
    
    def db_scan(self): #Method to Conduct Dirbuster Scan
        print('Button Works')

    def nikto_scan(self): #Method to Conduct Dirbuster Scan
        print('Button Works')

app=QApplication(sys.argv)
mainwindow=Program()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(300)
widget.show()
app.exec_()