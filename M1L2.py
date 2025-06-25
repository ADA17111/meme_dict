import random
character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long_password=int(input("introduzca la longitud de la contraseña\n"))
int(long_password)
password=""
for i in range(long_password):
    password+=random.choice(character)
print("Tu nueva contraseña es:",password)
