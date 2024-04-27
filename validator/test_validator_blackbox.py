import unittest
from original_code import Validator

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_validate_name_surname(self):
        self.assertTrue(self.validator.validate_name_surname("Elvis Presley"))
        self.assertFalse(self.validator.validate_name_surname("ElvisPresley"))
        self.assertFalse(self.validator.validate_name_surname("Elvis Presley forever"))
        self.assertFalse(self.validator.validate_name_surname("elvis Presley"))
        self.assertFalse(self.validator.validate_name_surname("Elvis presley"))
        self.assertFalse(self.validator.validate_name_surname("Elvis PResley"))
        self.assertFalse(self.validator.validate_name_surname("Elvis Presleyqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"))
        self.assertFalse(self.validator.validate_name_surname("Elvis P"))
        self.assertFalse(self.validator.validate_name_surname("Elvis P,resley"))
        self.assertFalse(self.validator.validate_name_surname("El1vis Presley"))

    def test_validate_age(self):
        self.assertTrue(self.validator.validate_age("20"))
        self.assertFalse(self.validator.validate_age("7"))
        self.assertFalse(self.validator.validate_age("100"))
        self.assertFalse(self.validator.validate_age("20."))
        self.assertFalse(self.validator.validate_age("20a"))
        self.assertFalse(self.validator.validate_age(""))
        self.assertFalse(self.validator.validate_age("20 20"))

    def test_validate_country(self):
        self.assertTrue(self.validator.validate_country("Ukraine"))
        self.assertFalse(self.validator.validate_country("U"))
        self.assertFalse(self.validator.validate_country("UUUUUUUUUUUUUUUUUUUUUUU"))
        self.assertFalse(self.validator.validate_country("Ukraine1"))
        self.assertFalse(self.validator.validate_country("ukraine"))
        self.assertTrue(self.validator.validate_country("USA"))
        self.assertFalse(self.validator.validate_country(""))
        self.assertFalse(self.validator.validate_country("1Ukraine"))
        self.assertFalse(self.validator.validate_country("Ukraine1234567890123456789012345678901234567890"))

    def test_validate_region(self):
        self.assertTrue(self.validator.validate_region("Lviv"))
        self.assertTrue(self.validator.validate_region("Lviv1"))
        self.assertFalse(self.validator.validate_region("L"))
        self.assertFalse(self.validator.validate_region("lviv"))
        self.assertFalse(self.validator.validate_region(""))
        self.assertFalse(self.validator.validate_region("1Lviv"))
        self.assertFalse(self.validator.validate_region("Lviv1234567890123456789012345678901234567890"))

    def test_validate_living_place(self):
        self.assertTrue(self.validator.validate_living_place("Koselnytska st. 2a"))
        self.assertFalse(self.validator.validate_living_place("koselnytska st. 2a"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska provulok 2a"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. 2"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. a2"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. 22"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. 22a"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. 22A"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. 22a "))
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. 22 a"))
        self.assertFalse(self.validator.validate_living_place("Koselnytska st. 22a "))
    
        
    def test_validate_index(self):
        self.assertTrue(self.validator.validate_index("79000"))
        self.assertFalse(self.validator.validate_index("7900"))
        self.assertFalse(self.validator.validate_index("790000"))
        self.assertFalse(self.validator.validate_index("7900q"))
        self.assertFalse(self.validator.validate_index("79 00"))
        self.assertFalse(self.validator.validate_index(""))
        self.assertFalse(self.validator.validate_index("7900 00"))

    def test_validate_phone(self):
        self.assertTrue(self.validator.validate_phone("+380951234567"))
        self.assertTrue(self.validator.validate_phone("+38 (095) 123-45-67"))
        self.assertFalse(self.validator.validate_phone("38 (095) 123-45-67"))
        self.assertFalse(self.validator.validate_phone("380951234567"))
        self.assertFalse(self.validator.validate_phone("-380951234567"))
        self.assertFalse(self.validator.validate_phone("+3810951234567"))
        self.assertFalse(self.validator.validate_phone("+20951234567"))
        self.assertFalse(self.validator.validate_phone("+3809 51234567"))
        self.assertFalse(self.validator.validate_phone("+38095 1234567"))
        self.assertFalse(self.validator.validate_phone("+380951 234567"))
        self.assertFalse(self.validator.validate_phone("+3809512 34567"))
        self.assertFalse(self.validator.validate_phone("+38095123 4567"))
        self.assertFalse(self.validator.validate_phone("+380951234 567"))
        self.assertFalse(self.validator.validate_phone("+3809512345 67"))
        self.assertFalse(self.validator.validate_phone("+38095123456"))
        self.assertFalse(self.validator.validate_phone("+380951234567a"))
        self.assertFalse(self.validator.validate_phone("+380951234567 "))
        self.assertFalse(self.validator.validate_phone(""))

    def test_validate_email(self):
        self.assertTrue(self.validator.validate_email("username@domain.com"))
        self.assertTrue(self.validator.validate_email("username+usersurname@domain.com"))
        self.assertTrue(self.validator.validate_email("username@ucu.edu.ua"))
        self.assertFalse(self.validator.validate_email("usernamedomain.com"))
        self.assertFalse(self.validator.validate_email("username@domaincom"))
        self.assertFalse(self.validator.validate_email("username@domain.aaa"))
        self.assertFalse(self.validator.validate_email("username@aaa"))
        self.assertFalse(self.validator.validate_email("@domain.com"))
        self.assertFalse(self.validator.validate_email("username.domain.com"))
        self.assertFalse(self.validator.validate_email("username@domain.c"))
        self.assertFalse(self.validator.validate_email("username@.com"))
        self.assertFalse(self.validator.validate_email("username@domain..com"))
        self.assertFalse(self.validator.validate_email("username@domain.com."))
        self.assertFalse(self.validator.validate_email("username..domain@domain.com"))
        self.assertFalse(self.validator.validate_email("username@domain.c"))
        self.assertFalse(self.validator.validate_email("username@domain.com (Joe Smith)"))
        self.assertFalse(self.validator.validate_email("username@domain.name"))
        self.assertFalse(self.validator.validate_email("username@domain"))
        self.assertFalse(self.validator.validate_email("username123@domain.com"))
        self.assertFalse(self.validator.validate_email("username.123@domain.com"))
        self.assertFalse(self.validator.validate_email("username-123@domain.com"))
        self.assertFalse(self.validator.validate_email("username@domain.123"))
        self.assertFalse(self.validator.validate_email("username@123.domain.com"))
        self.assertFalse(self.validator.validate_email("username@domain-123.com"))
        self.assertFalse(self.validator.validate_email("username@domain.com_123"))
        self.assertFalse(self.validator.validate_email("username@domain.name.123"))
        self.assertFalse(self.validator.validate_email("username@domain.name.123.456"))
        self.assertFalse(self.validator.validate_email("username@domain.name.123.456.789"))

    def test_validate_id(self):
        self.assertTrue(self.validator.validate_id("123450"))
        self.assertTrue(self.validator.validate_id("011111"))
        self.assertFalse(self.validator.validate_id("123456"))
        self.assertFalse(self.validator.validate_id("123006"))
        self.assertFalse(self.validator.validate_id("1230916"))
        self.assertFalse(self.validator.validate_id("12306"))

    def test_validate_data(self):
        self.assertTrue(self.validator.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450"))
        self.assertTrue(self.validator.validate("Elvis Presley;20;Ukraine;Lviv;Koselnytska st. 2a;79000;+380951234567;username@domain.com;123450"))
        self.assertTrue(self.validator.validate("Elvis Presley; 20; Ukraine; Lviv; Koselnytska st. 2a; 79000; +380951234567; username@domain.com; 123450"))
        self.assertTrue(self.validator.validate("Elvis Presley, 20, Ukraine, Lviv, Koselnytska st. 2a, 79000, +380951234567, username@domain.com, 123450"))
        self.assertFalse(self.validator.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123456"))
        self.assertFalse(self.validator.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123006"))
        self.assertFalse(self.validator.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,1230916"))
        self.assertFalse(self.validator.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,12306"))

if __name__ == '__main__':
    unittest.main()