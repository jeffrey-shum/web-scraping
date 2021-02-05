# article_scraper.py

import scrapy
import json


class ArticleScraper(scrapy.Spider):
    name = 'article_scraper'
    download_delay = 5

    domain = 'https://www.phnompenhpost.com'
    filename = 'articles.jl'
    start_urls = []
    with open(filename, 'r') as f:
        for line in f:
            dct = json.loads(line)
            start_urls.append(domain + dct["link"])

    #article_link_samples = ['/national/adb-graduates-not-ready-work',
                            #'/national/steep-drop-flights-siem-reap-forces-airport-layoffs']
    #domains = ['https://www.phnompenhpost.com'] * len(article_link_samples)
    #start_urls = [ domain + internal_link for domain, 
                    #internal_link in list(zip(domains, article_link_samples))]

    def parse(self, response):
        yield {
            "url": response.url[29:], #grab internal link only
            "author": response.css('p span::text').get().strip(),
            "article_body": response.css("#ArticleBody").get(),
            "article_header": response.css('.article-author-wrapper p').get()
            }

