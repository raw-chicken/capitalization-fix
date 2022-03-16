import re
import json
from nltk.corpus import words
from nltk.corpus import wordnet

# Random variables
type1 = 'utf_8'
chapters = {'997'} 
novel_cap = 'rotabas.txt'

# Word checker


# Custom capitlization that works with punctuation
def capitalize(text):
    punc_filter = re.compile('([".!?;]\s*)')
    split_with_punctuation = punc_filter.split(text)
    for i,j in enumerate(split_with_punctuation):
        if len(j) > 1:
            split_with_punctuation[i] = j[0].upper() + j[1:]
    text = ''.join(split_with_punctuation)
    return text

def replace(line):
    if '</p>' in line:
        ind = line.index('</p>')
        line = '\n'.join([line[:ind],capitalize(line[ind+299:])])
    if '<p><strong>' in line:
        line = line.replace('<p><strong>', '').replace('</strong>', '')
    if '<p>' in line:
        line = line.replace('<p>', '')
    if len(line) > 0 and line[0] == ' ':
        line = line[1:]

    return line

def check(line):
    clean = re.sub('\W+',' ', line)
    cleanwords = clean.split(' ')
    for word in cleanwords:
        word = wordnet.morphy(word)
        if word is None:
            continue
        if word not in words.words():
            print("Unknown word:", word) 



with open(novel_cap) as f:
    data = f.read()

list = json.loads(data)

for c in chapters:
    file_in = 'raw/' + c + '.txt'
    file_out = 'clean/' + c + '_e.txt'

    with open(file_in, encoding=type1, errors='ignore') as f:
        text = f.read()

    with open(file_out, 'w', encoding=type1, errors='ignore') as f:
        text = text.lower().replace('</p><p>', '\n').replace('“', '"')
        for key in list.keys():
            text = text.replace(key, list[key])
        
        lines = text.split('\n')
        lines = lines[1::]

        for line in lines:
            if '<strong><strong>' in line:
                continue
            line = capitalize(replace(line))
            # check(line)
                
            f.write(line + '\n')

        
        
