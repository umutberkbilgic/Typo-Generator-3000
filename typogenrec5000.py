import random

typos = {'a': "qwsz",   'b': "vghn",   'c': "xdfv",
         'd': "serfcx", 'e': "wsdfr",  'f': "dcvgtr",
         'g': "fvbhyt9", 'h': "gbnjuy", 'i': "ujko1",
         'j': "hnmkıu", 'k': "jmloi",  'l': "mkop",
         'm': "njkl",   'n': "bhjm",   'o': "iklp0",
         'p': "ol",     'q': "wa",     'r': "edft",
         's': "wazxde", 't': "rfgy",   'u': "yhji",
         'v': "cfgb",   'w': "qase",   'x': "zsdc",
         'y': "tghu",   'z': "asx",    ' ': " "}

randoms = ["ay", "of", "yha", "ya", "lan" , "wtf", "aq"]
RANDOM_RATE = 0.2

while(True):
    msg = input("\nTypo this, dumbass: ")
    tim = input("Loopy boi: ")
    FAIL_RATE = float(input("Failrate (0.0 - 1.0): "))
    RANDOM_RATE = float(input("Random word rate (0.0 - 1.0): "))
    
    msg = msg.lower() #convert msg to lowercase

    for i in range(0, int(tim)):

        res = "" #result string

        # iterate over all characters and change them randomly
        for c in msg:
            if(c in typos):
                determine_typo = random.uniform(0, 1)
                
                    
                if (determine_typo <= FAIL_RATE): #there is a typo now
                    res += typos[c][random.choice(range(0, len(typos[c])))]                        
                else:
                    res = res + c
            else:
                determine_random = random.uniform(0, 1)
                if (determine_random <= RANDOM_RATE): # there is random now
                    res += " " + randoms[random.choice(range(0, len(randoms)))] + " "
                res = res + c

        #report typo string
        print ("\n  -- Bahadır: \"" + res + "\"")

        msg = res
