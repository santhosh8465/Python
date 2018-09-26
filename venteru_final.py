#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 22:58:28 2018

@author: santhoshreddyventeru
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from boggle_dices import Boggle_Dice
from inpu_t import Input
from boggle_checker import Boggle_checker, Word_checker

class Boggle_Game(QMainWindow):
    EXIT_CODE_REBOOT = -123
    def __init__(self):
        super().__init__()
        self.board = Boggle_Dice()
        self._list = self.board.letterboard()
        #print(self._list)
        self.boggle_check = Boggle_checker()
        #self.bo_in = Input()
        self.words = list()
        self.inpu_t = Input()
        #print(self.input)
        self.initUI()
        
    def initUI(self):
        self.centerWidget = QWidget()
        self.BTWidget = QWidget(self.centerWidget)
        self.word_widget = QWidget(self.centerWidget)
        
        self.list_widget = QWidget(self.centerWidget)
        
        
        
        
        self.centralWidgetLayout = QVBoxLayout()
        
        self.textGridLayout = QGridLayout()
        
        self.wordEnterLayout = QHBoxLayout()
        self.wordListLayout = QHBoxLayout()
        self.setCentralWidget(self.centerWidget)
        
        
        
        
        self.BTWidget.setLayout(self.textGridLayout)
        for i in range(0, 4):
            for j in range(0, 4):
                button = QPushButton(self._list[i][j])
                self.textGridLayout.addWidget(button, i, j)
                
       
        
        
        
        self.word_widget.setLayout(self.wordEnterLayout)
        self.lineEdit = QLineEdit()
        
        self.addWordBtn = QPushButton('ADD')
        
        
        
        self.wordEnterLayout.addWidget(self.lineEdit)   
        self.wordEnterLayout.addWidget(self.addWordBtn)
        input
        
        
        
        
        self.list_widget.setLayout(self.wordListLayout)
        self.wordList = QTextEdit()
        
        self.scoreBtn = QPushButton('Get Score')
        
        self.wordListLayout.addWidget(self.wordList)
        
        self.wordListLayout.addWidget(self.scoreBtn)
        
       
        
        
        self.addWordBtn.clicked.connect(self.addWordBtn_clicked)
        self.scoreBtn.clicked.connect(self.scoreBtn_clicked)
        
        
        menubar = self.menuBar()
        gameMenu = menubar.addMenu('GAME')
        
        newGame = QAction('NEW GAME', self)
        
        gameMenu.addAction(newGame)
        
        newGame.triggered.connect(self.new_game)

        
        
        self.centerWidget.setLayout(self.centralWidgetLayout)
        #self.centerWidget.setLayout(self.CentralWidgetLayout)
        self.centralWidgetLayout.addWidget(self.BTWidget)
        #self.centralWidgetLayout.addWidget(self.word_listWidget)
        self.centralWidgetLayout.addWidget(self.word_widget)
        #self.centralWidgetLayout.addWidget(self.inplistWidget)
        #self.centralWidgetLayout.addWidget(self.inputlistWidget)
        #self.centralWidgetLayout.addWidget(self.checkWidget)
        #self.centralWidgetLayout.addWidget(self.wolistWidget)
        
        self.centralWidgetLayout.addWidget(self.list_widget)
        
        # Display the GUI
        self.setGeometry(800, 800, 800, 800)
        self.setWindowTitle('BOGGLE')
        #self.setWindowIcon(QIcon('./Documents/boggle-gui/boggle.png'))
        self.setWindowIcon(QIcon('/Users/santhoshreddyventeru/Documents/boggle-gui/boggle.png'))
        self.show()
    
    # Start a new Game
    def new_game(self):
        self.board = None
        self._list = None
        self.inpu_t = None
        self.boggle_check = None
        qApp.exit(Boggle_Game.EXIT_CODE_REBOOT)
        return
        
    def addWordBtn_clicked(self):
        word_entered = self.lineEdit.text()
        if word_entered:
            self.words.append(word_entered.strip().upper())
            self.lineEdit.clear()
            self.words = list(set(self.words))
            word_list_display = '\n'.join(self.words)
            self.wordList.setText(word_list_display)
        return
    
    def scoreBtn_clicked(self):
        self.inpu_t.setlist(self.words)
        self.boggle_check.setInputProcessor(self.inpu_t)
        self.boggle_check.setSixteenDices(self.board)
        Word_checker()
        self.boggle_check.scor_e()
        reply = QMessageBox.question(self, 'Congrats','Your Score: {0} \n Play Again ?'.format(str(self.boggle_check.getScore())),QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.new_game()
        else:
            sys.exit(0)
        return
    
if __name__ == "__main__":
    currentExitCode = Boggle_Game.EXIT_CODE_REBOOT
    while currentExitCode == Boggle_Game.EXIT_CODE_REBOOT:
        app = QApplication(sys.argv)
        gui = Boggle_Game()
        currentExitCode = app.exec_()
        app = None
    
