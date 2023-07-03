from datetime import date

class User:

    def __init__(self, name:str, birth: int):
        self.name = name
        self.birth = birth 
    
    def get_age(self):
        current_year = date.today().year
        return current_year - self.birth
    
    def is_adult(self):
        return self.get_age() >= 18