from main import *
import unittest

class TestCar(unittest.TestCase):
    def setUp(self):
        self.a = Car("Spyker","2007","black","sport",640000,Stamp("Spyker Cars","страна","завод","адрес","1"))
        PersistenceData.serialize(self.a, 'Car')
        print(PersistenceData.deserialize('Car'))

    def test_base(self):
        self.assertEqual(self.a.__call__(1000),1000,'Не соответствует')

class TestStaff(unittest.TestCase):
    def setUp(self):
        self.a = Staff("Фамилиия","Имя","Отчество","опыт работы",5000)
        PersistenceData.serialize(self.a, 'Car')
        print(PersistenceData.deserialize('Car'))

    def test_base(self):
        self.assertEqual(self.a.__add__(1000),6000,'Не соответствует')


if __name__ == "__main__":
    unittest.main()