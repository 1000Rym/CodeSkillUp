class Person:
    
    def __init__(self, given_name, family_name):
        self.__given_name = given_name
        self.__family_name = family_name

    @property 
    def full_name(self):
        """Change function as attribute"""
        return self.__given_name + " " + self.__family_name

    @property
    def age(self):
        """Implement private attribute age getter and setter"""
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f"The person's is {self.full_name}, {self.age} year's old"

if __name__ == '__main__':
    lin = Person("Benedict","Thousand")
    lin.age=32
    print(lin)