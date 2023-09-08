
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from main import *



class Scene():
    def __init__(self, root):
        
        my_Stamp = Stamp("Spyker Cars", "Голландия", "завод", "адрес")
        my_Car = Car("Spyker", "2007", "black", "sport", "$640000", my_Stamp)
        my_Staff = Staff("Фамилиия1", "Имя1", "Отчество1", "опыт работы", "зарплата")
        my_Buyer = Buyer("Фамилиия2", "Имя2", "Отчество2", "паспорт", "адрес", "город", "возраст", "пол")
        my_Sale = Sale("дата", my_Staff, my_Car, my_Buyer)
        self.root_node = my_Sale
        
        self.root = root
        self.root.title('АвтоShop')
        self.root.geometry('800x600')
        self.root.resizable(width=False, height=False)
        
        self.background = ttk.Notebook(self.root)
        
        self.stamp = tk.Frame(self.background, bg='white')
        self.stamp.pack(expand=True, fill='both')
        self.background.add(self.stamp, text='Марка машины')

        self.newImage1 = ImageTk.PhotoImage(Image.open('images/1.jpg'))        
        self.create_page(Menu(self.root_node).printStamp(), self.stamp, self.newImage1)
        
        self.car = tk.Frame(self.background, bg='white')
        self.car.pack(expand=True, fill='both')
        self.background.add(self.car, text='Машина')

        self.newImage2 = ImageTk.PhotoImage(Image.open('images/2.jpg'))        
        self.create_page(str(Menu(self.root_node).printCar()), self.car, self.newImage2)
        
        self.seller = tk.Frame(self.background, bg='white')
        self.seller.pack(expand=True, fill='both')
        self.background.add(self.seller, text='Продавец')
        
        self.create_page(str(Menu(self.root_node).printStaff()), self.seller, '')
        
        self.Buyer = tk.Frame(self.background, bg='white')
        self.Buyer.pack(expand=True, fill='both')
        self.background.add(self.Buyer, text='Покупатель')
        
        self.create_page(Menu(self.root_node).printBuyer(), self.Buyer, '')
        
        self.end = tk.Frame(self.background, bg='white')
        self.end.pack(expand=True, fill='both')
        self.background.add(self.end, text='Вывод товара')

        self.newImage3 = ImageTk.PhotoImage(Image.open('images/3.jpg'))
        self.create_page(Menu(self.root_node).printSale(), self.end, self.newImage3)

        self.background.place(relx=0,rely=0,relheight=1,relwidth=1)
        
    def create_page(self, arg, node, image):
        newLabel = tk.Label(node, height = 15, width=40, relief='solid', font="Courier 10", text = '')
        newButton = tk.Button(node, font="Courier 15", text = 'Посмотреть информацию', command = lambda label=newLabel, arg=arg: self.btn_pressed(label, arg))
        
        newLabel.place(x=20, y=150)
        newButton.place(x=50, y=80)

        if image != '':
            newImageLabel = tk.Label(node, image = image)
            newImageLabel.place(x=370, y=120)         

    def btn_pressed(self, label, arg):
        label.config(text=arg)

master = tk.Tk()
start = Scene(master)
master.mainloop()
# New github data