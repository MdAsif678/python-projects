with open("server.log") as f:
    lines = f.readlines()

    d = {}

    for line in lines:
        if "Failed" in line:
            ip = line.split()[-1]
            d[ip] = d.get(ip,0)+1

print(d)

maxi = 0
mini = float('inf')

most_ip = max(d , key=d.get)
least_ip = min(d , key=d.get)

print(f"{most_ip} failed {d[most_ip]} times (highest)")
print(f"{least_ip} failed {d[least_ip]} times (highest)")