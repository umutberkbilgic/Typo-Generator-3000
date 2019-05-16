import os, re, json
import editdistance

from emoji_extractor import EmojiExtractor
from pprint import pprint 

class MessageExtractor():

    def __init__(self, data_path):
        with open(data_path, 'r', encoding='utf-8') as in_file:
            self.raw_text = in_file.read() 
        
        self.__extract_messages()
        self.__create_vocabulary()
        self.__find_word_freqs()

    def __extract_messages(self):      
        regex_string = r'\b(\d+[/]\d+[/]\d+), (\d+:\d+) - Bahadır Durmaz: (.+)\n'
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
        self.vocabulary = {
            word.lower() for word in self.text.split()  
        }
    
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

    def find_closest_word(self, given_word): 
        min_edit_dis = int(1e9)

        for word in self.vocabulary:
            edit_dis = editdistance.eval(word, given_word)
            if edit_dis < min_edit_dis:
                min_edit_dis = edit_dis
                closest_word = word
        return closest_word

current_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_path, 'data', 'ozcs.txt')
message_extractor = MessageExtractor(data_path) 
