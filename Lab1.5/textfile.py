import glob
import os

lab_path = "C:\\Users\\pucher\\Documents\\Seafile\\p4ne_training\\config_files"

file_list2 = glob.iglob(lab_path + "\\*.txt")

for f in file_list2:
    with open(f) as file:
        print(file.readlines())



#print(glob.glob0("C:\\Users\\pucher\\Documents\\Seafile\\p4ne_training\\config_files","*.txt"))
