import glob
import re
from flask import Flask

file_host_ip_dict = {}
host_ip_dict = {}


def find_hostnames(input_str):
    if re.match("hostname", input_str):
        return input_str[9:]
    else:
        return None


def find_ips(input_str):
    if re.match("ip address \d{1,3}",input_str):
        return input_str[11:]
    else:
        return None


lab_path = "C:\\Users\\pucher\\Documents\\Seafile\\p4ne_training\\config_files"
file_list = glob.iglob(lab_path + "\\*.txt")
dict_addr = {}
for f in file_list:
    with open(f) as file:
        content = file.readlines()
        for line in content:
            temp = find_hostnames(line.strip())
            if temp:
                file_host_ip_dict[file.name] = [temp, []]
for file_path in file_host_ip_dict.keys():
    file = open(file_path)
    content = file.readlines()
    for line in content:
        temp = find_ips(line.strip())
        if temp:
            file_host_ip_dict[file.name][1].append(temp)
    file.close()
for i in file_host_ip_dict:
    host_ip_dict[file_host_ip_dict[i][0]]=file_host_ip_dict[i][1]

print(host_ip_dict)

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "Lab 2.2 web site. Go to /config to list the hostnames. Go to /configs/hostname to view all IP ot the host"


@app.route("/configs")
def configs():
    s = ''
    for i in host_ip_dict:
        s += i + '\n'
    return s

@app.route("/configs/<hostname>")
def host_ips(hostname):
    return str(host_ip_dict[hostname])


if __name__ == '__main__':
    app.run(debug=True)
