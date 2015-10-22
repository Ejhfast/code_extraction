# Any help on cursor.execute and urljoin?
execute("SELECT * FROM `item` WHERE `url` = %s", (urljoin(base_url, item_url),))
