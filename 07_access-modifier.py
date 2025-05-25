class Employ:
    def __init__(self, name, salary, ssn):
        self.name = name          # public
        self._salary = salary     # protected
        self.__ssn = ssn          # private

    def get_ssn(self):
        return self.__ssn

emp = Employ("Nimrah", 100000, "03020980302")

print(emp.name)
print(emp._salary)
print(emp.get_ssn())