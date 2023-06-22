import requests
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QDialog,  QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTreeView, QLineEdit
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys


class MainCovid(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        font = QFont("Courier New", 13)
        app.setFont(font)
        self.setStyleSheet(" background-image: url('vur.jpg'); ")
        self.setWindowTitle('covid')
        self.setFixedSize(QSize(500, 600))
        self.dataView = QTreeView()
        self.dataView.move(230, 16)
        self.dataView.setFixedSize(QSize(500, 300))
        self.model = self.createMailModel(self)
        self.dataView.setModel(self.model)
        self.setCentralWidget(self.dataView)
        self.buttonLeft = QPushButton("Выгрузить список", self)
        self.buttonLeft.move(165, 340)
        self.buttonLeft.setFixedSize(QSize(180, 50))
        self.buttonLeft.clicked.connect(self.connectionToServer)
        self.buttondob = QPushButton("добавить тест", self)
        self.buttondob.move(175, 400)
        self.buttondob.setFixedSize(QSize(160, 50))
        self.buttondob.clicked.connect(self.add)
        self.buttondel = QPushButton("удалить выбранный тест", self)
        self.buttondel.move(130, 470)
        self.buttondel.clicked.connect(self.TestBib)
        self.buttondel.setFixedSize(QSize(250, 50))
        self.buttonchange = QPushButton("Изменить тест", self)
        self.buttonchange.move(155, 540)
        self.buttonchange.clicked.connect(self.change)
        self.buttonchange.setFixedSize(QSize(200, 50))

    def createMailModel(self, parent):
        model = QStandardItemModel(0, 5, parent)
        model.setHeaderData(0, Qt.Orientation.Horizontal, "Результат")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "ФИО")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Дата сдачи")
        model.setHeaderData(3, Qt.Orientation.Horizontal, "Паспорт")
        model.setHeaderData(4, Qt.Orientation.Horizontal, "ID")
        return model

    def connectionToServer(self):
        try:
            self.numrow = self.model.rowCount()
            print(self.numrow)
            self.model.removeRows(0, self.numrow)
        except Exception as e:
            print(e)
        url = 'http://127.0.0.1:8000/covid'
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            for i in range(0, len(json_data)):
                temp = (
                    json_data[i]['fields']['resultat'],
                    json_data[i]['fields']['data_sdachi'],
                    json_data[i]['fields']['FIO'],
                    json_data[i]['fields']['IO'],
                    json_data[i]['pk'],
                )
                # tree.insert("", END, values=temp)
                self.addRow(temp)

    def addRow(self, temp):
        self.model.insertRow(0)
        self.model.setData(self.model.index(0, 0), temp[0])
        self.model.setData(self.model.index(0, 1), temp[2])
        self.model.setData(self.model.index(0, 2), temp[1])
        self.model.setData(self.model.index(0, 3), temp[3])
        self.model.setData(self.model.index(0, 4), temp[4])

    def add(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Добавление теста")
        self.dialog.setFixedSize(QSize(400, 400))
        self.FIOlb = QLabel(self.dialog)
        self.FIOlb.setText("Введите ФИО")
        self.FIO = QLineEdit(self.dialog)
        self.FIO.move(0, 20)
        self.IOlb = QLabel(self.dialog)
        self.IOlb.setText("Введите паспорт")
        self.IO = QLineEdit(self.dialog)
        self.IO.move(0, 60)
        self.IOlb.move(0, 40)
        self.resultlb = QLabel(self.dialog)
        self.resultlb.setText("Введите результат теста")
        #self.result = QLineEdit(self.dialog)
        self.result = QComboBox(self.dialog)
        self.result.addItem("положительный")
        self.result.addItem("отрицательный")
        self.result.addItem("ожидание")
        self.result.move(0, 100)
        self.resultlb.move(0, 80)
        self.datalb = QLabel(self.dialog)
        self.datalb.setText("Введите дату (формата YYYY-MM-DD)")
        self.data = QLineEdit(self.dialog)
        self.data.move(0, 140)
        self.datalb.move(0, 120)
        self.buttondobaw = QPushButton("загрузить тест", self.dialog)
        self.buttondobaw.move(200, 340)
        self.buttondobaw.clicked.connect(self.add_us)
        self.dialog.exec()

    def add_us(self):
        url = "http://127.0.0.1:8000/Tests"
        res = {"resultat": str(self.result.currentText()),
               "FIO": self.FIO.text(),
               "IO": self.IO.text(),
               "data_sdachi": self.data.text()}
        response = requests.post(url, res)
        print(response.status_code)
        if response.status_code == 200:
            json_data = response.json()
            print(json_data)

    def TestBib(self):
        indexes = self.dataView.selectedIndexes()
        print(self.model.itemFromIndex(indexes[4]).text())
        url = f'http://127.0.0.1:8000/Tests/{self.model.itemFromIndex(indexes[4]).text()}'
        response = requests.delete(url)
        q = response.json()
        print(q)

    def change(self):
        self.dialogi = QDialog(self)
        self.dialogi.setWindowTitle("Изменение")
        self.dialogi.setFixedSize(QSize(400, 400))
        self.FIOlg = QLabel(self.dialogi)
        self.FIOlg.setText("Введите ФИО")
        self.FIOl = QLineEdit(self.dialogi)
        self.FIOl.move(0, 20)
        self.IOlg = QLabel(self.dialogi)
        self.IOlg.setText("Введите паспорт")
        self.IOl = QLineEdit(self.dialogi)
        self.IOl.move(0, 60)
        self.IOlg.move(0, 40)
        self.resultlg = QLabel(self.dialogi)
        self.resultlg.setText("Введите результат теста")
        self.resultl = QLineEdit(self.dialogi)
        self.resultl.move(0, 100)
        self.resultlg.move(0, 80)
        self.datalg = QLabel(self.dialogi)
        self.datalg.setText("Введите дату сдачи")
        self.datal = QLineEdit(self.dialogi)
        self.datal.move(0, 140)
        self.datalg.move(0, 120)
        self.buttonizmen = QPushButton("загрузить тест", self.dialogi)
        self.buttonizmen.move(200, 340)

        self.buttonizmen.clicked.connect(self.chan)
        self.dialogi.exec()

    def chan(self):
        indexes = self.dataView.selectedIndexes()
        print(self.model.itemFromIndex(indexes[4]).text())
        url = f"http://127.0.0.1:8000/Tests/{self.model.itemFromIndex(indexes[4]).text()}"
        res = {"resultat": self.resultl.text(),
               "FIO": self.FIOl.text(),
               "IO": self.IOl.text(),
               "data_sdachi": self.datal.text()}
        response = requests.put(url, res)
        print(response.status_code)
        if response.status_code == 200:
            json_data = response.json()
            print(json_data)
            print(res)
        print(self.resultl.text())


app = QApplication(sys.argv)

window_com = MainCovid()
window_com.show()


app.exec()
