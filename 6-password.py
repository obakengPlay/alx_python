def validate_password(password) :
    if len(password) < 8:
      return False

has_upper = any(char.isupper()
                 for char in password)
has_lower = any(char.islower()
                 for char in password)
has_digit = any(char.isdigit()
                 for char in password)
has_space = ' ' in password
  
return has_upper and has_lower and has_digit
 
 
print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))
 