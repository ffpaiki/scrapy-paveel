import scrapy


class PaveelSpider(scrapy.Spider):
    name = 'paveelspider'
    allowed_domains = ['https://www.paveels.com/']
    start_urls = ['https://www.paveels.com/products/category/bathing/']

    def parse(self, response, **kwargs):
        for link in response.css('li.dropdown.transition > a::attr(href)').getall():
            yield response.follow(link, callback=self.parse_categories)



    def parse_categories(self, response):
        for link in response.css('div.product-name > a::attr(href)').getall():
            yield response.follow(link, callback=self.parse_product)

    def parse_product(self, response):
        yield{
            'name': response.css('h1::text').get(),
            'price': response.css('div.price.pos-relative::text').get().strip(),
            'description':
        }