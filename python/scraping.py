import sys
import requests
from bs4 import BeautifulSoup


h = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

url = 'https://www.amazon.in/?tag=msndeskstdin-21&ref=pd_sl_p2tz0mpwp_b&adgrpid=1323813609675834&hvadid=82738617105964&hvnetw=o&hvqmt=p&hvbmt=bb&hvdev=c&hvlocint=&hvlocphy=149917&hvtargid=kwd-82739230651722:loc-90&hydadcr=15414_2338258&mcid=&msclkid=be94059f50a51adf27d5620515e70986'

'''
r = requests.get(url, headers=headers)
# print(r.content)

# content = r.text
# soup = BeautifulSoup(content, "html.parser")


# Send a GET request
response = requests.get(url, headers=headers)



# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')


    print(soup)
    
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
'''





sys.stdout.reconfigure(encoding='utf-8')


response = requests.get(url, headers=h)


if response.status_code == 200:
   
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Print the parsed HTML safely
    print(soup.prettify())
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
