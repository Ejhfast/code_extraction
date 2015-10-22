# Python Comet Server
StreamHub hub = new StreamHub();
hub.connect("http://myserver.com/");
hub.subscribe("newsfeed", function(sTopic, oData) { alert("new news item: " + oData.Title); });
