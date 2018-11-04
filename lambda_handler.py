import xmltodict
import requests


def loadRSS(url):
    # creating HTTP response object from given url
    resp = requests.get(url)

    # # saving the xml file
    # with open('newest_720p.xml', 'wb') as f:
    #     f.write(resp.content)

    return xmltodict.parse(resp.content)


def createTrailerPage(rss):

    rss = loadRSS(rss)

    with open('newest_720p.html', 'wt') as f:
        # f.flush()
        f.write('<html><head><title>this is the title</title></head><body>')

    for movie in rss['records']['movieinfo']:
        title = movie['info']['title']
        url = movie['preview']['large']['#text']
        thumb = movie['poster']['location']

        with open('newest_720p.html', 'a') as f:

            f.write('<a href="' + url + '"><img src="' + thumb + '" title="' + title + '"></a>')
    with open('newest_720p.html', 'a') as f:
        f.write('</body></html>')
        f.close()


createTrailerPage('https://trailers.apple.com/trailers/home/xml/newest_720p.xml')
