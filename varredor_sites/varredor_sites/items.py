# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join
import string

def tirar_espaco_em_branco(valor):
    return valor.strip()

def processar_caracteres_especiais(valor):
    return valor.replace(u"\u2019","")

def tornar_maisculo(valor):
    return valor.upper()

class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    frase = scrapy.Field(
        input_processor=MapCompose(tirar_espaco_em_branco,processar_caracteres_especiais),
        output_processor=TakeFirst()
    )
    autor = scrapy.Field(
        input_processor=MapCompose(tirar_espaco_em_branco,tornar_maisculo),
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        output_processor=Join(";")
    )
    # name = scrapy.Field()
    pass
