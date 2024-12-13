import scrapy
from scrapy.loader import ItemLoader
from varredor_sites.items import QuotesItem

# CamelCase
class QuotesToScrapeSpider(scrapy.Spider):
    # Identidade
    name = 'frasebot'

    # Request
    def start_requests(self):
        # Definir URLs a varrer
        urls = ['https://www.goodreads.com/quotes?_gl=1*xsqn54*_ga*MTAxMTcxNjQ4NC4xNzMzMjIxNDkz*_ga_37GXT4VGQK*MTczMzg0MDIxOC4xNi4xLjE3MzM4NDQ1MzQuMC4wLjA.']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        # Processamento do retorno do Response
        for element in response.xpath("//div[@class='quote']"):
            loader = ItemLoader(item=QuotesItem(), selector=element, response=response)
            loader.add_xpath("frase",".//div[@class='quoteText']/text()")
            loader.add_xpath("autor",".//span[@class='authorOrTitle']/text()")
            loader.add_xpath("tags",".//div[@class='greyText smallText left']/a[@href]/text()")
            yield loader.load_item()

            """
            yield {
                'frase': element.xpath(".//div[@class='quoteText']/text()").get(),
                'autor': element.xpath(".//span[@class='authorOrTitle']/text()").get(),
                'tags': element.xpath(".//div[@class='greyText smallText left']/a[@href]/text()").getall(),
            }
            """

        #Varrendo várias paginas
        
        try:
            link_prox_pag = response.xpath('//div/a[@class="next_page"]/@href').get()
            if link_prox_pag is not None:
                link_prox_pag_completo = response.urljoin(link_prox_pag)
                yield scrapy.Request(url=link_prox_pag_completo,callback=self.parse)
        except:
            #Se nao encontrar para a automação
            print('Chegamos na ultima pagina')