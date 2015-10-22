# Scrapy :: Issues with CSV exporting
self.exporter = CsvItemExporter(open(spider.name+".csv", "w"), False,
                                        fields_to_export=self.fields_to_export, quoting=csv.QUOTE_ALL)
