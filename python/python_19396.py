# Firefox + Selenium in python: How to interactively get an element html?
driver.execute_script("for(var i = 0; i &lt; document.links.length; i++){document.links[i].onclick = function clicked(){var e = document.createElement('a'); e.setAttribute('id','myUniqueID'); e.setAttribute('value', this); document.getElementsByTagName('body')[0].appendChild(e);};}")
