# Selenium Python how to get text(html source) from <div>
re.search(r'&lt;div.*?&gt;(*.?)&lt;/div&gt;', price.get_attribute('innerHTML')).group(1)
