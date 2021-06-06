from pprint import pprint as pp
import urllib.request as ul

#read in csv
csvfile = open('python tags.csv')
csv = csvfile.read()

#prepare csv
csv.strip('\n')
nlcsv = csv.split('\n')

#ask for folder
folder = input('Enter folder name/path: ')
if not folder[len(folder) - 1] == '/':
    folder += '/'

####################

templatefile = ul.urlopen('https://jq30.github.io/sorter/template.html')
template = str(templatefile.read())[2:]
template = template.strip("'")
template = template.replace('\\n', '\n')
template = template.replace('\\t', '\t')

template = template.split('<!--&-->')

####################

def makedict():
    d = {}
    i = 1
    while i < len(nlcsv):
        s = nlcsv[i]
        
        #if the file is attached with multiple tags
        if '"' in s:
            tags = s[ s.find('"') + 1 :]
            tags = tags[: tags.find('"') ]
            s = s.split(',')
            
        #if only one tag
        else:
            s = s.split(',')
            tags = s[1]
        
        #key and tags (as list)
        key = s[0]
        tags = tags.split(',')
        
        #gets rid of any unwanted spaces
        x = 0
        while x < len(tags):
            tags[x] = tags[x].strip(' ')
            x += 1
        
        #assigns tags
        d[key] = tags
        i += 1
    return d

le_dict = makedict()

def search(d):
    l = []
    query = input('Enter tag: ')
    for x in d:
        if query in d[x]:
            l.append(x)
    return l

def oldmakehtml(r):
    links = ''
    for x in r:
        links += f'<a href="{folder}{x}">{x}</a>\n'
    html = f'<html>\n<head>\n</head>\n<body>\n{links}</body>\n</html>'
    return html

def makeheader(r):
    html = ''
    
    html += template[0]
    h1 = template[1]
    h1 = h1.replace('{n}', str(len(r)))
    html += h1
    html += template[2]
    
    return html

def makecards(r):
    html = ''
    i = 0
    while i < len(r):
        if i % 5 == 0 and i != 0:
            html += template[4]
            html += template[2]
        
        x = template[3].replace('{link}', folder + r[i])
        x = x.replace('{filename}', r[i])
        html += x
        i += 1
    return html

def makefooter(r):
    html = ''
    html += template[4]
    html += template[5]
    
    return html

def makehtml(r):
    html = ''
    
    head = makeheader(r)
    html += head
    
    cards = makecards(r)
    html += cards
    
    foot = makefooter(r)
    html += foot
    return html

####################


results = search(le_dict)
final = makehtml(results)

print(final)

