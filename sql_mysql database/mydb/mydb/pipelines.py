

import sqlite3

class QuotesPipeline(object):

    def open_spider(self, spider):
        self.connection = sqlite3.connect('quotedb.db')
        self.cur = self.connection.cursor()
        try:
            self.cur.execute(
                '''
                CREATE TABLE qtable(
                    title TEXT,
                    author TEXT,
                    tag TEXT)
                    ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass
    def close_spider(self, spider):
        self.connection.close()
      
    def process_item(self, item, spider):

        self.cur.execute('''
            INSERT INTO qtable(title, author, tag) VALUES (?,?,?)
            ''', (
                item.get('title'),
                item.get('author'),
                item.get('tag')
                ))
        self.connection.commit()
        return item



#MysqlDB

import mysql.connector

class QuotesPipeline(object):

    def open_spider(self, spider):
        self.connection =  mysql.connector.connect(
            host= 'localhost',
            username = 'root',
            password = 'pass',
            database ='myquote_db'
            )
        self.cur = self.connection.cursor()
        
        self.cur.execute(''' DROP TABLE IF EXISTS myqt ''')
        self.cur.execute(
            '''
            CREATE TABLE myqt(
                title TEXT,
                author TEXT,
                tag TEXT)
                ''')
        self.connection.commit()
       
    def close_spider(self, spider):
        self.connection.close()
      
    def process_item(self, item, spider):

        self.cur.execute('''
            INSERT INTO myqt(title, author, tag) VALUES (%s,%s,%s)
            ''', (
                item.get('title'),
                item.get('author'),
                item.get('tag')
                ))
        self.connection.commit()
        return item






#Mongodb

# import pymongo

# class QuotesPipeline(object):
#     collection_name = 'myqtable'

#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient("mongodb+srv://mtest:i6HmFNLLpassG@cluster0.tvylfi7.mongodb.net/?retryWrites=true&w=majority")
#         self.db = self.client['mymongoDB']
        
#     def close_spider(self, spider):
#         self.client.close()

#     def process_item(self, item, spider):
#         self.db[self.
        
#         collection_name].insert(item)

#         return item



      
       
