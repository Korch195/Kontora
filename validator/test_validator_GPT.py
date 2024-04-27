import unittest
from improved_validator_by_chatGPT import Validator

class TestValidator(unittest.TestCase):
    def test_validate_name_surname(self):
        valid = Validator()
        self.assertTrue(valid.validate_name_surname("Elvis Presley"))
        self.assertFalse(valid.validate_name_surname("ElvisPresley"))
        self.assertFalse(valid.validate_name_surname("Elvis Presley forever"))
        self.assertFalse(valid.validate_name_surname("elvis Presley"))
        self.assertFalse(valid.validate_name_surname("Elvis presley"))
        self.assertFalse(valid.validate_name_surname("Elvis PResley"))
        self.assertFalse(valid.validate_name_surname("Elvis Presleyqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"))
        self.assertFalse(valid.validate_name_surname("Elvis P"))
        self.assertFalse(valid.validate_name_surname("Elvis P,resley"))
        self.assertFalse(valid.validate_name_surname("El1vis Presley"))
        # Додані крайові випадки
        # Порожнє ім'я
        self.assertFalse(valid.validate_name_surname(""))
        # Ім'я з пробілом
        self.assertFalse(valid.validate_name_surname(" "))
        # Ім'я довжиною більше 30 символів
        self.assertFalse(valid.validate_name_surname("A" * 31))
        # Ім'я без прізвища
        self.assertFalse(valid.validate_name_surname("Elvis"))
        # Ім'я з цифрами
        self.assertFalse(valid.validate_name_surname("1234"))

    def test_validate_age(self):
        valid = Validator()
        self.assertTrue(valid.validate_age("20"))
        self.assertFalse(valid.validate_age("7"))
        self.assertFalse(valid.validate_age("100"))
        self.assertFalse(valid.validate_age("20."))
        self.assertFalse(valid.validate_age("20a"))
        # Додані крайові випадки
        # Вік менше 0
        self.assertFalse(valid.validate_age("-1"))
        # Вік більше 99
        self.assertFalse(valid.validate_age("100"))
        # Вік у дробовому форматі
        self.assertFalse(valid.validate_age("20.5"))
        # Вік у текстовому форматі
        self.assertFalse(valid.validate_age("twenty"))

    def test_validate_country(self):
        valid = Validator()
        self.assertTrue(valid.validate_country("Ukraine"))
        self.assertFalse(valid.validate_country("U"))
        self.assertFalse(valid.validate_country("UUUUUUUUUUUUUUUUUUUUUUU"))
        self.assertFalse(valid.validate_country("Ukraine1"))
        self.assertFalse(valid.validate_country("ukraine"))
        self.assertTrue(valid.validate_country("USA"))
        # Додані крайові випадки
        # Порожня назва країни
        self.assertFalse(valid.validate_country(""))
        # Назва країни з пробілом
        self.assertFalse(valid.validate_country(" "))
        # Коротка назва країни
        self.assertFalse(valid.validate_country("A"))
        # Назва країни довше 10 символів
        self.assertFalse(valid.validate_country("A" * 11))

    def test_validate_region(self):
        valid = Validator()
        self.assertTrue(valid.validate_region("Lviv"))
        self.assertTrue(valid.validate_region("Lviv1"))
        self.assertFalse(valid.validate_region("L"))
        self.assertFalse(valid.validate_region("lviv"))
        # Додані крайові випадки
        # Порожня назва регіону
        self.assertFalse(valid.validate_region(""))
        # Назва регіону з пробілом
        self.assertFalse(valid.validate_region(" "))
        # Коротка назва регіону
        self.assertFalse(valid.validate_region("A"))
        # Назва регіону довше 10 символів
        self.assertFalse(valid.validate_region("A" * 11))

    def test_validate_living_place(self):
        valid = Validator()
        self.assertTrue(valid.validate_living_place("Koselnytska st. 2a"))
        self.assertFalse(valid.validate_living_place("koselnytska st. 2a"))
        self.assertFalse(valid.validate_living_place("Koselnytska provulok 2a"))
        self.assertFalse(valid.validate_living_place("Koselnytska st. 2"))
        self.assertFalse(valid.validate_living_place("Koselnytska st. a2"))
        self.assertTrue(valid.validate_living_place("Koselnytska st. 22"))
        # Додані крайові випадки
        # Порожня назва місця проживання
        self.assertFalse(valid.validate_living_place(""))
        # Назва місця проживання з пробілом
        self.assertFalse(valid.validate_living_place(" "))
        # Коротка назва місця проживання
        self.assertFalse(valid.validate_living_place("A"))
        # Назва місця проживання довше 30 символів
        self.assertFalse(valid.validate_living_place("A" * 31))

    def test_validate_index(self):
        valid = Validator()
        self.assertTrue(valid.validate_index("79000"))
        self.assertFalse(valid.validate_index("7900"))
        self.assertFalse(valid.validate_index("790000"))
        self.assertFalse(valid.validate_index("7900q"))
        self.assertFalse(valid.validate_index("790 00"))
        # Додані крайові випадки
        # Порожній індекс
        self.assertFalse(valid.validate_index(""))
        # Індекс з пробілом
        self.assertFalse(valid.validate_index(" "))
        # Короткий індекс
        self.assertFalse(valid.validate_index("1234"))
        # Довгий індекс
        self.assertFalse(valid.validate_index("123456"))

    def test_validate_phone(self):
        valid = Validator()
        self.assertTrue(valid.validate_phone("+380951234567"))
        self.assertTrue(valid.validate_phone("+38 (095) 123-45-67"))
        self.assertFalse(valid.validate_phone("38 (095) 123-45-67"))
        self.assertFalse(valid.validate_phone("380951234567"))
        self.assertFalse(valid.validate_phone("-380951234567"))
        self.assertFalse(valid.validate_phone("+3810951234567"))
        self.assertTrue(valid.validate_phone("+20951234567"))
        # Додані крайові випадки
        # Порожній номер
        self.assertFalse(valid.validate_phone(""))
        # Номер без "+"
        self.assertFalse(valid.validate_phone("380951234567"))
        # Номер з більше ніж 12 цифрами
        self.assertFalse(valid.validate_phone("+3809512345678"))
        # Номер з менше ніж 9 цифрами
        self.assertFalse(valid.validate_phone("+38095123"))
        # Номер з неправильним кодом країни (не "38")
        self.assertFalse(valid.validate_phone("+4810951234567"))
        # Номер з додатковими цифрами в кінці
        self.assertFalse(valid.validate_phone("+38 (095) 123-45-678"))

    def test_validate_email(self):
        valid = Validator()
        self.assertTrue(valid.validate_email("username@domain.com"))
        self.assertTrue(valid.validate_email("username+usersurname@domain.com"))
        self.assertTrue(valid.validate_email("username@ucu.edu.ua"))
        self.assertFalse(valid.validate_email("usernamedomain.com"))
        self.assertFalse(valid.validate_email("username@domaincom"))
        self.assertFalse(valid.validate_email("username@domain.aaa"))
        self.assertFalse(valid.validate_email("username@aaa"))
        self.assertFalse(valid.validate_email("@domain.com"))
        # Додані крайові випадки
        # Порожній email
        self.assertFalse(valid.validate_email(""))
        # Email без "@"
        self.assertFalse(valid.validate_email("usernamedomain.com"))
        # Email без домену
        self.assertFalse(valid.validate_email("username@"))
        # Email з пробілом
        self.assertFalse(valid.validate_email("username @domain.com"))
        # Email з неправильним доменом
        self.assertFalse(valid.validate_email("username@domain."))
        # Email з неправильним форматом імені
        self.assertFalse(valid.validate_email(".username@domain.com"))

    def test_validate_id(self):
        valid = Validator()
        self.assertTrue(valid.validate_id("123450"))
        self.assertTrue(valid.validate_id("011111"))
        self.assertFalse(valid.validate_id("123456"))
        self.assertFalse(valid.validate_id("123006"))
        self.assertFalse(valid.validate_id("1230916"))
        self.assertFalse(valid.validate_id("12306"))
        # Додані крайові випадки
        # Порожній ID
        self.assertFalse(valid.validate_id(""))
        # ID без нуля
        self.assertFalse(valid.validate_id("123456"))
        # ID з двома нулями
        self.assertTrue(valid.validate_id("120456"))
        # ID з більше ніж 6 цифрами
        self.assertFalse(valid.validate_id("1234567"))
        # ID з менше ніж 6 цифрами
        self.assertFalse(valid.validate_id("12345"))


    def test_validate(self):
        valid = Validator()
        data = "Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450"
        self.assertTrue(valid.validate(data))
        # Додані крайові випадки
        # Порожні дані
        self.assertFalse(valid.validate(""))
        # Дані без пробілів
        self.assertFalse(valid.validate("ElvisPresley,20,Ukraine,Lviv,Koselnytskast2a,79000,+380951234567,username@domain.com,123450"))
        # Дані з неправильним номером телефону
        self.assertFalse(valid.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+38 (095) 123-45-678,username@domain.com,123450"))

if __name__ == '__main__':
    unittest.main()
