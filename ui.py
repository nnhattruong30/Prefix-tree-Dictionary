import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from dictionary import *


class App(QMainWindow):
    def __init__(self, my_dict):
        super().__init__()
        self.my_dict = my_dict
        self.title = 'My Dictionary'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.resize(500, 380)

        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

        #self.setGeometry(self.left, self.top, self.width, self.height)
        
        QLabel('Word:', self).move(20,0)
        self.textbox_search = QLineEdit(self)
        self.textbox_search.move(20, 30)
        self.textbox_search.resize(350,30)
        self.textbox_search.setPlaceholderText('Type the word here and press Enter')
        self.textbox_search.setCompleter(self.autoCompleteWord())
        self.textbox_search.returnPressed.connect(self.onClickSearchButton)

        self.label_message = QLabel('', self)
        self.label_message.move(20, 60)
        self.label_message.resize(350, 20)

        self.button_ser = QPushButton('Search', self)
        self.button_ser.move(380,30)
        self.button_ser.clicked.connect(self.onClickSearchButton)

        QLabel('Mean:', self).move(20,80)
        self.textbox_mean = QTextEdit(self)
        self.textbox_mean.move(20, 110)
        self.textbox_mean.resize(460,200)
        self.textbox_mean.setReadOnly(True)

        self.button_add = QPushButton('Add word', self)
        self.button_add.move(20,330)
        self.button_add.clicked.connect(self.onClickAddButton)
        self.window_add = None

        self.button_del = QPushButton('Delete word', self)
        self.button_del.move(380,330)
        self.button_del.clicked.connect(self.onClickDeleteButton)
        self.window_del = None

        self.show()

    def autoCompleteWord(self):
        query = self.textbox_search.text()
        list_sug = self.my_dict.getSuggestion(query)
        completer = QCompleter(list_sug)
        return completer

    @pyqtSlot()
    def onClickSearchButton(self):
        word = self.textbox_search.text()
        word = word.lower()
        if word == '':
            self.label_message.setText("<font color='red'>Your word is empty.</font>")
        else:
            mean = self.my_dict.searchWord(word)
            self.textbox_mean.setText(mean)
            self.label_message.setText('')
            if mean == '':
                self.label_message.setText("<font color='red'>Your word does not exist in dictionary.</font>")
    
    @pyqtSlot()
    def onClickAddButton(self):
        if self.window_add == None:
            self.window_add = AddForm(self)
        self.window_add.show()
        self.textbox_search.setText('')
        self.textbox_mean.setText('')
        self.hide()

    @pyqtSlot()    
    def onClickDeleteButton(self):
        if self.window_del == None:
            self.window_del = DeleteForm(self)
        self.window_del.show()
        self.textbox_search.setText('')
        self.textbox_mean.setText('')
        self.hide()

    def closeEvent(self, event):
        self.my_dict.saveStructure()
        event.accept()

class AddForm(QWidget):
    def __init__(self, parent = None):
        super(QWidget, self).__init__(parent)
        self.title = 'Add word'
        self.initForm()

    def initForm(self):
        self.setWindowTitle(self.title)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.Window)
        self.resize(500, 370)

        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

        QLabel('Word:', self).move(20,10)
        self.textbox_word = QLineEdit(self)
        self.textbox_word.move(20, 30)
        self.textbox_word.resize(460,30)

        QLabel('Mean:', self).move(20,70)
        self.textbox_mean = QLineEdit(self)
        self.textbox_mean.move(20, 90)
        self.textbox_mean.resize(460,200)
        self.textbox_mean.setAlignment(QtCore.Qt.AlignTop)

        self.label_message = QLabel('', self)
        self.label_message.move(20, 300)
        self.label_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_message.resize(460, 20)

        self.button_add = QPushButton('Add', self)
        self.button_add.move(150,330)
        self.button_add.clicked.connect(self.onClickAddButton)

        self.button_cancel = QPushButton('Quit', self)
        self.button_cancel.move(280,330)
        self.button_cancel.clicked.connect(self.close)

    def onClickAddButton(self):
        word = self.textbox_word.text()
        if word == '': 
            self.label_message.setText("<font color='red'>Word is empty.</font>")
            return
        mean = self.textbox_mean.text()
        if mean == '': 
            self.label_message.setText("<font color='red'>Mean is empty.</font>")
            return
        mean_in_dict = self.parent().my_dict.searchWord(word)
        if mean_in_dict == '': 
            self.parent().my_dict.addOneWord(word, mean)
            QMessageBox.information(self,'Dictionary message', 'Add successfully.', QMessageBox.Ok)
        else:
            button_reply = QMessageBox.warning(self, 'Dictionary message', 'Your word already exists. Do you want to replace it?', QMessageBox.Yes, QMessageBox.No)
            if button_reply == QMessageBox.Yes:
                self.parent().my_dict.addOneWord(word, mean)
                QMessageBox.information(self,'Dictionary message', 'Add successfully.', QMessageBox.Ok)
        self.textbox_word.setText('')
        self.textbox_mean.setText('')
        self.label_message.setText('')

    def closeEvent(self, event):
        self.parent().textbox_search.setCompleter(self.parent().autoCompleteWord())
        self.parent().show()
        self.textbox_mean.setText('')
        self.textbox_word.setText('')
        event.accept()

class DeleteForm(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('Delete word')
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.Window)

        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

        QLabel('Word:', self).move(20,10)
        self.textbox_word = QLineEdit(self)
        self.textbox_word.move(20, 30)
        self.textbox_word.resize(200,30)

        self.button_del = QPushButton('Delete', self)
        self.button_del.move(20,80)
        self.button_del.clicked.connect(self.onClickDeleteButton)

        self.button_cancel = QPushButton('Quit', self)
        self.button_cancel.move(130,80)
        self.button_cancel.clicked.connect(self.close)

    def onClickDeleteButton(self):
        word = self.textbox_word.text()
        mean_in_dict = self.parent().my_dict.searchWord(word)
        if mean_in_dict == '':
            QMessageBox.information(self, 'Dictionary message', 'Your word does not exist.', QMessageBox.Ok)
        else:
            button_reply = QMessageBox.warning(self, 'Dictionary message', 'Are you sure you want to delete this word?', QMessageBox.No, QMessageBox.Yes)
            if button_reply == QMessageBox.Yes:
                self.parent().my_dict.deleteOneWord(word)
                QMessageBox.information(self, 'Dictionary message', 'Delete successfully.', QMessageBox.Ok)
        self.textbox_word.setText('')

    def closeEvent(self, event):
        self.textbox_word.setText('')
        self.parent().textbox_search.setCompleter(self.parent().autoCompleteWord())
        self.parent().show()
        event.accept()


    