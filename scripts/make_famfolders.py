import os
from os import listdir

# Must be executed from "scripts" folder in termianl
os.chdir('..')
currDir=os.getcwd()

for file in listdir(currDir):
    if file[-7:]=="ref.vie":
        famName=file.split('_ref.')[0]
        os.system("mkdir fam_"+famName)
        os.system("mv "+famName+"_ref.vie fam_"+famName+"/")
        os.system("mv "+famName+"_test-only.vie fam_"+famName+"/")
