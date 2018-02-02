def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

val_str = input("Entrez un nombre : ")
try:
    val = int(val_str)
except:
    print("Ceci n'est pas un nombre...")
    exit()

if is_prime(val):
    print(val, "est premier")
else:
    print(val, "n'est pas premier")
    
