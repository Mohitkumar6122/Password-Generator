import string
import secrets

def secure_password_gen(passlength):
    password = ''.join((secrets.choice(string.ascii_letters) for i in range(passlength)))
    return password

n = int(input('Enter length of password : '))
print('Password generated is :', secure_password_gen(n))
