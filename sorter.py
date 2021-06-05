#from pprint import pprint as pp
import urllib

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

def makehtml(r):
    links = ''
    for x in r:
        links += f'<a href="{folder}{x}">{x}</a>\n'
    html = f'<html>\n<head>\n</head>\n<body>\n{links}</body>\n</html>'
    return html

####################

results = search(le_dict)
print(makehtml(results))
