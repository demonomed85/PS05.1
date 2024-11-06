import scrapy


class MynewparsSpider(scrapy.Spider):
    name = "mynewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lights = response.css('div.WdR1o')
        for light in lights:
            yield {"name": light.css('div.lsooF span::text').get(),
                   "url": light.css('div.lsooF a::attr(href)').get(),
                   "price": light.css('div.pY3d2 span::text').get()
                   }
