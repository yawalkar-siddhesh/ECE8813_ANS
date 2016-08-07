import scrapy
import urllib2, cStringIO, zipfile 
import tldextract

class AlexaSpider(scrapy.Spider):
    name = "alexa"

    start_urls = []

    url = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'

    remotezip = urllib2.urlopen(url)
    zipinmemory = cStringIO.StringIO(remotezip.read())
    zip = zipfile.ZipFile(zipinmemory)
    for fn in zip.namelist():
        for domain in zip.read(fn).split():
            if int(domain.split(',')[0]) <= 10000:
                start_urls.append('http://' + domain.split(',')[1]+ '/')
            else:
                break

    def parse(self, response):
        with open("alexa_domains", 'r+') as f:
            for sel in response.xpath('//a/@href'): 
                r = sel.extract()
                ext = tldextract.extract(r)
                spaced = ' '.join(ext).strip()
                if spaced != "":
                    try:
                        f.write(spaced.replace(' ','.').lower() + '\n')
                    except UnicodeEncodeError as e:
                        print e
