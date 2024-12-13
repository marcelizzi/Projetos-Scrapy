import scrapy

class ProxyScraperSpider(scrapy.Spider):
    #ID
    name = "newproxyscraper"
    #Request
    def start_requests(self):
        urls = ["https://free-proxy-list.net/web-proxy.html"]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    #Response
    def parse(self, response):
        for line in response.xpath("//table[@class='table table-striped table-bordered']//tr"):
            yield {
                "Proxy Name": line.xpath("./td[1]/a/text()").get(),
                "Domain": line.xpath("./td[2]/text()").get(),
                "Country": line.xpath("./td[3]/text()").get(),
                "Speed": line.xpath("./td[4]/text()").get(),
                "Popularity": line.xpath("./td[5]//div[@class='progress-bar']/text()").get(),
                }
    