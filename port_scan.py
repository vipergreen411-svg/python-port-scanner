# simple port scanner using Python sockets 
# Demonstrates port scanning and timeout
import socket

target = "127.0.0.1"
ports = range(1, 1025)

print(f"\n[+] Starting TCP scan on {target}\n")

for port in ports:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")

    except socket.error as e:
        print(f"[!] Error scanning port {port}: {e}")

    finally:
        s.close()

print("\n[+] Scan complete")
