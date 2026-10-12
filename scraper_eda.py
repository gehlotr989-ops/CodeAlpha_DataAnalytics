import requests
from bs4 import BeautifulSoup
import pandas as pd

# टारगेट वेबसाइट (यहाँ हम उदाहरण के लिए कोट्स वेबसाइट का उपयोग कर रहे हैं)
url = 'http://quotes.toscrape.com/'
response = requests.get(url)

# HTML कंटेंट को पार्स करना
soup = BeautifulSoup(response.text, 'html.parser')

quotes_data = []

# डेटा एक्सट्रैक्ट करना
for quote in soup.find_all('div', class_='quote'):
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    quotes_data.append({'Quote': text, 'Author': author})

# डेटा को DataFrame में बदलना और CSV फाइल में सेव करना
df = pd.DataFrame(quotes_data)
df.to_csv('scraped_quotes.csv', index=False)

print("डेटा सफलताપूर्वक स्क्रैप और 'scraped_quotes.csv' के रूप में सेव हो गया है!")
print(df.head())