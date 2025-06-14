import socket

# Function to scan a range of ports on a target host
def vul_ports(target, port_range=(1, 1024)):
    print(f"Scanning {target} from port {port_range[0]} to {port_range[1]}...")
    open = []  # List to store open ports

    # Iterate through the specified port range
    for port in range(port_range[0], port_range[1] + 1):
        # Create a TCP socket (IPv4)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # Set timeout for connection attempt (0.5 seconds)
            
            # Attempt to connect to the target on the current port
            result = s.connect_ex((target, port))

            # If result is 0, connection succeeded → port is open
            if result == 0:
                print(f"  [OPEN] Port {port}")
                open.append(port)

    # If no open ports are found
    if not open:
        print("No open ports found.")
