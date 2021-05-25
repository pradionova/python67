import requests

link = requests.get('https://stepic.org/media/attachments/course67/3.6.2/429.txt')
splitLink = link.text.strip().split('\n')
count = 0
for i in splitLink:
    if i:
        count += 1
    
print(len(splitLink))
print(count)