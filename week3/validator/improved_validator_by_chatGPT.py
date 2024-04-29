"""validator"""
import re
class Validator:
    """classes for validator"""
    def validate_name_surname(self, name_surname: str):
        """checks name and surname"""
        name = r"^[A-Z][a-z]{1,30}+\s[A-Z][a-z]{1,30}$"
        return bool(re.match(name, name_surname))

    def validate_age(self, age: str):
        """checks age"""
        re_age = r"^(1[6-9]|[2-9][0-9])$"
        return bool(re.match(re_age, age))

    def validate_country(self, country: str):
        """checks country"""
        re_country = r"^[A-Z][a-zA-Z]{1,9}$"
        return bool(re.match(re_country, country))

    def validate_region(self, region: str):
        """checks region"""
        re_region = r"^[A-Z][a-z0-9]{1,9}$"
        return bool(re.match(re_region, region))

    def validate_living_place(self, living_place: str):
        """checks street"""
        re_living = r"^[A-Z][a-z]{3,20}\s(?:st\.|av\.|prosp\.|rd\.)\s(?:\d{2}|(?:\d[a-z]))$"
        return bool(re.match(re_living, living_place))

    def validate_index(self, index: str):
        """checks index"""
        re_index = r"^\d{5}$"
        return bool(re.match(re_index, index))

    def validate_phone(self, phone: str):
        """checks phone number"""
        re_phone = r"^\+(?:\d{9,12})$|^\+[3][8]\s\(\d{3}\)\s\d{3}\-\d{2}\-\d{2}$"
        return bool(re.match(re_phone,phone))

    def validate_email(self, email: str):
        """checks email"""
        re_email = r"^(?!.*\.\.)[A-Za-z0-9!#$%&'*+/=?^_`{|}~-][A-Za-z0-9!#$%&'*+/=?^_`{|}~.-]{0,62}[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]@[a-z\d.-]+\.(?:com|org|edu|gov|net|ua)$"
        return bool(re.match(re_email, email))

    def validate_id(self, id: str):
        """checks id"""
        re_id = r"^(?=.*0)(?!.*0.*0)\d{6}$"
        return bool(re.match(re_id,id))

    def validate(self, data: str):
        """validate entire data string"""
        separators = r'[;]|, |; |[,]'
        components = re.split(separators, data.strip())
        if len(components) != 9:
            return False
        name_surname, age, country, region, living_place, index, phone, email, \
            id = map(str.strip, components)
        return all([
            self.validate_name_surname(name_surname),
            self.validate_age(age),
            self.validate_country(country),
            self.validate_region(region),
            self.validate_living_place(living_place),
            self.validate_index(index),
            self.validate_phone(phone),
            self.validate_email(email),
            self.validate_id(id)])
