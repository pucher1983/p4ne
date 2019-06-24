import glob
import ipaddress


lab_path = "C:\\Users\\pucher\\Documents\\Seafile\\p4ne_training\\config_files"
file_list2 = glob.iglob(lab_path + "\\*.txt")
dict_addr = {}
for f in file_list2:
    with open(f) as file:
        content = file.readlines()
        for line in content:
            if line.find('ip address ') > 0:
                temp_arrd = line.strip()[11:]
                try:
                    addr = ipaddress.IPv4Address(temp_arrd.split(' ')[0])
                except ipaddress.AddressValueError:
                    pass
                else:
                    if not temp_arrd in dict_addr:
                        dict_addr[temp_arrd]=1
print(sorted(dict_addr.keys()))
