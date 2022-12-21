import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quote'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').get()
            author = quotes.css('.author::text').get()
            tag = ', '.join(quotes.css('.tag::text').extract())
            yield {
                'title': title,
                'author':author,
                'tag': tag
                }
           

            