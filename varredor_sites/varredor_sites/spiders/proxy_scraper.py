import scrapy

class ProxyScraperSpider(scrapy.Spider):
    #ID
    name = "proxyscraper"
    #Request
    def start_requests(self):
        urls = ["https://www.us-proxy.org/"]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    #Response
    def parse(self, response):
        for line in response.xpath("//table[@class='table table-striped table-bordered']//tr"):
            yield {
                "ip_address": line.xpath("./td[1]/text()").get(),
                "port": line.xpath("./td[2]/text()").get(),
                "code": line.xpath("./td[3]/text()").get(),
                "country": line.xpath("./td[4]/text()").get(),
                "anonimity": line.xpath("./td[5]/text()").get(),
                "google": line.xpath("./td[6]/text()").get(),
                "google": line.xpath("./td[7]/text()").get(),
                "last_checked": line.xpath("./td[8]/text()").get()
                }
    