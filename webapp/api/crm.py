import re
import string
from tinydb import TinyDB, where, table
from pathlib import Path
from typing import List

class User():
    
    DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)
    
    def __init__(self, first_name : str, last_name: str, phone_number: str="", addresse: str ="") :
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.addresse = addresse
    
    
    def __repr__(self):
        return f"User({self.first_name}, {self.last_name})"
    
    def __str__(self):
        return f"{self.full_name}\n{self.phone_number}\n{self.addresse}"

    @property
    def full_name(self) :
        return f"{self.first_name} {self.last_name}"
    
    @property
    def db_instance(self) :
        return User.DB.get((where('first_name') == self.first_name) & (where('last_name') == self.last_name))
    

    def _checks(self) :
        self._chech_phone_number()
        self._check_names()

    def _chech_phone_number(self) :
       phone_number = re.sub(r"[+()\s]*", "", self.phone_number)
       if len(phone_number) < 10 or not phone_number.isdigit() :
           raise ValueError(f"Numéro de téléphone {self.phone_number} invalide")


    def _check_names(self) :
        if not self.first_name and self.last_name :
            raise ValueError("Le nom et le prénom ne doivent pas être vides")

        specials_characters = string.digits + string.punctuation
        
        for characters in self.first_name + self.last_name :
            if characters in  specials_characters:
                raise ValueError(f"Nom invalide {self.full_name}")
    
    
    def exists(self):
        return bool(self.db_instance)
    
    
    def delete(self) -> List[int]:
        if self.exists() :
            return User.DB.remove(doc_ids=[self.db_instance.doc_id])    
        return []
    
    
    def save(self, validate_data: bool=False) -> int:
        if validate_data :
            self._checks()
        if self.exists() :
            return -1
        else :
            return User.DB.insert(self.__dict__)
    
def get_all_users() :
    return [User(**user) for user in User.DB.all()]

if __name__ == "__main__" :
    name = User("Agathe", "Buisson")
    print(name.exists())
    print(name.db_instance)
    # from faker import Faker
    # fake = Faker(locale = "fr_FR")
    # for _ in range(10) :
    #     user = User(first_name = fake.first_name(),
    #                 last_name = fake.last_name(),
    #                 phone_number = fake.phone_number(),
    #                 addresse= fake.address()
    #                 )
    #     print(user.save())
    #     print("-" * 10 )