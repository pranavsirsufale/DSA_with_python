import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.
url = 'https://www.flipkart.com/'


r = requests.get(url, headers=headers)
# print(r.content)


# soup = BeautifulSoup(r.content, 'html5lib')


# print(r.content)
# 




#Python program to scrape website 
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
 
# URL = &quot;http://www.values.com/inspirational-quotes&quot;
r = requests.get(url)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
quotes=[]  # a list to store quotes
 
table = soup.find('div', attrs = {'id':'all_quotes'}) 
 
for row in table.findAll('div',
                         attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(&quot; #&quot;)[0]
    quote['author'] = row.img['alt'].split(&quot; #&quot;)[1]
    quotes.append(quote)
 
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)


