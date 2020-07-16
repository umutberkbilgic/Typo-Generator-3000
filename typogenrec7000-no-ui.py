import random
import argparse

DEFAULT_LOOPY_BOI = 2
DEFAULT_FAIL_RATE = 0.1
DEFAULT_RANDOM_WORDS = 0.5
DEFAULT_PROB_DISTANCE = 0.8

parser = argparse.ArgumentParser(description="feelin' a bit baho today?")
parser.add_argument('-l', '--loopy',  type=int, default=DEFAULT_LOOPY_BOI, help=f'set # of froot loops, default is {DEFAULT_LOOPY_BOI}')
parser.add_argument('-f', '--fail',  type=float, default=DEFAULT_FAIL_RATE, help=f'set drunkenness in range 0.0 to 1.0, default is {DEFAULT_FAIL_RATE}')
parser.add_argument('-r', '--random',  type=float, default=DEFAULT_RANDOM_WORDS, help=f'set grr factor in range 0.0 to 1.0, default is {DEFAULT_RANDOM_WORDS}')
parser.add_argument('-p', '--prob',  type=float, default=DEFAULT_PROB_DISTANCE, help=f'set prob for: if random > prob, more distant key is sacrificed {DEFAULT_PROB_DISTANCE}')
parser.add_argument('-m', '--msg',  type=str, required=True, help=f'a string that makes too much sense as it is')
args = parser.parse_args()

RANDOM_RATE = args.random
FAIL_RATE = args.fail
tim = args.loopy
msg = args.msg
prob = args.prob


typos = {'a': "sqz,wxe",   'b': "vghn,fj", 'c': "xdfv,sg",
         'd': "sfxce,wrz", 'e': "wdr,sf",  'f': "dgrc,etv",
         'g': "fvth,by",   'h': "bgyj,nu", 'i': "şğ,üpç",
         'j': "uhnmk,ı",   'k': "mjıl,öo", 'l': "ökoş,çp",
         'm': "nöjk,hl",   'n': "bmhj,gk", 'o': "ıpl,kş0",
         'p': "oşğ,li",    'q': "aw,s",    'r': "eft,gd",
         's': "zaw,xeq",   't': "rgy,fh",  'u': "yjı,hk",
         'v': "cfgb,dh",   'w': "qse,ad",  'x': "zcsd,af",
         'y': "thu,gj",    'z': "asx,d",   'ı': "uko,jl" , 
         'ğ':"piü,ş",      'ü': "ği,ş",    'ö': "mklç,şj",
         'ç':"ölş,ki",     'ş':"çlpi,ğoöü"}

randoms = ["ay", "of", "yha", "ya", "lan" , "wtf", "aq", "abi", "8"]


msg = msg.lower() #convert msg to lowercase

for i in range(0, int(tim)):

    res = "" #result string

    # iterate over all characters and change them randomly
    for c in msg:
        if(c in typos):
            determine_typo = random.uniform(0, 1)
            
            if (determine_typo <= FAIL_RATE): #there is a typo now

                probarr = typos[c].split(",")
                determine_distance = random.uniform(0, 1)

                typo_f = probarr[0]

                if(determine_distance >= prob): # a more distant key is going to be typod with lower probability
                    typo_f = probarr[1]

                res += typo_f[random.choice(range(0, len(typo_f)))]                        
            else:
                res = res + c
        else:
            determine_random = random.uniform(0, 1)
            if (determine_random <= RANDOM_RATE): # there is random now
                res += " " + randoms[random.choice(range(0, len(randoms)))] + " "
            res = res + c

    msg = res

print(msg)
