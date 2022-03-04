#Napisz program, który wczyta długość promienia podaną przez użytkownika.
#Następnie obliczy i wypisze pole oraz obwód koła.
print("Podaj promień koła")
r = int(input())
pi = 3.14
pole = pi * (r**2)
obwod = 2 * pi * r
print("Pole koła wynosi:")
print(pole)
print("Obwód koła wynosi:")
print(round(obwod, 3))
