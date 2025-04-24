import socket

# Simple port scanner by Carmel Delcy

target = input("Enter the IP or domain to scan: ")
ports = [21, 22, 23, 80, 443, 8080]  # Common ports to scan

print(f"\nScanning {target}...\n")

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
