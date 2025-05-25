class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    
    def display(self):
        print("Name: ", self.name)
        print("Roll: ", self.roll)


s = Student("Rupin", 50)
s.display()