import xmltodict
import requests


def loadRSS():
    # justadded
    url = 'https://trailers.apple.com/trailers/home/xml/newest_720p.xml'

    # creating HTTP response object from given url
    resp = requests.get(url)

    # # saving the xml file
    # with open('newest_720p.xml', 'wb') as f:
    #     f.write(resp.content)

    return xmltodict.parse(resp.content)


rss = loadRSS()

heading = '<html><head><title>this is the title</title></head><body>'
print(heading)

# print(doc['records']['movieinfo']['info']['title']['#text'])
for movie in rss['records']['movieinfo']:
    title = movie['info']['title']
    url = movie['preview']['large']['#text']
    thumb = movie['poster']['location']
    # print(title + " " + url + " " + poster)
    href = ('<a href="' + url + '"><img src="' + thumb + '" title="' + title + '"></a>')
    print(href)
    # <a href=" "><img src="flower.jpg" width="82" height="86" title="White flower" alt="Flower"></a>

print('</body></html>')
