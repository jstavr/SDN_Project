from os import listdir, system, chdir

PROJECTPATH="../atpg/"
SEARCHPATH="../atpg/work/Internet2/"

chdir(PROJECTPATH)
for f in listdir(SEARCHPATH):
    if "combo" in f:

        system("./atpg_internet2.py -p 10 -f i2-10.sqlite --folder ~/SDN_Project2/SDN_Project/atpg/work/Internet2/" + f + "/ > ./work/i2-10_" + f + ".txt")
        
