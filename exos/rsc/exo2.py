a = input("Entrez le premier nombre : ")
b = input("Entrez le deuxième nombre : ")
try:
        a_num = int(a)
except(Exception):
    print("Première valeur incorrecte");
    exit()

try:
        b_num = int(b)
except(Exception):
    print("Deuxième valeur incorrecte");
    exit()

print (a + " + " + b + " = " + str(a_num + b_num))
