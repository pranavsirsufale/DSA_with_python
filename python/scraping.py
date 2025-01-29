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




