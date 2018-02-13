from utils import *
import sys
sys.path.append("../../exos/LG/")


tab = toArray("../../exos/rsc/data/csv/installations.csv",',')
numColumn = countColumn(tab)

tab = removeSymbol(tab,'"',numColumn)

tmp = []
for i in range(0,numColumn-1):
    tmp.append(tab[i])

print(tmp)

parseToJsonArray("installations_column_name.json", tmp)