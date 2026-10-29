password = input("Enter password: ")

if len(password) < 8:
    print("Password must have at least 8 characters")
elif not any(c.isupper() for c in password):
    print("Include an uppercase letter")
elif not any(c.islower() for c in password):
    print("Include a lowercase letter")
elif not any(c.isdigit() for c in password):
    print("Include a digit")
elif not any(not c.isalnum() for c in password):
    print("Include a special character")
else:
    print("Password is valid")