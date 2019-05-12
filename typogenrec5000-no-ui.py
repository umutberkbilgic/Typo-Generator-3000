import random
import argparse

DEFAULT_LOOPY_BOI = 2
DEFAULT_FAIL_RATE = 0.3
DEFAULT_RANDOM_WORDS = 0.05

parser = argparse.ArgumentParser(description="feelin' a bit baho today?")
parser.add_argument('-l', '--loopy',  type=int, default=DEFAULT_LOOPY_BOI, help=f'set # of froot loops, default is {DEFAULT_LOOPY_BOI}')
parser.add_argument('-f', '--fail',  type=float, default=0.1, help=f'set drunkenness in range 0.0 to 1.0, default is {DEFAULT_FAIL_RATE}')
parser.add_argument('-r', '--random',  type=float, default=0.5, help=f'set grr factor in range 0.0 to 1.0, default is {DEFAULT_RANDOM_WORDS}')
parser.add_argument('-m', '--msg',  type=str, required=True, help=f'a string that makes too much sense as it is')
args = parser.parse_args()

RANDOM_RATE = args.random
FAIL_RATE = args.fail
tim = args.loopy
msg = args.msg


typos = {'a': "qwsz",   'b': "vghn",   'c': "xdfv",
         'd': "serfcx", 'e': "wsdfr",  'f': "dcvgtr",
         'g': "fvbhyt9", 'h': "gbnjuy", 'i': "ujko1",
         'j': "hnmkıu", 'k': "jmloi",  'l': "mkop",
         'm': "njkl",   'n': "bhjm",   'o': "iklp0",
         'p': "ol",     'q': "wa",     'r': "edft",
         's': "wazxde", 't': "rfgy",   'u': "yhji",
         'v': "cfgb",   'w': "qase",   'x': "zsdc",
         'y': "tghu",   'z': "asx"}

randoms = ["ay", "of", "yha", "ya", "lan" , "wtf", "aq"]


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

    msg = res

print(msg)
