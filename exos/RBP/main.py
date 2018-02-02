def toArray(filePath, symbol=""):
    array = []
    f = open(filePath, "r")
    if symbol=="":
        while f.readable():
            line = f.readline()
            for obj in line:
                array.append(obj)
    else:
        while f.readable():
            line = f.readline()
            tmp = line.split(symbol)
            array.extend(tmp)
    return array

def formatInt(array):
    for i in range(0,len(array)):
        array[i] = int(array[i])
    return array

def toString(array,symbol=""):
    tmp = ""
    if symbol =="":
        for obj in array:
            tmp += str(obj)
    else:
        for obj in array:
            tmp += str(obj)
            tmp += " "
    print(tmp)

tab = toArray("../rsc/test_val"," ")
tab = formatInt(tab)
toString(tab," ")
print(sum(tab))
