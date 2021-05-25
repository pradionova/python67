import requests
baseurl = 'https://stepic.org/media/attachments/course67/3.6.3/'
filename = '699991.txt'
while True:
    link = requests.get(baseurl + filename)
    print(link.text)
    if link.text.startswith('We'):
        break
    else:
        filename = link.text