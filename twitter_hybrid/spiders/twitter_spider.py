from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class someSpider(CrawlSpider):
  name = 'twitter'
  allowed_domains = []
  start_urls = [
               "https://twitter.com/"
               ]
  rules = (Rule(LinkExtractor(allow=()), callback='parse_obj', follow=True),)


  def parse_obj(self,response):
    with open("twitter", 'a+') as f:
	for link in LinkExtractor(allow=()).extract_links(response):
	    f.write(link.url + '\n')


