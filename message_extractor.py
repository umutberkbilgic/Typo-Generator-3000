import os, re, json
import editdistance

from emoji_extractor import EmojiExtractor
from pprint import pprint 


current_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_path, 'data', 'ozcs.txt')
tr_corpus_path = os.path.join(current_path, 'data', 'tr_word_stems_freqs.txt')
en_corpus_path = os.path.join(current_path, 'data', 'en_words.txt')

class MessageExtractor():
    def __init__(self, name):
        with open(data_path, 'r', encoding='utf-8') as in_file:
            self.raw_text = in_file.read()
        
        self.__extract_messages(name)
        self.__create_vocabulary()
        self.__find_word_freqs()
        self.__create_turkish_vocabulary(tr_corpus_path)
        self.__create_english_vocabulary(en_corpus_path)
        self.__create_unified_vocabulary()
        self.__find_links()
        self.__find_typo_rate()

    def __create_turkish_vocabulary(self, tr_corpus_path):
        skiprow = 6 
        self.turkish_word_freqs = {}

        with open(tr_corpus_path, 'r', encoding='utf-8') as corpus_file: 
            for row in range(skiprow): 
                next(corpus_file) 
            for row in corpus_file: 
                parts = row.split() 
                self.turkish_word_freqs[parts[0]] = parts[3] 
        
        self.turkish_vocabulary = set(self.turkish_word_freqs.keys())

    def __create_english_vocabulary(self, en_corpus_path):
        with open(en_corpus_path, 'r', encoding='utf-8') as corpus_file:
            self.english_vocabulary = { word.lower() for word in corpus_file.read().split() } 


    def __create_unified_vocabulary(self):
        self.unified_vocabulary = self.turkish_vocabulary.union(self.english_vocabulary)

    def __extract_messages(self, name):      
        regex_string = r'\b(\d+[/]\d+[/]\d+), (\d+:\d+) - {}: (.+)\n'.format(name)
        results = re.findall(regex_string, self.raw_text)

        self.message_data = [
            {
                "date": date,
                "time": time,
                "message": message
            } 
            for (date, time, message) in results
        ]

        self.messages = [
            element["message"] for element in self.message_data
        ]

        self.text = " ".join(self.messages)
    
    def __create_vocabulary(self):
        self.personal_vocabulary = set(self.text.lower().split())  
    
    def __find_word_freqs(self):
        all_words = self.text.lower().split()
        
        self.word_freqs = {}
        
        for word in all_words:
            if word not in self.word_freqs:
                self.word_freqs[word] = 1
            else:
                self.word_freqs[word] += 1             

    def dump_data(self, folder_path):
        with open(os.path.join(folder_path, 'message_data.json'), 'w', encoding='utf-8') as out_file:
            json.dump(self.message_data, out_file)

    def find_emoji_freqs(self):
        pass

    # gives you the closest bahadir word, a typoed one if typo option is True 
    def find_closest_word(self, given_word, typo=False): 
        min_edit_dis = int(1e9)

        for word in self.personal_vocabulary:
            if typo and word in self.unified_vocabulary:
                continue
            
            edit_dis = editdistance.eval(word, given_word)
            
            if edit_dis < min_edit_dis:
                min_edit_dis = edit_dis
                closest_word = word

        return closest_word
    
    def __find_links(self):
        regex_string = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        self.links = re.findall(regex_string, self.text)


    def __find_typo_rate(self):
        all_words = self.text.lower().split()
        
        count = 0
        for word in all_words:
            if word not in self.unified_vocabulary:
                count += 1
        
        self.typo_rate = count / len(all_words)


extractor = MessageExtractor('Enes') 
print(extractor.typo_rate)