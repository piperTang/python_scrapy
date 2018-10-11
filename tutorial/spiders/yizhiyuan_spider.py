import scrapy
from tutorial.items import TutorialItem
class yizhiyuanSpider(scrapy.Spider):
    name="yizhiyuan"
    allowed_domains="www.92ez.com"
    start_urls=[
        "https://www.92ez.com/?action=show&id=23471"
    ]
    def parse(self,response):
        for data in response.xpath("//div[@id='page']"):
            item=TutorialItem()
            item['title']=data.xpath(".//h1//text()").extract()
            item['date']=data.xpath(".//p[@class='post-date'][1]//text()").extract()
            # 获取文章内容
            item['content']=data.xpath(".//div[@class='post-body'][1]").extract()
            yield item
        next_page_url=response.xpath(".//p[@id='article-other-title']//a//@href").extract()
        # print(next_page_url)
        # 爬取分页数据
        if next_page_url:
            yield scrapy.Request(next_page_url[0], callback=self.parse,dont_filter=True)