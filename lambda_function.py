import xmltodict
import requests
import boto3

output_filename = '/tmp/newest_720p.html'


def loadRSS(url):
    # creating HTTP response object from given url
    resp = requests.get(url)

    # # saving the xml file
    # with open('newest_720p.xml', 'wb') as f:
    #     f.write(resp.content)

    return xmltodict.parse(resp.content)


def createTrailerPage(rss):

    rss = loadRSS(rss)

    with open(output_filename, 'wt') as f:
        # f.flush()
        f.write('<html><head><title>Moie Trailers</title></head><body>')

    for movie in rss['records']['movieinfo']:
        title = movie['info']['title']
        url = movie['preview']['large']['#text']
        thumb = movie['poster']['xlarge']

        with open(output_filename, 'a') as f:

            f.write('<a href="' + url + '" type="video/x-msvideo"><img src="' + thumb + '" title="' + title + '"></a>')
    with open(output_filename, 'a') as f:
        f.write('</body></html>')
        f.close()


def uploadS3():
    # Create an S3 client
    s3 = boto3.client('s3')

    bucket_name = 'apple-trailers'

    # Uploads the given file using a managed uploader, whic+-h will split up large
    # files automatically and upload parts in parallel.
    s3.upload_file(output_filename, bucket_name, 'index.html', ExtraArgs={'ACL': 'public-read', 'ContentType': 'text/html'})


def lambda_handler(event="", context=""):

    createTrailerPage('https://trailers.apple.com/trailers/home/xml/newest_720p.xml')
    uploadS3()


lambda_handler()
