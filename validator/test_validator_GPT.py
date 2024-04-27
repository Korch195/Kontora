import unittest
from improved_validator_by_chatGPT import Validator


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.valid = Validator()

    def test_validate_name_surname(self):
        valid_names = ["Elvis Presley"]
        invalid_names = ["ElvisPresley", "Elvis Presley forever", "elvis Presley", "Elvis presley", "Elvis PResley", "Elvis Presleyqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq", "Elvis P", "Elvis P,resley", "El1vis Presley", "", " ", "A" * 31, "Elvis"]
        for name in valid_names:
            self.assertTrue(self.valid.validate_name_surname(name))
        for name in invalid_names:
            self.assertFalse(self.valid.validate_name_surname(name))

    def test_validate_age(self):
        valid_ages = ["20"]
        invalid_ages = ["7", "100", "20.", "20a", "-1", "100", "20.5", "twenty"]
        for age in valid_ages:
            self.assertTrue(self.valid.validate_age(age))
        for age in invalid_ages:
            self.assertFalse(self.valid.validate_age(age))

    def test_validate_country(self):
        valid_countries = ["Ukraine", "USA"]
        invalid_countries = ["U", "UUUUUUUUUUUUUUUUUUUUUUU", "Ukraine1", "ukraine", "", " ", "A" * 11]
        for country in valid_countries:
            self.assertTrue(self.valid.validate_country(country))
        for country in invalid_countries:
            self.assertFalse(self.valid.validate_country(country))

    def test_validate_region(self):
        valid_regions = ["Lviv", "Lviv1"]
        invalid_regions = ["L", "lviv", "", " ", "A" * 11]
        for region in valid_regions:
            self.assertTrue(self.valid.validate_region(region))
        for region in invalid_regions:
            self.assertFalse(self.valid.validate_region(region))

    def test_validate_living_place(self):
        valid_places = ["Koselnytska st. 2a", "Koselnytska st. 22"]
        invalid_places = ["koselnytska st. 2a", "Koselnytska provulok 2a", "Koselnytska st. 2", "Koselnytska st. a2", "", " ", "A" * 31]
        for place in valid_places:
            self.assertTrue(self.valid.validate_living_place(place))
        for place in invalid_places:
            self.assertFalse(self.valid.validate_living_place(place))

    def test_validate_index(self):
        valid_indices = ["79000"]
        invalid_indices = ["7900", "790000", "7900q", "790 00", "", " ", "1234", "123456"]
        for index in valid_indices:
            self.assertTrue(self.valid.validate_index(index))
        for index in invalid_indices:
            self.assertFalse(self.valid.validate_index(index))

    def test_validate_phone(self):
        valid_phones = ["+380951234567", "+38 (095) 123-45-67", "+20951234567"]
        invalid_phones = ["38 (095) 123-45-67", "380951234567", "-380951234567", "+3810951234567", "", " ", "38095123", "+3809512345678", "+4810951234567", "+38 (095) 123-45-678"]
        for phone in valid_phones:
            self.assertTrue(self.valid.validate_phone(phone))
        for phone in invalid_phones:
            self.assertFalse(self.valid.validate_phone(phone))

    def test_validate_email(self):
        valid_emails = ["username@domain.com", "username+usersurname@domain.com", "username@ucu.edu.ua"]
        invalid_emails = ["usernamedomain.com", "username@domaincom", "username@domain.aaa", "username@aaa", "@domain.com", "", " ", "username @domain.com", "username@domain."]
        for email in valid_emails:
            self.assertTrue(self.valid.validate_email(email))
        for email in invalid_emails:
            self.assertFalse(self.valid.validate_email(email))

    def test_validate_id(self):
        valid_ids = ["123450", "011111", "120456"]
        invalid_ids = ["123456", "123006", "1230916", "12306", "", " ", "1234567", "12345"]
        for id in valid_ids:
            self.assertTrue(self.valid.validate_id(id))
        for id in invalid_ids:
            self.assertFalse(self.valid.validate_id(id))

    def test_validate(self):
        data = "Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450"
        self.assertTrue(self.valid.validate(data))
        self.assertFalse(self.valid.validate(""))
        self.assertFalse(self.valid.validate("ElvisPresley,20,Ukraine,Lviv,Koselnytskast2a,79000,+380951234567,username@domain.com,123450"))
        self.assertFalse(self.valid.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+38 (095) 123-45-678,username@domain.com,123450"))

if __name__ == '__main__':
    unittest.main()
