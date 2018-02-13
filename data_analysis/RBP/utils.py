import json

def toArray(filePath, delimeter=""):

    array = []
    f = open(filePath, "r", encoding="utf-8")
    if delimeter=="":
        for line in f:
            for obj in line:
                array.append(obj)
    else:
        fline = 0
        for line in f:

            if fline == 0:
                array.append("<start>")
                print("start")

            obj = line.split(delimeter)
            array.extend(obj)

            if fline == 0:
                array.append("<end>")
                fline = 1

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

def findLinkedValue(array, value, numColumn):
    map = dict()
    innerArray = []
    index = array.index(value)
    for i in range(index, len(array), numColumn):
        innerArray.append(array[i])
    map[value] = innerArray
    return map


def countColumn(array):
    for i in range(0, len(array)):
        if (array[i]=="<start>"):
            array.pop(i)
        if(array[i]=="<end>"):
            array.pop(i)
            return i

def removeSymbol(array, symbol, numColumn):
    tmp = ""
    for i in range(0, numColumn):
        for car in array[i]:
            if car != symbol:
                tmp += car
        print(tmp)
        array[i] = tmp
        tmp = ""
    return array

def parseToJsonArray(path, array):
    with open(path, "w") as file:
        json.dump(array, file, ensure_ascii=False)
        file.close()