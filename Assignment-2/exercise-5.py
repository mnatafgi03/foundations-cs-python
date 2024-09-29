def check_password(passw):
    upper = lower = digit = special = False
    special_chars = "#?!$"

    for char in passw:
        if 'A' <= char <= 'Z':
            upper = True
        elif 'a' <= char <= 'z':
            lower = True
        elif '0' <= char <= '9':
            digit = True
        elif char in special_chars:
            special = True

    if len(passw) >= 8 and upper and lower and digit and special:
        return "Strong password"
    else:
        return "Weak password"

password = input("Please enter a password: ")
print(check_password(password))
