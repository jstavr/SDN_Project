from os import listdir, system, chdir

PROJECTPATH="../atpg/"
SEARCHPATH="../atpg/work/"


count = 0
for f in listdir(SEARCHPATH):
    if "i2-10" in f:
        fl = open(SEARCHPATH + f, "r")
        lines = fl.readlines()
        fl.close()
        if "Total" in lines[len(lines)-1]:
            count += 1
print count

