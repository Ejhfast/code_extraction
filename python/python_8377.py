# downloading dynamic webcontent through Scrapy (python 2.7)
IMAGES_STORE = 'you dir path where you want to download images'
ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline'] #enable image pipline
