import requests
from bs4 import BeautifulSoup

url = 'https://apps.timwhitlock.info/emoji/tables/unicode'

class EmojiExtractor():
    
    def __init__(self): 
        session = requests.Session()
        response = session.get(url) 
        html = response.text 

        soup = BeautifulSoup(html, 'html.parser')
        
        code_htmls = soup.findAll('td', {'class' : 'code'})
        desc_htmls = soup.findAll('td', {'class' : 'name'})

        self.emojis = {
            code_html.get_text() : desc_html.get_text().lower()
            for (code_html, desc_html) in zip(code_htmls, desc_htmls[::2])  
        }

        # TODO somethings wrong i can feel it, like somethings about to happen, but i dont know what
        self.emoji_codes = self.emojis.keys()



