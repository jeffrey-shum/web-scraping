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
#        for article in response.css('li.views-row'):
#        article_data = list(zip(article_titles, article_urls))

#        if self.first == True:
#            with open(filename, 'w') as csvfile:
#                writer = csv.writer(csvfile, delimiter=',')
#                writer.writerow(['page_number', 'article_title', 'article_url'])
#                self.first = False

#        filename = 'pp_post_national_scrape.csv'
#        with open(filename, 'a') as csvfile:
#            writer = csv.writer(csvfile, delimiter=',')
#            for title, url in article_data:
#                writer.writerow([page_num, title, 'https://www.phnompenhpost.com' + url])

#set up connection to URL
#url_to_increment = 
#page_num = 0
#while True:
#    url = url_to_increment + str(page_num)
#    try:
#        response = requests.get(url)
#        page_num += 1
#        status = response.status_code
#        time.sleep(20 + random.random())

#begin collecting article links


#increment the page number of this URL then use requests to get the html and also the article links

#begin crawling articles
    #as crawling store html of each article as well as url of the article  
        #TODO: determine what file type to save data
    #depending on news outlet, control the crawling rate
        #include some randomness to imitate human user

#continue retrieving articles
    #for Phnom Penh Post this will require using selenium to click 'Load More' button

#allow functionality to start and stop the crawler
