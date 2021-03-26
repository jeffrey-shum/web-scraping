# scraper.py

#import modules:
import csv
import scrapy


class PPPostSpider(scrapy.Spider):
    name = 'pp_post_national'
#    start_urls = ['https://www.phnompenhpost.com/national?page=0']
    download_delay = 20.1

    start_urls = []
    for page_num in range(0, 6000):
        url = f'https://www.phnompenhpost.com/national?page='
        start_urls.append(url+str(page_num))

    def parse(self, response):
        page_num = response.url.split('/')[-1][14:]
        article_titles = response.css("li.views-row a::text").getall()
        article_urls = response.css("li.views-row a::attr(href)").getall()
        if article_urls is not None:
            for title, link in list(zip(article_titles, article_urls)):
                yield {
                    "page": page_num,
                    "title": title,
                    "link": link
                    }