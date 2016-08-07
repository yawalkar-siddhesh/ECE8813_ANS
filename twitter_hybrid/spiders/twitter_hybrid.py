import scrapy
import urllib2, cStringIO, zipfile 
import tldextract
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import httplib


class AlexaSpider(scrapy.Spider):
    name = "twitter_hybrid"
    allowed_domains = []
    start_urls = ["https://twitter.com/"]
    rules = (Rule(LinkExtractor(allow=()), callback='parse', follow=True),)


    def __init__(self):
        self.f = open('domains/twitter_hybrid_domains','a+')

    def parse(self, response, max_retry=3):
        domain = ' '.join(response.url).strip().lower().replace(' ', '.') 
        self.f.write(domain + '\n')

        for sel in response.xpath('//a/@href'): 

            r = sel.extract()
            ext = tldextract.extract(r)

            if ext.tld != "" and ext.domain != "":
                try:

                    spaced = ' '.join(ext).strip()
                    domain = spaced.replace(' ','.').lower()
                    #yield scrapy.Request('http://' + domain + '/' , callback=self.validate)
                    self.f.write(domain + '\n')

                except UnicodeEncodeError as e:
                    continue

    def validate(self, response, retry=0, max_retry=0):
        self.f.write(response.url + '\n')
