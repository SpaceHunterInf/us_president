import re
from argparse import ArgumentParser

def cleaning(s):
    s = str(s)
    s = re.sub('\s\W',' ',s)
    s = re.sub('\W,\s',' ',s)
    s = re.sub("\d+", "", s)
    s = re.sub('\s+',' ',s)
    s = re.sub('[!@#$_]', '', s)
    s = s.replace("co","")
    s = s.replace("https","")
    s = s.replace("[\w*"," ")
    return s


text_data = open('cleaned_full.txt', 'w', encoding='utf-8')

with open('fine_tuning_corpus.txt', 'r', encoding='utf-8') as f:
    article = f.readlines()

for l in article:
    text_data.write(cleaning(l))

text_data.close()