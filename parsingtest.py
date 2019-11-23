from bs4 import BeautifulSoup 
import requests

url = 'https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary'

def get_html(url):
    arr = requests.get(url)
    return arr.text

def get_content(html):

    soup = BeautifulSoup(html, 'html.parser')
    bloks = soup.find('div', class_ = 'mr-3').find_all('div', class_ = 'listing-item-main')
    for blok in bloks:
        name = blok.find('a').text
        price = blok.find('p', class_='listing-item-title').text.strip()
        print(price)
    
    
    
get_content(get_html(url))


