class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"Name: {self.name} Marks: {self.marks}")

s1 = Student("Nimrah", 96)
 
s1.display()