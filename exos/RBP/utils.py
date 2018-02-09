"""Méthode permettant de transformer un fichier en tableau, soit ligne par ligne, soit en séparant sur
    un symbole donné en entrée"""
def toArray(filePath, symbol=""):

    array = []
    f = open(filePath, "r")
    if symbol=="":
        for line in f.readlines():
            for obj in line:
                array.append(obj)
    else:
        for line in f.readlines():
            obj = line.split(symbol)
            array.extend(obj)
    f.close()
    return array

"""Méthode permettant de convertir toute les string d'un tableau en int (à condition que les sting soit des chiffre"""
def formatInt(array):
    for i in range(0,len(array)):
        array[i] = int(array[i])
    return array

def join(array, glue=", "):
    length = len(array)
    if length == 0:
        return ""
    elif length == 1:
        return str(array[0])
    else:
        ret = str(array[0])
        for i in range(1, length):
            ret += glue + str(array[i])

        return ret

def toString(array,symbol=""):
    tmp = ""
    if symbol =="":
        for obj in array:
            tmp += str(obj)
    else:
        for obj in array:
            tmp += str(obj)
            tmp += symbol
    print(tmp)

def findNumRows(array):
    it = 0
    for i in range(0, len(array)):
        for char in array[i]:
            if char =='"':
                it += 1
            if it > 1:
                return i