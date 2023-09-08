from main import *
import unittest

class TestCar(unittest.TestCase):
    def setUp(self):
        self.a = Car("Spyker","Spyker Cars","2007","black","sport","$640000")
        PersistenceData.serialize(self.a, 'Car')
        print(PersistenceData.deserialize('Car'))

    def test_base(self):
        self.assertEqual(self.a.name, "Spyker", "Название машины не определено")
        self.assertEqual(self.a.stamp, "Spyker Cars", "Марка машины не определен")
        self.assertEqual(self.a.age, "2007", "Год машины не определен")
        self.assertEqual(self.a.color, "black", "Цвет машины не определен")
        self.assertEqual(self.a.category, "sport", "Категория машины не определен")
        self.assertEqual(self.a.price, "$640000", "Цена машины не определена")
        with self.assertRaises(TypeError):
            pass

class TestStamp(unittest.TestCase):
    def setUp(self):
        self.a = Stamp("название","страна","завод","адрес")
        PersistenceData.serialize(self.a, 'Stamp')
        print(PersistenceData.deserialize('Stamp'))

    def test_base(self):
        self.assertEqual(self.a.name, "название", "Название марки не определено")
        self.assertEqual(self.a.country, "страна", "Страна марки не определен")
        self.assertEqual(self.a.factory, "завод", "Заврд марки не определен")
        self.assertEqual(self.a.address, "адрес", "Адрес марки не определен")

class TestStaff(unittest.TestCase):
    def setUp(self):
        self.a = Staff("Фамилиия","Имя","Отчество","опыт работы","зарплата")
        PersistenceData.serialize(self.a, 'Staff')
        print(PersistenceData.deserialize('Staff'))

    def test_base(self):
        self.assertEqual(self.a.F, "Фамилиия", "Фамилиия сотрудника не определен")
        self.assertEqual(self.a.I, "Имя", "Имя сотрудника не определен")
        self.assertEqual(self.a.O, "Отчество", "Отчество сотрудника не определен")
        self.assertEqual(self.a.exp, "опыт работы", "Опыт сотрудника не определен")
        self.assertEqual(self.a.salary, "зарплата", "Зарплата сотрудника не определена")

class TestBuyer(unittest.TestCase):
    def setUp(self):
        self.a = Buyer("Фамилиия","Имя","Отчество","паспорт","адрес","город","возраст","пол")
        PersistenceData.serialize(self.a, 'Buyer')
        print(PersistenceData.deserialize('Buyer'))

    def test_base(self):
        self.assertEqual(self.a.F, "Фамилиия", "Фамилиия покупателя не определен")
        self.assertEqual(self.a.I, "Имя", "Имя покупателя не определен")
        self.assertEqual(self.a.O, "Отчество", "Отчество покупателя не определен")
        self.assertEqual(self.a.passport, "паспорт", "Паспорт покупателя не определен")
        self.assertEqual(self.a.address, "адрес", "Адрес покупателя не определен")
        self.assertEqual(self.a.city, "город", "Город покупателя не определен")
        self.assertEqual(self.a.age, "возраст", "Возраст покупателя не определен")
        self.assertEqual(self.a.pol, "пол", "Пол покупателя не определен")

class TestSale(unittest.TestCase):
    def setUp(self):
        self.a = Sale("дата","сотрудник","машина","покупатель")
        PersistenceData.serialize(self.a, 'Sale')
        print(PersistenceData.deserialize('Sale'))

    def test_base(self):
        self.assertEqual(self.a.date, "дата", "Дата цены не определена")
        self.assertEqual(self.a.staff, "сотрудник", "Сотрудник цены не определен")
        self.assertEqual(self.a.car, "машина", "Машина цены не определена")
        self.assertEqual(self.a.buyer, "покупатель", "Покупатель цены не определен")

if __name__ == "__main__":
    unittest.main()