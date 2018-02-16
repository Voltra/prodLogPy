import json
import csv

def readCSV(filepath, delimiter, quotechar):
    with open(filepath, "r") as csvfile:
        array = csv.DictReader(csvfile)
    for row in array:
        print(', '.join(row))
    return array

def toArray(filePath, delimiter="", quotechar=""):

    array = []
    f = open(filePath, "r", encoding="utf-8")
    if delimiter=="":
        for line in f:
            for obj in line:
                array.append(obj)
    else:
        quote = 0
        tmp = ""
        for line in f:

            for i in range(0, len(line)):

                if (line[i] == quotechar):
                    quote += 1
                    continue

                if (line[i] == delimiter and i+1 == len(line)-1):
                    array.append("NULL")
                    tmp = ""
                    continue

                if (line[i] == delimiter and tmp == ""):
                    array.append("NULL")
                    tmp = ""
                    continue

                if (line[i] == delimiter and quote == 0 or quote == 2):
                    tmp = tmp.replace("\n","n")
                    array.append(tmp)
                    quote = 0
                    tmp = ""
                    continue

                tmp += line[i]

    f.close()
    return array

"""Méthode permettant de convertir toute les string d'un tableau en int (à condition que les sting soit des chiffre"""
def formatInt(array):
    for i in range(0,len(array)):
        array[i] = int(array[i])
    return array

def toString(array, delimiter=""):
    tmp = ""
    if delimiter =="":
        for obj in array:
            tmp += str(obj)
    else:
        for obj in array:
            tmp += str(obj)
            tmp += delimiter
    print(tmp)

def findLinkedValue(array, value, numColumn):
    map = dict()
    innerArray = []
    index = array.index(value)
    for i in range(index, len(array), numColumn-1):
        innerArray.append(array[i])
    map[value] = innerArray
    return map

"""Récupèrer la première ligne"""
def countColumn(filePath, delimiter="", quotechar=""):
    quote = 0
    array = []
    tmp = ""
    with open(filePath, "r") as file:
        line = file.readline()
        for i in range(0, len(line)):

            if (line[i] == quotechar):
                quote += 1
                continue

            if (line[i] == delimiter and quote == 0 or quote == 2 and i < len(line)):
                quote = 0
                array.append(tmp)
                tmp = ""
                continue

            tmp += line[i]
    file.close()
    return array



def removeSymbol(array, delimiter, numColumn):
    tmp = ""
    for i in range(0, numColumn):
        for car in array[i]:
            if car != delimiter:
                tmp += car
        array[i] = tmp
        tmp = ""
    return array

def parseToJsonArray(path, array):
    with open(path, "w") as file:
        json.dump(array, file, ensure_ascii=False)
        file.close()