# Running scrapy from script not including pipeline
from scrapy.utils.project import get_project_settings
settings = get_project_settings()
crawler = Crawler(settings)
