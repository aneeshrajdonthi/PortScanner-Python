

import socket
import threading
import sys

print_lock = threading.Lock()

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "No banner"
            with print_lock:
                print(f"[+] Port {port} is open | Banner: {banner}")
        sock.close()
    except:
        pass

def main():
    if len(sys.argv) != 2:
        print("Usage: python port_scanner.py <target-ip>")
        sys.exit(1)

    target = sys.argv[1]
    print(f"Scanning target: {target}")
    for port in range(1, 1025):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()

if __name__ == "__main__":
    main()
