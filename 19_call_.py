class Multiplier:
    def _init_(self, factor):
        self.factor = factor  

    def _call_(self, number):
        return self.factor * number



m = Multiplier(5)


print(callable(m))  


result = m(10)    
print(result)      