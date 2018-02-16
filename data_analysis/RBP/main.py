from utils import *
import sys
sys.path.append("../../exos/LG/")


tab = toArray("../../exos/rsc/data/csv/activites.csv",',','"')
# subTab = countColumn("../../exos/rsc/data/csv/activites.csv",',','"')

tmp = ""
for i in range(0, len(tab)):
    if i%10 == 0:
        print(str(i)+"::"+tmp)
        tmp = ""
    tmp += tab[i]+" "