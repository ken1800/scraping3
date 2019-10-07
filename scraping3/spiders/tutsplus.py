# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TutsplusSpider(CrawlSpider):
    name = 'tutsplus'
    allowed_domains = ['tutsplus.com']
    start_urls = ['https://code.tutsplus.com/categories/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='alphadex__item-link']"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[@class='pagination__button pagination__next-button']"), callback='parse_item', follow=True),
    )
 
    def parse_item(self, response):
        item = {}
        for tr in response.xpath("//li[@class='posts__post']"):
            yield{
                
                'Title': tr.xpath(".//a[@class='posts__post-title ']/h1/text()").extract_first(),
                'url': tr.xpath(".//a[@class='posts__post-title ']/@href").extract_first(),
                'category':response.xpath("//span[@class='content-banner__title-breadcrumb-category']/text()").extract_first(),
            }
        
        # //li[@class="posts__post"] 
        # //a[@class="posts__post-title "]
        # //a[@class="posts__post-title "]/h1/text()
        # //div[@class='posts__post-primary-category']/a/text()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
       # return item
