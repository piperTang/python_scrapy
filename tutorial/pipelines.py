# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from tutorial.settings import MYSQL_HOST, MYSQL_DBNAME, MYSQL_USER, MYSQL_PASSWD,MYSQL_PORT
class TutorialPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
        host = MYSQL_HOST,
        db = MYSQL_DBNAME,
        user = MYSQL_USER,
        passwd = MYSQL_PASSWD,
        charset = 'utf8',
        use_unicode = True
        )
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        # item['title']=str.replace("\n","  ",item['title'])
        # item['title']=item['title'].
        # item['content']=str.replace("\n","  ",item['content'])
        self.cursor.execute(
            "insert into scrapy_yizhiyuan(title, date,content) value(%s, %s, %s)",
            (item['title'],self.connect.escape(item['date']),self.connect.escape(item['content'])))
        self.connect.commit()
        return item
    def close_spider(self,spider):
        self.connect.close()
