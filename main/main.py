import pickle
import time

'''Класс для сохранений данных'''
class PersistenceData(object):
    
    '''Метод для сохранения данных'''    
    @staticmethod
    def serialize(data,name):
        with open(('data' + '\\' + name + '.txt'), 'wb') as f:
            pickle.dump(data, f)
        f.closed
        
    '''Метод для загрузки данных'''    
    @staticmethod
    def deserialize(name):
        with open(('data' + '\\' + name + '.txt'), 'rb') as f:
            data = pickle.load(f)
        f.closed
        return data

'''Класс марки'''
class Stamp():
    def __init__(self,name,country,factory,address):
        self.__name = name
        self.__country = country
        self.__factory = factory
        self.__address = address
        self.stamp = name
    #def Print(self):
    #    print("Stamp( " + str(self.name) + ", " + str(self.country) + ", " + str(self.factory) + ", " + str(self.address) + " )")

    def __str__(self):
        return ' Марка авто: {0} \n Страна: {1} \n Завод: {2} \n Адрес: {3} '.format(self.__name, self.__country, self.__factory, self.__address)
    
    def __get__(self, instance, owner):
        return self.__name
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('name is str!')
        else:
            self.__name = value

    #def __del__(self):
    #    print("Class Stamp() destroyed!")

class Car(Stamp):
    '''Класс машины'''
    def __init__(self,name,age,color,category,price,Stamp = None):
        self.name = name
        #Stamp.__init__(stamp)
        #super(Car, self).get_stamp(stamp)
        #self.stamp = Stamp.get_stamp(self)
        self.age = age
        self.color = color
        self.category = category
        self.price = price
        self.car = ""
        self.StampVar = Stamp
        self.stamp = Stamp.stamp
        self.data = []

    def Change(self, price):
        self.price = price
        self.data.append(Car(self.name, self.age, self.color, self.category, price, self.car, self.StampVar))

    def Print(self,value):
        #print("Car( " + str(self.name) + ", " + str(self.stamp) + ", " + str(self.age) + ", " + str(self.color) + ", " + str(self.category) + ", " + str(self.price) + " 
        print(value)

    def __str__(self):
        return ' Название авто: {0} \n Возраст: {1} \n Цвет: {2} \n Марка: {3} \n Категория: {4} \n Цена: {5} '.format(self.name, self.age, self.color, self.stamp, self.category, self.price)
    
    def __get__(self, instance, owner):
        return self.price
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('name is str!')
        else:
            self.name = value
    
    def __add__(self, value):
        self.price += value
        return self.price
    
    def __call__(self, value):
        self.price = value
        return self.price

    def __del__(self):
        print("Class Car() destroyed!")

'''Класс работника'''
class Staff():
    def __init__(self,F,I,O,exp,salary):
        self.__F = F
        self.__I = I
        self.__O = O
        self.__exp = exp
        self.__salary = salary
        self.staff = ""
        self.__data = []
        self.name = F + " " + I + " " + O

    def Change(self, exp, salary):
        self.__salary = salary
        self.__exp = exp
        self.__data.append(Staff(self.__F, self.__I, self.__O, exp, salary, self.staff))

    def Print(self,value):
        #print("Staff( " + str(self.F) + ", " + str(self.I) + ", " + str(self.O) + ", " + str(self.exp) + ", " + str(self.salary) + " )")
        print(value)

    def __str__(self):
        return ' ФИО: {0} {1} {2} \n Стаж работы: {3} \n Зарплата: {4} '.format(self.__F, self.__I, self.__O, self.__exp, self.__salary)
    
    def __get__(self, instance, owner):
        return self.name
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('name is str!')
        else:
            self.name = value
    
    def __add__(self, value):
        self.__salary += value
        return self.__salary
    
    def __call__(self, value):
        self.__salary = value
        return self.__salary

    #def __del__(self):
    #    print("Class Staff() destroyed!")

'''Класс покупателя''' 
class Buyer():
    def __init__(self,F,I,O,passport,address,city,age,pol):
        self.__F = F
        self.__I = I
        self.__O = O
        self.__passport = passport
        self.__address = address
        self.__city = city
        self.__age = age
        self.__pol = pol
        self.buyer = ""
        self.name = self.__F + " " + self.__I + " " + self.__O

    def Print(self,value):
        #print("Buyer( " + str(self.F) + ", " + str(self.I) + ", " + str(self.O) + ", " + str(self.passport) + ", " + str(self.address) + ", " + str(self.city) + ", " + str(self.age) + ", " + str(self.pol) + " )")
        print(value)

    def __str__(self):
        return ' ФИО покупателя: {0} {1} {2} \n Адрес проживания: {3} \n Город: {4} \n Возраст: {5} \n Пол: {6} '.format(self.__F, self.__I, self.__O, self.__address, self.__city, self.__age, self.__pol)
    
    def __get__(self, instance, owner):
        return self.name
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('name is str!')
        else:
            self.__name = value

    def __del__(self):
        print("Class Buyer() destroyed!")


'''Класс покупки'''
class Sale():
    
    def __init__(self,date, staff, car, buyer):
        self.date = date
        self.Staff_ = staff
        self.Car_ = car
        self.Buyer_ = buyer

    #def Print(self):
    #    print("Sale( " + str(self.date) + ", " + str(self.staff) + ", " + str(self.car) + ", " + str(self.buyer) + " )")

    def __str__(self):
        return ' Сотрудник: {0} \n Название машины: {1} \n Покупатель: {2} \n Дата: {3} '.format(self.Staff_.name, self.Car_.name, self.Buyer_.name, self.date)

    def __del__(self):
        print("Class Sale() destroyed!")

class Menu():
    def __init__(self,my_Sale = None):
        self.my_Sale = my_Sale
    def printSale(self):
        #print("Sale( " + str(self.my_Sale.date) + ", " + str(self.my_Sale.Staff_) + ", " + str(self.my_Sale.Car_) + ", " + str(self.my_Sale.Buyer_) + " )")
        print(self.my_Sale)
        return self.my_Sale
    def printCar(self):
        print(self.my_Sale.Car_)
        return self.my_Sale.Car_
    def printStaff(self):
        print(self.my_Sale.Staff_)
        return self.my_Sale.Staff_
    def printBuyer(self):
        print(self.my_Sale.Buyer_)
        return self.my_Sale.Buyer_
    def printStamp(self):
        print(self.my_Sale.Car_.StampVar)
        return self.my_Sale.Car_.StampVar
    def run(self):
        choice = 0
        choices = {
        1 : lambda : self.printSale(),
        2 : lambda : self.printCar(),
        3 : lambda : self.printStaff(),
        4 : lambda : self.printBuyer(),
        5 : lambda : self.printStamp()
        }
        while 6 > choice >= 0:
            print()
            print('1. print Sale')
            print('2. print Car')
            print('3. print Staff')
            print('4. print Buyer')
            print('5. print Stamp')
            print('6. EXIT')
            print('choose:')
            choice = int(input())
            if choice in choices:
                choices[choice]()
            time.sleep(5)


if __name__ == '__main__':
    print()
    Menu(Sale("дата", Staff("Фамилиия","Имя","Отчество","опыт работы","зарплата"), Car("машина","год производства","цвет","категория","цена",Stamp("название","страна","завод","адрес")), Buyer("Фамилиия","Имя","Отчество","паспорт","адрес","город","возраст","пол"))).run()