# in log file server adds ip-addresses, that took requests
# Analyse last N addresses and save them into new file with pair: "ip-adress - number of requests"

# pass all local ip-addresses: 192.169.*.*

from collections import OrderedDict, defaultdict, deque

N = 3000
with open('big_log.txt', "r", encoding="utf-8") as f:
    log = deque(f, N)

data = OrderedDict()
spam = defaultdict(int)

for item in log:
    ip = item[:-1]

    if not  ip.startswith('192.168'):
        spam[ip] += 1
        data[ip] = 1

data.update(spam)  # adding keys from spam to data

with open("data.txt", "w", encoding="utf-8") as f:
    for key, value in data.items():
        f.write(f"{key} - {value} \n")


