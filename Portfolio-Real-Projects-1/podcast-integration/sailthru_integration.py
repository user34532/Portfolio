import requests

# Example: Sending a test request to Sailthru API
api_url = "https://api.sailthru.com/content"
response = requests.get(api_url, params={"limit": 10})

if response.status_code == 200:
    print("Sailthru API connection successful!")
else:
    print("Failed to connect to Sailthru API")
