# Importing tools from custom modules
from port_scan import vul_ports         # Port scanning tool
from brute_force import brute         # HTTP Basic Auth brute forcer
from web_scan import scan                  # Web vulnerability scanner (SQLi, XSS)

# Main function for the penetration testing toolkit
def main():
    # Display the menu
    print("\n  @ Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    print("3. Web Vulnerability Scanner")
    
    # Get user's tool choice
    ask= input("\nSelect a tool (1-3): ")

    # Port Scanner option
    if ask == "1":
        target = input("Enter IP/domain to scan: ")  # Ask for target IP/domain
        vul_ports(target)  # Call port scanner with default port range (1–1024)

    # Brute Forcer option
    elif ask == "2":
        url = input("Enter URL (with HTTP Basic Auth): ")  # Ask for target URL
        # Example hardcoded credentials for testing
        user = ["admin", "user", "test"]
        pwd = ["admin", "1234", "password", "admin123"]
        brute(url, user, pwd)  # Call brute force function

    # Web Vulnerability Scanner option
    elif ask == "3":
        url = input("Enter URL to scan for vulnerabilities: ")  # Ask for target website
        scan(url)  # Scan for SQL Injection and XSS

    # Invalid selection
    else:
        print("Invalid option")

# Entry point of the program
if __name__ == "__main__":
    main()
