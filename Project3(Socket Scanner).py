import socket

try:
    target = input("Enter an ip address: ")
    target = socket.gethostbyname(target)
except socket.gaierror:
    print("No such Address")
    exit()

start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print("Looking for open ports...")
for port in range(start_port,end_port +1):
    s = socket.socket()
    s.settimeout(0.3)
    result = s.connect_ex((target,port))
    if result == 0:
        print(f"Port: {port} is Open")
    s.close()

print("\nScan Complete.")