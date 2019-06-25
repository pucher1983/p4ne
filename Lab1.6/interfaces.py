import glob
import ipaddress
import re


def find_hostnames(input_str):
    if re.match("hostname", input_str):
        return input_str[9:]
    else:
        return None

def find_ips(input_str):
    if re.match("ip address \d{1,3}",input_str):
        return input_str
    else:
        return None

interfaces = []
ip_addresses = []
hostnames = {}
hostnames_ips = {}

lab_path = "C:\\Users\\pucher\\Documents\\Seafile\\p4ne_training\\config_files"
file_list = glob.iglob(lab_path + "\\*.txt")
dict_addr = {}
for f in file_list:
    with open(f) as file:
        content = file.readlines()
        for line in content:
            pass # to be done
            temp = find_hostnames(line.strip())
            if temp:
                # print(file.name + temp)
                hostnames[file.name] = [temp,[]]

print(hostnames)

for file_path in hostnames.keys():
    file = open(file_path)
    content = file.readlines()
    for line in content:
        temp = find_ips(line.strip())
        if temp:
            # temp2 = hostnames[file.name]
            hostnames[file.name][1].append(temp)
    file.close()

print(hostnames)
