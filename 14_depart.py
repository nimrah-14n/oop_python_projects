class Employ:

    def __init__(self,name):
        self.name = name

class Department:

    def __init__(self, employ):
        self.employ = employ

emp = Employ("Nimrah")

dept = Department(emp)
print(dept.employ.name)