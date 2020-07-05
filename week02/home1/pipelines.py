# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
db_info = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'port': 3306,
    'db': 'test'
    }

class SpidersPipeline:
#     def process_item(self, item, spider):
#         return item
    def process_item(self, item, spider):
        title = item['title']
        movie_type = item['movie_type']
        time = item['time']
        connect = pymysql.Connect(
            host = db_info['host'],
            user = db_info['user'],
            password = db_info['password'],
            port = db_info['port'],
            db = db_info['db']
        )
        # 游标建立的时候就开启了一个隐形的事务
        cur = connect.cursor()
        try:
            v = [title,movie_type,time]
            # print(v[0])
            # print(v[1])
            # print(v[2])
            cur.execute('create table if not exists test.MaoYan(id bigint not null auto_increment,title varchar(10),movie_type varchar(100),time DATE,primary key(id))')
            cur.execute('insert into MaoYan(title,movie_type,time) values(%s,%s,%s)', v)
            connect.commit()
            cur.close()
        except Exception as e:
            print(e)
            connect.rollback()
            connect.close()
        return item


# class SpidersPipeline:
# #     def process_item(self, item, spider):
# #         return item
#     def process_item(self, item, spider):
#         title = item['title']
#         movie_type = item['movie_type']
#         time = item['time']
#         output = f'|{title}|\t|{movie_type}|\t|{time}|\n\n'
#         with open('./MaoYanmovie.txt', 'a+', encoding='utf-8') as article:
#             article.write(output)
#             article.close()
#         return item

