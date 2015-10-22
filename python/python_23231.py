# scrapy :if FormRequest have jsessionid
yield FormRequest(url='http://xxx.tw/ca/toView?mtd=do', callback=self.parse3, formdata={'actId': str(actId)})
