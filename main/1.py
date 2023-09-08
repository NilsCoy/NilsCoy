import sys 
from PyQt5 import QtWidgets 
from PyQt5 import uic
from myform1 import Ui_MainWindow
from main import *

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        
        my_Stamp = Stamp("Spyker Cars", "Голландия", "завод", "адрес")
        my_Car = Car("Spyker", "2007", "black", "sport", "$640000", my_Stamp)
        my_Staff = Staff("Фамилиия1", "Имя1", "Отчество1", "опыт работы", "зарплата")
        my_Buyer = Buyer("Фамилиия2", "Имя2", "Отчество2", "паспорт", "адрес", "город", "возраст", "пол")
        my_Sale = Sale("дата", my_Staff, my_Car, my_Buyer)
        self.node = my_Sale
        
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # подключение клик-сигнал к слоту btnClicked
        self.ui.pushButton.clicked.connect(self.btnClicked1)
        self.ui.pushButton_2.clicked.connect(self.btnClicked2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked3)
        self.ui.pushButton_4.clicked.connect(self.btnClicked4)
        self.ui.pushButton_5.clicked.connect(self.btnClicked5)

    def btnClicked1(self):
        self.ui.textBrowser.setText(str(Menu(self.node).printStamp()))
    def btnClicked2(self):
        self.ui.textBrowser_2.setText(str(Menu(self.node).printCar()))
    def btnClicked3(self):
        self.ui.textBrowser_3.setText(str(Menu(self.node).printStaff()))
    def btnClicked4(self):
        self.ui.textBrowser_4.setText(str(Menu(self.node).printBuyer()))
    def btnClicked5(self):
        self.ui.textBrowser_5.setText(str(Menu(self.node).printSale()))

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())