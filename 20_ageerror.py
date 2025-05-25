
class InvalidAgeError(Exception):
    pass  

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")  
    else:
        print("Age is valid. You can proceed.")


try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("InvalidAgeError:", e)