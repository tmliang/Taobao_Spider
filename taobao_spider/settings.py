# -*- coding: utf-8 -*-

# Scrapy settings for taobao_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'taobao_spider'

SPIDER_MODULES = ['taobao_spider.spiders']
NEWSPIDER_MODULE = 'taobao_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'   #设置用户代理值

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  #不遵循 robots.txt协议

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'taobao_spider.middlewares.TaobaoSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'taobao_spider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'taobao_spider.pipelines.TaobaoSpiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

SCHEDULER = "scrapy_redis.scheduler.Scheduler"  #启用Redis调度存储请求队列
SCHEDULER_PERSIST = True    #不清除Redis队列、这样可以暂停/恢复 爬取
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  #确保所有的爬虫通过Redis去重
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
REDIS_HOST = '127.0.0.1'  # 也可以根据情况改成 localhost
REDIS_PORT = 6379

USER_AGENT_LIST = ['zspider/0.9-dev http://feedback.redkolibri.com/',
                    'Xaldon_WebSpider/2.0.b1',
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)',
                    'Mozilla/5.0 (compatible; Speedy Spider; http://www.entireweb.com/about/search_tech/speedy_spider/)',
                    'Speedy Spider (Entireweb; Beta/1.3; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Entireweb; Beta/1.2; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Entireweb; Beta/1.1; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Entireweb; Beta/1.0; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Beta/1.0; www.entireweb.com)',
                    'Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)',
                    'Speedy Spider (http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (http://www.entireweb.com)',
                    'Sosospider+(+http://help.soso.com/webspider.htm)',
                    'sogou spider',
                    'Nusearch Spider (www.nusearch.com)',
                    'nuSearch Spider (compatible; MSIE 4.01; Windows NT)',
                    'lmspider (lmspider@scansoft.com)',
                    'lmspider lmspider@scansoft.com',
                    'ldspider (http://code.google.com/p/ldspider/wiki/Robots)',
                    'iaskspider/2.0(+http://iask.com/help/help_index.html)',
                    'iaskspider',
                    'hl_ftien_spider_v1.1',
                    'hl_ftien_spider',
                    'FyberSpider (+http://www.fybersearch.com/fyberspider.php)',
                    'FyberSpider',
                    'everyfeed-spider/2.0 (http://www.everyfeed.com)',
                    'envolk[ITS]spider/1.6 (+http://www.envolk.com/envolkspider.html)',
                    'envolk[ITS]spider/1.6 ( http://www.envolk.com/envolkspider.html)',
                    'Baiduspider+(+http://www.baidu.com/search/spider_jp.html)',
                    'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
                    'BaiDuSpider',
                    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com',
                   ]

DOWNLOADER_MIDDLEWARES = {
    'taobao_spider.MidWare.HeaderMidWare.ProcessHeaderMidware': 543,
}

MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "tbdb"  # 库名
MONGO_COLL = "taobao"  # collection名
# MONGO_USER = "username"
# MONGO_PSW = "password"
