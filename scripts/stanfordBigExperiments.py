from os import listdir, system, chdir

PROJECTPATH="../atpg/"
SEARCHPATH="../atpg/work/stanford/"

chdir(PROJECTPATH)

checkCombos = []
for f in listdir("/home/ioanna/SDN_Project/atpg/work"):
    if "combo" in f:
        fl = open("/home/ioanna/SDN_Project/atpg/work/" + f, "r")
        lines = fl.readlines()
        fl.close()
        if "Total" in lines[len(lines)-1]:
            checkCombos.append(f.replace("s2-10_", "").replace(".txt", ""))


for percentage in ["10", "40", "70", "100"]:
    count = 0
    for f in checkCombos:
        if "combo" in f:

            system("./atpg_stanford.py -p " + percentage +" -f s2-"+ percentage +"_"+f+".sqlite --folder ~/SDN_Project/atpg/work/stanford/" + f + "/ > ./work/big/s2-"+percentage+"_" + f + ".txt")


            fl = open("./work/big/s2-" + percentage + "_" +  f + ".txt", "r")
            lines = fl.readlines()
            fl.close()
            if "Total" in lines[len(lines)-1]:
                print "Success in " + f + " with percentage " + percentage
                count += 1

            if count>10:
                break

            
        
