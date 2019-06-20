import ipaddress
import random

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        network_is_ok = False
        while not network_is_ok:
            o1 = str(random.randint(11, 224)) + "."
            o2 = str(random.randint(0, 256)) + "."
            o3 = str(random.randint(0, 256)) + "."
            o4 = "0"
            prefix = "/" + str(random.randint(8, 24))
            network_address = o1 + o2 + o3 + o4 + prefix
            try:
                ipaddress.IPv4Network.__init__(self,network_address)
                network_is_ok = True
            except ValueError:
                network_is_ok = False


L = []
for i in range(0, 9):
    test = IPv4RandomNetwork()
    L.append((str(test.network_address),(str(test.prefixlen))))

def f(x):
    return x[1] + x[0]


print(L)

print(sorted(L, key=f))