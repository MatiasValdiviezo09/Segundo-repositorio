import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

#introduce la longitud de la contraseña
length = int(input("Introduce la longitud de la contraseña: "))

#contraseña generada
password = ""

# generador de la contraseña
for _ in range(length):
    password += random.choice(characters)

#imprimiendo la contraseña
print("Tu contraseña generada es:", password)
