# -*- coding: utf-8 -*-

# Scrapy settings for alexa project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'alexa'

SPIDER_MODULES = ['alexa.spiders']
NEWSPIDER_MODULE = 'alexa.spiders'

CONCURRENT_REQUESTS = 100

REACTOR_THREADPOOL_MAXSIZE = 20

LOG_LEVEL = 'INFO'

COOKIES_ENABLED = False

#RETRY_ENABLED = False
CONCURRENT_REQUESTS_PER_DOMAIN=1

DOWNLOAD_TIMEOUT = 15

AJAXCRAWL_ENABLED = True

ITEM_PIPELINES = {
    'alexa.pipelines.AlexaPipeline': 0,
}
#REDIRECT_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'alexa (+http://www.yourdomain.com)'
