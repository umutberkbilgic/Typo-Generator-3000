import requests
from bs4 import BeautifulSoup

URL = 'https://apps.timwhitlock.info/emoji/tables/unicode'

class EmojiExtractor():
    
    def __init__(self): 
        session = requests.Session()
        response = session.get(URL) 
        html = response.text 

        soup = BeautifulSoup(html, 'html.parser')
        
        code_htmls = soup.findAll('td', {'class' : 'code'})
        desc_htmls = soup.findAll('td', {'class' : 'name'})

        self.emojis = {
            code_html.get_text() : desc_html.get_text().lower()
            for (code_html, desc_html) in zip(code_htmls, desc_htmls[::2])  
        }

        self.emoji_codes = self.emojis.keys()

    def find_emoji_freqs(self, text):
        self.emoji_freqs = {
            code : text.count(code)
            for code in self.emoji_codes
        }



