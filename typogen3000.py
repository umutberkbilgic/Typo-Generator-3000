import random

typos = {'a': "qwsz",
         'b': "vghn",
         'c': "xdfv",
         'd': "serfcx",
         'e': "wsdfr",
         'f': "dcvgtr",
         'g': "fvbhyt",
         'h': "gbnjuy",
         'i': "ujko",
         'j': "hnmkıu",
         'k': "jmloi",
         'l': "mkop",
         'm': "njkl",
         'n': "bhjm",
         'o': "iklp",
         'p': "ol",
         'q': "wa",
         'r': "edft",
         's': "wazxde",
         't': "rfgy",
         'u': "yhji",
         'v': "cfgb",
         'w': "qase",
         'x': "zsdc",
         'y': "tghu",
         'z': "asx",
         ' ': " "}

FAILRATE = 0.2


while(True):
    msg = input("\nMsg : ")
    if(all(char in typos for char in msg) is False):
        print("Please enter a valid message.")
    else:
        res = ""
        for c in msg:
            deter = random.uniform(0, 1)
            
            if (deter <= FAILRATE): #there is a typo now
                typo_set = typos[c]
                typo_set_len = len(typo_set)
                random_typo_choice = random.choice(range(0, typo_set_len))
                random_typo_char = typo_set[random_typo_choice]

                res = res + random_typo_char
                
            else:
                res = res + c
                

        print ("Bahadir would say: " + res + "\n\n") 
        
        
        

    
