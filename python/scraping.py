import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.
url = 'https://www.flipkart.com/'


r = requests.get(url, headers=headers)
# print(r.content)

# content = r.text



# Initialize the object with an HTML page
# soup = BeautifulSoup(content, "html.parser")




import requests
from bs4 import BeautifulSoup

# Define the URL of the Twitter profile
url = "https://twitter.com/TwitterHandle"  # Replace 'TwitterHandle' with the desired profile handle.

# Headers to simulate a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}

# Send a GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Get the profile name
    # profile_name = soup.find('div', {'data-testid': 'UserName'}).get_text(strip=True)
    # print("Profile Name:", profile_name)
    
    # Example: Get the bio/description
    # bio = soup.find('div', {'data-testid': 'UserDescription'})
    # if bio:
    #     print("Bio:", bio.get_text(strip=True))
    
    # Example: Scrape tweets (may not work consistently due to dynamic content)
    tweets = soup.find_all('div', {'data-testid': 'tweet'})
    for i, tweet in enumerate(tweets, start=1):
        print(f"Tweet {i}: {tweet.get_text(strip=True)}")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
