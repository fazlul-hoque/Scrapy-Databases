
BOT_NAME = 'mydb'

SPIDER_MODULES = ['mydb.spiders']
NEWSPIDER_MODULE = 'mydb.spiders'

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
   'mydb.pipelines.QuotesPipeline': 300,
}




