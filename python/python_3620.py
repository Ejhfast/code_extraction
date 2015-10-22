# How do I make Selenium RC to not move the browser window?
selenium.getEval("this.browserbot.getCurrentWindow().moveTo((" + h + "),(" + v + "))");
selenium.getEval("this.browserbot.getCurrentWindow().resizeTo(" + w + "," + h + ")");
