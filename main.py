import re
from termcolor import cprint
import json

with open('keywords.json', 'r') as kwJSON:
    keywords = json.load(kwJSON)

with open('data/1 800 FLOWERS COM INC_2015-06-28(00010848692015-09-11).txt', 'r') as tenK:
    text = tenK.read()

pat = re.compile(
    "("
    + "|".join(map(re.escape, sorted(keywords, key=len, reverse=True)))
    + ")",
    flags=re.I,
)

counts = {}
for w in map(str.strip, pat.split(text)):
    wl = w.lower()
    if wl in keywords:
        if wl in counts:
            counts[wl] += 1
        else:
            counts[wl] = 1
        cprint(w, keywords[wl]['color'], end=" ")
    else:
        print(w, end=" ")

print("\n" + str(counts))
