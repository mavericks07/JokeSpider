# -*- coding: utf-8 -*-

# Scrapy settings for scrapyMongoDB project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'JokeSpider'

SPIDER_MODULES = ['JokeSpider.spiders']
NEWSPIDER_MODULE = 'JokeSpider.spiders'
ITEM_PIPELINES = ['JokeSpider.pipelines.JokespiderPipeline']
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'
COOKIES_ENABLED = True

# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# REDIS_URL = None
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'test_db'
MONGODB_DOCNAME = 'Joke'

