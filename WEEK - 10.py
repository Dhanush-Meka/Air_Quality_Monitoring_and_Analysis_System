def check_value(value):
    if value < 0:
        return False
    return True
import validators

value = float(input("Enter PM2.5: "))

if validators.check_value(value):
    print("Valid Value")
else:
    print("Invalid Value")