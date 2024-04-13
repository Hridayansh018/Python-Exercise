class adException(Exception):
    pass

class person:
    def __init__(self,name, age):
        self.name = name 
        self.age = age 

    def get_age(self):
        if int(self.age) >= 18:
            raise adException
        else:
            return self.age
        
    def display(self):
        try:
            print(f"age -> {self.get_age()}")
        except adException :
            print("The Person is an adult")
        finally:
            print(f"name -> {self.name}")

aman = person("Amandeep", 17)
shiva = person("Shiva Varma", 19).display()


