import re
import json

# Random variables
type1 = 'utf_8'
chapters = {'988','991'} 
novel_cap = 'rotabas.txt'

# Custom capitlization that works with punctuation
def capitalize(text):
    punc_filter = re.compile('([".!?;]\s*)')
    split_with_punctuation = punc_filter.split(text)
    for i,j in enumerate(split_with_punctuation):
        if len(j) > 1:
            split_with_punctuation[i] = j[0].upper() + j[1:]
    text = ''.join(split_with_punctuation)
    return text



with open(novel_cap) as f:
    data = f.read()

list = json.loads(data)

for c in chapters:
    file_in = 'raw/' + c + '.txt'
    file_out = 'clean/' + c + '_e.txt'

    with open(file_in, encoding=type1, errors='ignore') as f:
        text = f.read()

    with open(file_out, 'w', encoding=type1, errors='ignore') as f:
        text = text.lower().replace('</p><p>', '\n').replace('“','"')
        for key in list.keys():
            text = text.replace(key, list[key])
        
        lines = text.split('\n')
        lines = lines[1::]

        for line in lines:
            if '<strong><strong>' in line:
                continue
            if '</p>' in line:
                ind = line.index('</p>')
                line = '\n'.join([line[:ind],capitalize(line[ind+299:])])
            if '<p><strong>' in line:
                line = line.replace('<p><strong>','').replace('</strong>','')
            if len(line) > 0 and line[0] == ' ':
                line = line[1:]
                
            line = capitalize(line)
            f.write(line + '\n')

        
        
