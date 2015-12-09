from os import listdir, system, chdir


WORK_DIR = "/home/mininet/SDN_Project2/SDN_Project/atpg/work/"
for f in listdir(WORK_DIR):

    if ".sqlite" in f:
        print f
        system("../atpg/link_cover.py " + WORK_DIR + f )#+ " > " + WORK_DIR + f.replace(".sqllite", "_link.txt"))
        
