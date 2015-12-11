from os import listdir, system, chdir

PROJECTPATH="../atpg/"
SEARCHPATH="../atpg/work/stanford/"

chdir(PROJECTPATH)
for f in listdir(SEARCHPATH):
    if "combo" in f:

        system("./atpg_stanford.py -p 10 -f s2-10.sqlite --folder ~/SDN_Project/atpg/work/stanford/" + f + "/ > ./work/s2-10_" + f + ".txt")
        
