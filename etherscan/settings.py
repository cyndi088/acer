# -*- coding: utf-8 -*-

# Scrapy settings for etherscan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'etherscan'

SPIDER_MODULES = ['etherscan.spiders']
NEWSPIDER_MODULE = 'etherscan.spiders'

MONGO_HOST = '1o746k7976.51mypc.cn'
MONGO_PORT = 31006
MONGO_USER = 'llps'
MONGO_PSW = 'llps&789'
MONGO_DB = 'neo_crawl_data'
MONGO_COLL = 'etherscan_token'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'etherscan (+http://www.yourdomain.com)'
# USER_AGENT_LIST = [
#     'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31',
#     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',
#     'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
#     'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
#     'Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
#     'Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
#     'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1',
#     'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:15.0) Gecko/20120910144328 Firefox/15.0.2',
#     'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
#     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
#     'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.13; ) Gecko/20101203',
#     'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
#     'Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50',
#     'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52',
#     'Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285',
#     'Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.7pre) Gecko/20070815 Firefox/2.0.0.6 Navigator/9.0b3',
#     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
# ]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 0.5
DOWNLOAD_TIMEOUT = 300
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 1
# CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'referer': 'https://etherscan.io/',
    'cookie': '__cfduid=de6e94b9990ecaf510c5e81ba4f18206e1527129086;_ga=GA1.2.799864744.1527129086;etherscan_autologin=True;etherscan_userid=cyndi088;etherscan_cookieconsent=True;showfavourite0x3136ef851592acf49ca4c825131e364170fa32b3=0;etherscan_pwd=4792:Qdxb:gWdslDXDqgylK/l0r3N8WpQzp9WmmAkS4NKmhfEcZg4=;_gid=GA1.2.705220662.1527472614;ASP.NET_SessionId=3d2c00vzkyyvxm4c5ipjkkjd;__cflb=1309472310;cf_clearance=b61561284fc42c9e8b1cddec2d2db3ac31ef59a6-1527745706-2700;_gat_gtag_UA_46998878_6=1;'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'etherscan.middlewares.ProxyMiddleware': 250,
    # 'etherscan.middlewares.RandomUserAgentMiddleware': 400,
    'etherscan.middlewares.EtherscanDownloaderMiddleware': 543
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'etherscan.pipelines.EtherscanPipeline': 300,
    'etherscan.pipelines.MongoPipeline': 200,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 0.5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 5
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# LOG_LEVEL = 'INFO'

RETRY_ENABLED = True
RETRY_TIMES = 3

# HTPERROR_ALLOW_ALL = True
